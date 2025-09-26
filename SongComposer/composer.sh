#!/bin/bash

# Change to the script's directory
cd "$(dirname "$0")"

# Check if prompt is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 '<prompt>'"
    echo "Example: $0 'Write a song about love'"
    exit 1
fi

# Activate Python virtual environment
source ../venv/bin/activate

# Install requirements
pip install -r ../requirements.txt

# Run the song composer with prompt
echo "Running Song Composer with prompt: $1"
python composer.py "$1"

# Deactivate virtual environment
deactivate
