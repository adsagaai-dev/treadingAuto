#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ensure_venv() {
  if python3 -m venv .venv 2>/dev/null; then
    return 0
  fi
  if command -v sudo >/dev/null 2>&1; then
    sudo DEBIAN_FRONTEND=noninteractive apt-get update -qq
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3-venv
  else
    apt-get update -qq
    DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3-venv
  fi
  python3 -m venv .venv
}

if [[ ! -d .venv ]]; then
  ensure_venv
fi

.venv/bin/pip install -q -U pip
.venv/bin/pip install -q -e '.[dev]'
