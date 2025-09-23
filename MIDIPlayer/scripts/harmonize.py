from music21 import converter, stream, chord, key, meter, instrument, note
import sys
import os

def harmonize(input_midi, output='../midi_files/harmonized.mid'):
    # Parse melody
    melody = converter.parse(input_midi)
    
    # Add 4/4 time signature if none exists
    if not melody.getTimeSignatures():
        melody.insert(0, meter.TimeSignature('4/4'))
    
    # Get all notes from original melody (preserve timing)
    all_notes = list(melody.flatten().notes)
    if not all_notes:
        print("No notes found in MIDI file")
        return

    # Analyze key (default to C if fails)
    try:
        detected_key = melody.analyze('key')
    except:
        detected_key = key.Key('C')

    print(f"Detected key: {detected_key}")

    # Create accompaniment part
    accomp = stream.Part()
    accomp.append(instrument.Piano())

    # Create measures for analysis only (don't modify original melody)
    melody_with_measures = melody.makeMeasures(inPlace=False)
    
    # Process each measure to add chords
    for m in melody_with_measures.getElementsByClass(stream.Measure):
        if not m.notes:
            # Empty measure - add rest
            accomp.append(note.Rest(quarterLength=4.0))
            continue

        # Get note names from this measure
        note_names = []
        for n in m.notes:
            if n.isNote:
                note_names.append(n.pitch.name)
            elif n.isChord:
                note_names.extend(p.name for p in n.pitches)

        if not note_names:
            accomp.append(note.Rest(quarterLength=4.0))
            continue
            
        # Find best chord for these notes
        best_chord, best_score = None, 0
        
        for deg in range(1, 8):
            for kind in ['triad', 'seventh']:
                try:
                    candidate = detected_key.chordFromDegree(deg, kind=kind if kind != 'triad' else None)
                except:
                    continue

                chord_pitches = [p.name for p in candidate.pitches]
                score = sum(1 for name in note_names if name in chord_pitches)

                if score > best_score:
                    best_score, best_chord = score, candidate

        # Add chord or rest
        if best_chord:
            best_chord = chord.Chord(best_chord)
            best_chord.quarterLength = 4.0  # Full measure chord
            accomp.append(best_chord)
        else:
            accomp.append(note.Rest(quarterLength=4.0))

    # Final score
    score = stream.Score()

    # Create melody part using original melody (preserve all timing and durations)
    melody_part = stream.Part()
    melody_part.append(instrument.Piano())
    
    # Copy all elements from original melody (notes, rests, etc.) to preserve timing
    for element in melody.flatten():
        melody_part.append(element)

    score.append(melody_part)
    score.append(accomp)

    # Write to file
    try:
        score.write("midi", fp=output)
        print(f"✅ Harmonized MIDI saved to {output}")
    except Exception as e:
        print(f"❌ Error saving harmonized MIDI: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python harmonize.py <input_midi_file> [output_midi_file]")
        print("Example: python harmonize.py ../midi_files/Erika.mid")
        print("Example: python harmonize.py ../midi_files/Erika.mid ../midi_files/Erika_harmonized.mid")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: Input file '{input_file}' not found!")
        sys.exit(1)
    
    # Set output file (use provided name or generate default)
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        # Generate output filename based on input
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_dir = os.path.dirname(input_file)
        output_file = os.path.join(output_dir, f"{base_name}_harmonized.mid")
    
    print(f"🎵 Harmonizing: {input_file}")
    print(f"💾 Output will be saved to: {output_file}")
    
    harmonize(input_file, output_file)
