#!/bin/bash

# Change to the script's directory
cd "$(dirname "$0")"

# Check if input file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 [input_file] [output_file]"
    echo "Example: $0 melody.txt output.mid"
    echo "If no arguments provided, uses melody.txt and output.mid"
    exit 1
fi

# Activate Python virtual environment
source ../venv/bin/activate

# Install requirements
pip install -r ../requirements.txt

# Run the converter
echo "Running Music Converter..."
if [ $# -eq 1 ]; then
    echo "Converting $1 to output.mid"
    python convert.py "$1"
elif [ $# -eq 2 ]; then
    echo "Converting $1 to $2"
    python convert.py "$1" "$2"
else
    echo "Converting melody.txt to output.mid"
    python convert.py
fi

# Deactivate virtual environment
deactivate
