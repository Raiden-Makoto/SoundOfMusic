import subprocess
import time

# Play MIDI file using FluidSynth command line
print("Playing MIDI file: ybwm.mid")
print("Using SoundFont: FluidR3_GM.sf2")
print("Press Ctrl+C to stop playback")

try:
    subprocess.run([
        "fluidsynth", 
        "-i", 
        "../soundfonts/FluidR3_GM.sf2", 
        "../midi_files/ybwm.mid"
    ])
except KeyboardInterrupt:
    print("\nPlayback stopped by user")
except Exception as e:
    print(f"Error playing MIDI file: {e}")