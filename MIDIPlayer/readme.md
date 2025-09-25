# MIDIPlayer

A MIDI playback and visualization system with organized file structure.

## Directory Structure

```
MIDIPlayer/
├── scripts/           # Python scripts for MIDI playback and visualization
│   ├── playsong.py    # MIDI file playback using FluidSynth
│   └── visualizer.py  # 3D audio visualization with PyQt
├── soundfonts/        # SoundFont files (.sf2)
│   ├── Arachno SoundFont - Version 1.0.sf2
│   ├── ElectricGuitar.sf2
│   ├── FluidR3_GM.sf2
│   ├── Guitar.sf2
│   ├── Piano.sf2
│   └── TimGM6mb.sf2
├── midi_files/        # MIDI files (.mid)
│   ├── ErikaTrombone.mid
│   └── ybwm.mid
├── audio_files/       # Audio files (.wav)
│   └── ybwm.wav
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Usage

### MIDI Playback
```bash
cd scripts
python playsong.py
```

### Audio Visualization
```bash
cd scripts
python visualizer.py
```

## Dependencies
See `requirements.txt` for required Python packages.

## File Paths
All scripts have been updated to use relative paths from the `scripts/` directory:
- SoundFonts: `../soundfonts/`
- MIDI files: `../midi_files/`
- Audio files: `../audio_files/`