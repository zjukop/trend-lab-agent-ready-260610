# Agent Ready

A tiny CLI that scans a repository and generates starter files that help coding agents contribute reliably.

## Install

```bash
pip install -e .
```

## Usage

From any repository root:

```bash
agent-ready init
```

This creates:

- `.agent/skills/repo.md`
- `.agent/checklists/delivery.md`
- `AGENT_READY.md`

## Development

```bash
pytest
python -m agent_ready.main init --repo .
```
