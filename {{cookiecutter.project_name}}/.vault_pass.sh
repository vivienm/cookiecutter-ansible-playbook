#!/usr/bin/env bash
set -euo pipefail
exec gpg -d .vault_pass.asc 2>/dev/null
