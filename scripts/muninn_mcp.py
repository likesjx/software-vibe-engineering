#!/usr/bin/env python3
"""Muninn MCP helper for SVE.

Provides CLI commands for interacting with MuninnDB via MCP protocol.
Used by the muninn-memory-habit skill for session bootstrap, recall,
and memory write-back.

Commands:
  bootstrap  - Start local server if needed, verify connectivity
  health     - Check MCP connectivity and required tools
  require    - Fail unless MCP is ready (for session gating)
  tools      - List available Muninn tools
  where-left-off - Retrieve recent active memory
  recall     - Recall relevant memory by context
  remember   - Store an atomic memory
  decide     - Store a decision with rationale
  call       - Call an arbitrary Muninn tool
"""
import argparse
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.parse
import urllib.request


DEFAULT_BASE_URL = "http://localhost:8750/mcp"
REQUIRED_TOOLS = (
    "muninn_where_left_off",
    "muninn_recall",
    "muninn_remember",
    "muninn_decide",
)
APPROVAL_REQUIRED_EXIT = 42
DEFAULT_MUNINN_DIR = pathlib.Path.home() / "code" / "muninndb"


class MuninnMcpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.message_url = None
        self._sse_response = None

    def connect(self) -> None:
        req = urllib.request.Request(self.base_url, headers={"accept": "text/event-stream"})
        self._sse_response = urllib.request.urlopen(req, timeout=10)
        endpoint = None
        while True:
            raw = self._sse_response.readline()
            if not raw:
                break
            line = raw.decode("utf-8", errors="replace").strip()
            if line.startswith("data: "):
                endpoint = line[len("data: "):].strip()
                break
        if not endpoint:
            self.close()
            raise RuntimeError("Muninn MCP handshake did not return a message endpoint")
        if endpoint.startswith("http://") or endpoint.startswith("https://"):
            self.message_url = endpoint
        else:
            parsed = urllib.parse.urlparse(self.base_url)
            origin = f"{parsed.scheme}://{parsed.netloc}"
            self.message_url = urllib.parse.urljoin(origin + "/", endpoint.lstrip("/"))
        self._post({"jsonrpc": "2.0", "id": "initialize", "method": "initialize",
                     "params": {"protocolVersion": "2025-03-26", "capabilities": {},
                                "clientInfo": {"name": "muninn_mcp.py", "version": "1.0"}}})
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})

    def close(self) -> None:
        if self._sse_response is not None:
            self._sse_response.close()
            self._sse_response = None

    def _post(self, payload: dict) -> dict:
        if not self.message_url:
            raise RuntimeError("Muninn MCP client is not connected")
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(self.message_url, data=body,
                                      headers={"content-type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=20) as response:
            raw = response.read().decode("utf-8", errors="replace")
            if not raw.strip():
                return {}
            return json.loads(raw)

    def tools_list(self) -> dict:
        return self._post({"jsonrpc": "2.0", "id": "tools-list", "method": "tools/list", "params": {}})

    def call_tool(self, name: str, arguments: dict) -> dict:
        return self._post({"jsonrpc": "2.0", "id": f"tool-{name}",
                            "method": "tools/call", "params": {"name": name, "arguments": arguments}})


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Muninn MCP helper")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("health")
    sub.add_parser("bootstrap")
    sub.add_parser("require")
    sub.add_parser("tools")
    w = sub.add_parser("where-left-off")
    w.add_argument("--limit", type=int, default=5)
    r = sub.add_parser("recall")
    r.add_argument("--context", action="append", required=True)
    r.add_argument("--limit", type=int, default=5)
    r.add_argument("--mode", default="semantic")
    rem = sub.add_parser("remember")
    rem.add_argument("--content", required=True)
    rem.add_argument("--concept")
    rem.add_argument("--summary")
    rem.add_argument("--type", default="fact")
    rem.add_argument("--tag", action="append", default=[])
    d = sub.add_parser("decide")
    d.add_argument("--decision", required=True)
    d.add_argument("--rationale", required=True)
    d.add_argument("--alternative", action="append", default=[])
    c = sub.add_parser("call")
    c.add_argument("tool_name")
    c.add_argument("--args-json", default="{}")
    return parser


def extract_tool_names(result: dict) -> list[str]:
    return [t["name"] for t in result.get("result", {}).get("tools", []) if isinstance(t.get("name"), str)]


def health_payload(base_url: str) -> dict:
    payload = {"base_url": base_url, "reachable": False, "required_tools_present": False,
               "missing_tools": [], "available_tools": [], "approval_required": False, "status": "unreachable"}
    client = MuninnMcpClient(base_url)
    try:
        client.connect()
        payload["reachable"] = True
        names = extract_tool_names(client.tools_list())
        payload["available_tools"] = names
        missing = [t for t in REQUIRED_TOOLS if t not in names]
        payload["missing_tools"] = missing
        payload["required_tools_present"] = not missing
        payload["status"] = "ready" if not missing else "missing_tools"
        payload["approval_required"] = bool(missing)
    except Exception as exc:
        payload["error"] = str(exc)
        payload["approval_required"] = True
    finally:
        client.close()
    return payload


def emit_approval_required(payload: dict) -> int:
    print("MUNINN BLOCKER: Muninn MCP is unavailable or incomplete. "
          "Operator approval is required before continuing without memory.", file=sys.stderr)
    print(json.dumps(payload, indent=2, sort_keys=True), file=sys.stderr)
    return APPROVAL_REQUIRED_EXIT


def resolve_local_server_dir() -> pathlib.Path | None:
    env_dir = os.environ.get("MUNINN_SERVER_DIR")
    candidates = []
    if env_dir:
        candidates.append(pathlib.Path(env_dir).expanduser())
    candidates.append(DEFAULT_MUNINN_DIR)
    for c in candidates:
        if (c / "muninndb-server").exists():
            return c
    return None


def try_start_local_server() -> dict:
    server_dir = resolve_local_server_dir()
    if server_dir is None:
        return {"started": False, "start_attempted": False, "start_reason": "local muninndb-server binary not found"}
    binary = server_dir / "muninndb-server"
    try:
        subprocess.Popen([str(binary), "--daemon"], cwd=server_dir,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    except Exception as exc:
        return {"started": False, "start_attempted": True, "start_reason": f"failed: {exc}"}
    time.sleep(1.0)
    return {"started": True, "start_attempted": True, "server_dir": str(server_dir)}


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "health":
        payload = health_payload(args.base_url)
        json.dump(payload, sys.stdout, indent=2, sort_keys=True)
        print()
        return 0 if payload["status"] == "ready" else 1

    if args.command == "bootstrap":
        payload = health_payload(args.base_url)
        if payload["status"] == "ready":
            json.dump(payload, sys.stdout, indent=2, sort_keys=True)
            print()
            return 0
        start_info = try_start_local_server()
        retry = health_payload(args.base_url)
        retry.update(start_info)
        if retry["status"] != "ready":
            return emit_approval_required(retry)
        json.dump(retry, sys.stdout, indent=2, sort_keys=True)
        print()
        return 0

    if args.command == "require":
        payload = health_payload(args.base_url)
        if payload["status"] != "ready":
            return emit_approval_required(payload)
        json.dump(payload, sys.stdout, indent=2, sort_keys=True)
        print()
        return 0

    client = MuninnMcpClient(args.base_url)
    client.connect()
    result = {}
    try:
        if args.command == "tools":
            result = client.tools_list()
        elif args.command == "where-left-off":
            result = client.call_tool("muninn_where_left_off", {"limit": args.limit})
        elif args.command == "recall":
            result = client.call_tool("muninn_recall", {"context": args.context, "limit": args.limit, "mode": args.mode})
        elif args.command == "remember":
            p = {"content": args.content, "type": args.type}
            if args.concept: p["concept"] = args.concept
            if args.summary: p["summary"] = args.summary
            if args.tag: p["tags"] = args.tag
            result = client.call_tool("muninn_remember", p)
        elif args.command == "decide":
            p = {"decision": args.decision, "rationale": args.rationale}
            if args.alternative: p["alternatives"] = args.alternative
            result = client.call_tool("muninn_decide", p)
        elif args.command == "call":
            result = client.call_tool(args.tool_name, json.loads(args.args_json))
        json.dump(result, sys.stdout, indent=2, sort_keys=True)
        print()
        return 0
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
