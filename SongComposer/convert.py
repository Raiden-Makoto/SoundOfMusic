#!/usr/bin/env python3
"""
Convert symbolic music output to MIDI file
Usage: python convert.py [input_file] [output_file]
"""

import sys
import re
import pretty_midi

def parse_symbolic_music(text):
    """Parse symbolic music format and extract notes and lyrics."""
    notes = []
    lyrics = []
    
    # Pattern to match "Lyric: [text]" and "Note: [note] [duration]"
    lyric_pattern = r'Lyric:\s*(.+)'
    note_pattern = r'Note:\s*([A-G]#?[0-9]+)\s+(\w+)'
    
    lines = text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for lyric
        lyric_match = re.search(lyric_pattern, line)
        if lyric_match:
            lyrics.append(lyric_match.group(1).strip())
            continue
            
        # Check for note
        note_match = re.search(note_pattern, line)
        if note_match:
            note_name = note_match.group(1)
            duration = note_match.group(2)
            notes.append((note_name, duration))
    
    return notes, lyrics

def note_name_to_midi_number(note_name):
    """Convert note name (e.g., 'C4') to MIDI number."""
    # Note mapping
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
        'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }
    
    # Parse note and octave
    match = re.match(r'([A-G]#?b?)(\d+)', note_name)
    if not match:
        raise ValueError(f"Invalid note name: {note_name}")
    
    note, octave = match.groups()
    octave = int(octave)
    
    # Calculate MIDI number (C4 = 60)
    midi_number = 12 + (octave * 12) + note_map[note]
    return midi_number

def duration_to_seconds(duration, tempo=96):
    """Convert duration name to seconds based on tempo."""
    # Duration mapping (in beats)
    duration_map = {
        'Whole': 4,
        'Half': 2,
        'Quarter': 1,
        'Eighth': 0.5,
        'Sixteenth': 0.25,
        'Thirty-second': 0.125
    }
    
    beats = duration_map.get(duration, 1)  # Default to quarter note
    # Convert beats to seconds: (beats * 60) / tempo
    seconds = (beats * 60) / tempo
    return seconds

def create_midi(notes, lyrics, output_file, tempo=96):
    """Create MIDI file from parsed notes and lyrics."""
    pm = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano
    
    current_time = 0.0
    
    for i, (note_name, duration) in enumerate(notes):
        # Convert note name to MIDI number
        midi_number = note_name_to_midi_number(note_name)
        
        # Convert duration to seconds
        note_duration = duration_to_seconds(duration, tempo)
        
        # Create note
        note = pretty_midi.Note(
            velocity=80,  # Note velocity (loudness)
            pitch=midi_number,
            start=current_time,
            end=current_time + note_duration
        )
        
        piano.notes.append(note)
        current_time += note_duration
    
    # Add instrument to PrettyMIDI object
    pm.instruments.append(piano)
    
    # Save MIDI file
    pm.write(output_file)
    print(f"MIDI file saved as: {output_file}")

def main():
    # Default input and output files
    input_file = "melody.txt"
    output_file = "output.mid"
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    try:
        # Read input file
        with open(input_file, 'r') as f:
            content = f.read()
        
        print(f"Reading from: {input_file}")
        
        # Parse symbolic music
        notes, lyrics = parse_symbolic_music(content)
        
        print(f"Found {len(notes)} notes and {len(lyrics)} lyrics")
        
        if not notes:
            print("No notes found in input file!")
            return
        
        # Create MIDI file
        create_midi(notes, lyrics, output_file)
        
        # Print summary
        print("\nNotes parsed:")
        for i, (note, duration) in enumerate(notes):
            lyric = lyrics[i] if i < len(lyrics) else ""
            print(f"  {note} ({duration}) - {lyric}")
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found!")
        print("Usage: python convert.py [input_file] [output_file]")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
