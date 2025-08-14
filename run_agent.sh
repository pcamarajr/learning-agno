#!/bin/bash

# Activate virtual environment and run Python scripts
# Usage: ./run_agent.sh src/agents/base/level_1_agent.py

# Add uv to PATH
export PATH="$HOME/.local/bin:$PATH"

# Activate virtual environment
source .venv/bin/activate

# Run the provided Python script
python "$@"
