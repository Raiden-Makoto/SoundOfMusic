#!/usr/bin/env python3
"""
Song Composer - Generate songs using AI model
Usage: python composer.py "<prompt>"
"""

import sys
import torch
from transformers import AutoTokenizer, AutoModel

def main():
    # Check if prompt is provided
    if len(sys.argv) != 2:
        print("Usage: python composer.py '<prompt>'")
        print("Example: python composer.py 'Write a song about love'")
        sys.exit(1)
    
    prompt = sys.argv[1]
    
    # Load model and tokenizer
    print("Loading model...")
    checkpoint_path = "Mar2Ding/songcomposer_sft"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint_path, trust_remote_code=True)
    model = AutoModel.from_pretrained(checkpoint_path, trust_remote_code=True)
    
    # Set device
    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    model.to(device)
    print(f"Using device: {device}")
    
    # Generate song
    print(f"Generating song with prompt: {prompt}")
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    song = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Save to file
    output_file = "melody.txt"
    with open(output_file, "w") as f:
        f.write(song)
    
    print(f"Song generated and saved to {output_file}")

if __name__ == "__main__":
    main()
