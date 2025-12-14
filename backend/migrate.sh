#!/usr/bin/env bash
set -e  # stop on error
set -o pipefail

# ─────────────────────────────────────────────
# OPTIONAL: Activate virtual environment
# ─────────────────────────────────────────────
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# ─────────────────────────────────────────────
# Check Alembic
# ─────────────────────────────────────────────
if ! command -v alembic &> /dev/null
then
    echo "Error: alembic not found. Install it: pip install alembic"
    exit 1
fi

# ─────────────────────────────────────────────
# Apply migrations
# ─────────────────────────────────────────────
echo "Running Alembic migrations..."
alembic upgrade head

echo "Migrations applied successfully!"
