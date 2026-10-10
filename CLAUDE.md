# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Study scripts for the Claude Certified Architect (CCA) exam. Each file is a standalone, heavily commented teaching example of an Anthropic API pattern — not a package. There are no tests, linters, or build steps.

## Setup and running

Uses a local venv at `.venv` (Python 3.14, `anthropic` SDK). On Windows PowerShell:

    .venv\Scripts\Activate.ps1
    pip install anthropic          # only dependency
    $env:ANTHROPIC_API_KEY = "..."  # the SDK reads this automatically
    python agent.py
    python api_check.py

## Scripts

- `agent.py` — a hand-written agentic tool-use loop (customer-support order lookup with a mock DB). Key ideas it demonstrates, which should be preserved when editing:
  - The loop exits only on `stop_reason == "end_turn"`; `MAX_ITERATIONS` is a safety valve, not the primary stop condition.
  - On `tool_use`, the assistant message is appended first, then all `tool_result` blocks go back in a single `user` message.
  - `execute_tool` never raises for unknown tools; `handle_tool_call` maps exceptions to structured error results (`is_error: True` with `errorCategory` transient / permission / validation / internal and `isRetryable`) so the model can decide whether to retry, self-correct, or escalate.
- `api_check.py` — minimal single `messages.create` call to verify the API key works.

## Conventions

- Files are organized as numbered "STEP" sections with box-drawing comment banners and explain the *why* inline; match this teaching style in new examples.
- Default model in the examples is `claude-haiku-4-5` (cheap, for learning).
- Credentials come only from the `ANTHROPIC_API_KEY` environment variable — `anthropic.Anthropic()` with no arguments. A prior commit ("remove keys") stripped hardcoded keys; don't reintroduce them.
