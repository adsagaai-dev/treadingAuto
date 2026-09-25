# treadingAuto

Python starter for trading automation workflows. Includes a dry-run trade engine, HTTP API, and CLI for local development and Cloud Agent verification.

## Setup

```bash
bash scripts/cloud-agent-install.sh
```

## Development

Run tests:

```bash
.venv/bin/pytest
```

Dry-run trade via CLI:

```bash
.venv/bin/treading-auto dry-run --symbol AAPL --quantity 1
```

Start the API (also available as the `api` Cloud Agent terminal):

```bash
.venv/bin/uvicorn treading_auto.api:app --host 0.0.0.0 --port 8000 --reload
```

- `GET /health` — readiness check
- `POST /trades/dry-run` — simulate a trade (`{"symbol": "AAPL", "side": "buy", "quantity": 1}`)
