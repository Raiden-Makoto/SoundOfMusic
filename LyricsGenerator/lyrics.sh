#!/bin/bash

# Change to the script's directory
cd "$(dirname "$0")"

# Check if starting lyrics are provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 '<starting_lyrics>'"
    echo "Example: $0 'It was a dark and stormy night'"
    exit 1
fi

# Initialize conda and activate environment
eval "$(conda shell.bash hook)"
conda activate mididdsp

# Install requirements
pip install -r ../requirements.txt

# Run the lyric generator with starting lyrics
echo "Running Lyrics Generator with starting lyrics: $1"
python lyricgenerator.py "$1"

# Deactivate conda environment
conda deactivate
