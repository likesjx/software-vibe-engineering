# Task Surface Guide

The task surface is the single file that tracks active implementation work. It bridges proposals (intent) and code (reality).

## Purpose

A task.md file serves as the human-readable work tracker for a project. It should answer:

1. What are we building right now?
2. What slices are in flight?
3. What is blocked or waiting?

## Structure

Your task surface should contain these sections:

### Current Slice

Name the active slice, link to its proposal, and set a status (in-progress, blocked, complete).

### Work Items

Use checkbox lists with IDs (WI-1, WI-2, etc). Each item should note acceptance criteria and which seams it touches.

### Blocked

List any blocked items with the reason and what unblocks them.

### Next Slice

Planned work that follows the current slice. Keep this short.

### Completed Slices

Archive completed slices with date, what was delivered, and any reality gaps (where implementation diverged from the proposal).

## Rules

1. One task surface per project - don't scatter work tracking across multiple files
2. Link to proposals - every work item should trace back to a proposal or design doc
3. Track reality gaps - when implementation diverges from the proposal, note it here
4. Keep it current - the task surface is worthless if it lags behind actual work
5. Slice boundaries matter - group work into discrete, completable slices rather than an infinite backlog

## Integration with Skills

The slice-closeout skill references the task surface to verify work completion. The proposal-maintainer skill uses it to keep proposals aligned with actual progress.
