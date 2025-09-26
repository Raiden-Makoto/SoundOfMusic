# SoundOfMusic 🎵

A complete AI-powered music generation pipeline that creates pop songs in Taylor Swift's style. The system generates lyrics using a fine-tuned GPT-2 model, creates melodies with a Transformer model, converts them to MIDI format, and provides real-time audio visualization.

## 🎯 Project Overview

This project consists of three main components:
- **LyricsGenerator**: AI-powered lyric generation using a fine-tuned GPT-2 model
- **SongComposer**: AI-powered melody generation using a Transformer model
- **MIDIPlayer**: MIDI playback, harmonization, and 3D audio visualization

## 🔄 Complete Pipeline

The music generation pipeline follows this workflow:

1. **Generate Lyrics** → 2. **Compose Melody** → 3. **Convert to MIDI** → 4. **Play & Visualize**

```
LyricsGenerator → SongComposer → MIDI Conversion → MIDIPlayer
     ↓               ↓              ↓              ↓
  lyrics.txt    melody.txt    output.mid    Audio Playback
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Any OS (tested on macOS 26 Tahoe)
- Homebrew or equivalent (for Python installation)

**NOTE: SongComposer is a large model and requires at least 17GB of available storage. It is also recommended to have 18+ GB of RAM**

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SoundOfMusic
   ```

2. **Install Python 3.11** (if not already installed)
   ```bash
   brew install python@3.11
   ```

3. **Create and activate virtual environment**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📝 LyricsGenerator

### Overview
The LyricsGenerator uses a pre-trained GPT-2 model fine-tuned on Taylor Swift's song lyrics to generate new lyrics in her style.

### Usage

#### Method 1: Using the shell script (Recommended)
```bash
cd LyricsGenerator
./lyrics.sh "It was a dark and stormy night"
```

#### Method 2: Direct Python execution
```bash
cd LyricsGenerator
source ../venv/bin/activate
python lyricgenerator.py "Your starting lyrics here"
```

### Features
- Command-line argument support for starting lyrics
- Automatic model loading from `model_checkpoint/`
- GPU/MPS/CPU device detection
- Configurable generation parameters

## 🎼 SongComposer

### Overview
The SongComposer uses a Transformer model to generate melodies and musical notation based on prompts. It outputs symbolic music format that can be converted to MIDI.

### Usage

#### Method 1: Using the shell script (Recommended)
```bash
cd SongComposer
./composer.sh "Write a song about love"
```

#### Method 2: Direct Python execution
```bash
cd SongComposer
source ../venv/bin/activate
python composer.py "Write a song about love"
```

### Features
- Command-line argument support for prompts
- Automatic model loading from Hugging Face
- GPU/MPS/CPU device detection
- Outputs symbolic music format (notes and lyrics)

### MIDI Conversion

The generated symbolic music can be converted to MIDI format:

#### Method 1: Using the shell script (Recommended)
```bash
cd SongComposer
./convert.sh melody.txt output.mid
```

#### Method 2: Direct Python execution
```bash
cd SongComposer
source ../venv/bin/activate
python convert.py melody.txt output.mid
```

### Features
- Parses symbolic music format (Lyric: text, Note: pitch duration)
- Converts note names to MIDI numbers
- Handles various note durations (Quarter, Eighth, etc.)
- Configurable tempo (default: 96 BPM)
- Creates MIDI files with piano instrument


## 🎼 MIDIPlayer

### Overview
The MIDIPlayer system provides MIDI file playback, harmonization, and 3D audio visualization capabilities.

### Directory Structure
```
MIDIPlayer/
├── scripts/           # Python scripts
│   ├── playsong.py    # MIDI file playback
│   ├── harmonize.py   # Melody harmonization
│   └── visualizer.py  # 3D audio visualization
├── soundfonts/        # SoundFont files (.sf2)
├── midi_files/        # MIDI files (.mid)
└── audio_files/       # Audio files (.wav)
```

### Usage

#### MIDI Playback
```bash
cd MIDIPlayer/scripts
python playsong.py
```

#### Melody Harmonization
```bash
cd MIDIPlayer/scripts
python harmonize.py
```

#### 3D Audio Visualization
```bash
cd MIDIPlayer/scripts
python visualizer.py
```

### Features
- **MIDI Playback**: Uses FluidSynth for high-quality audio synthesis
- **Harmonization**: Automatically adds chord progressions to melodies
- **3D Visualization**: Real-time audio waveform visualization with PyQt6
- **Multiple SoundFonts**: Support for various instrument sounds

## 🛠️ Development

### Project Structure
```
SoundOfMusic/
├── LyricsGenerator/
│   ├── lyricgenerator.py    # Main lyric generation script
│   ├── lyrics.sh           # Shell script wrapper
│   ├── SwiftGPT.ipynb      # Jupyter notebook for model training
│   ├── model_checkpoint/   # Fine-tuned model files
│   └── readme.md
├── SongComposer/
│   ├── composer.py         # Main melody generation script
│   ├── composer.sh         # Shell script wrapper
│   ├── convert.py          # MIDI conversion script
│   ├── convert.sh          # MIDI conversion shell script
│   ├── composer.ipynb      # Original Jupyter notebook
│   └── readme.md
├── MIDIPlayer/
│   ├── scripts/            # Python scripts
│   ├── soundfonts/         # SoundFont files
│   ├── midi_files/         # MIDI files
│   ├── audio_files/        # Audio files
│   └── readme.md
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

### Key Dependencies
- **PyTorch**: Deep learning framework
- **Transformers**: Hugging Face model library
- **Music21**: Music analysis and processing
- **Librosa**: Audio processing
- **PyQt6**: GUI framework for visualization
- **Pygame**: Audio playback
- **MIDI libraries**: miditoolkit, mido, pretty_midi

### Model Files
The `model_checkpoint/` directory contains:
- `config.json`: Model configuration
- `model.safetensors`: Model weights
- `tokenizer.json`: Tokenizer configuration
- `vocab.json`: Vocabulary file
- Additional tokenizer files

## 🎵 Example Usage

### Complete Pipeline Example

#### 1. Generate Lyrics
```bash
# Generate lyrics starting with "In the morning light"
./LyricsGenerator/lyrics.sh "In the morning light"

# Output: Generated lyrics in Taylor Swift's style
```

#### 2. Compose Melody
```bash
# Generate melody based on a prompt
./SongComposer/composer.sh "Write a song about love"

# Output: Symbolic music format in melody.txt
```

#### 3. Convert to MIDI
```bash
# Convert symbolic music to MIDI
./SongComposer/convert.sh melody.txt output.mid

# Output: MIDI file ready for playback
```

#### 4. Play & Visualize
```bash
# Start the 3D audio visualizer
cd MIDIPlayer/scripts
python visualizer.py
```

### Individual Component Usage

#### Generate Lyrics Only
```bash
./LyricsGenerator/lyrics.sh "It was a dark and stormy night"
```

#### Compose Melody Only
```bash
./SongComposer/composer.sh "Write a song about love"
```

#### Convert MIDI Only
```bash
./SongComposer/convert.sh input.txt output.mid
```

#### Play MIDI with Visualization
```bash
cd MIDIPlayer/scripts
python visualizer.py
```

## 🔧 Troubleshooting

### Common Issues

1. **Python Version**: Ensure you're using Python 3.11+
   ```bash
   python3.11 --version
   ```

2. **Virtual Environment**: Always activate the virtual environment
   ```bash
   source venv/bin/activate
   ```

3. **Model Files**: Ensure `model_checkpoint/` contains all required files

4. **SoundFonts**: Verify SoundFont files are in `MIDIPlayer/soundfonts/`

5. **Dependencies**: Reinstall requirements if needed
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

### Performance Tips
- Use GPU acceleration if available (CUDA/MPS)
- Ensure sufficient RAM for model loading
- Use SSD storage for faster file access

## 📊 System Requirements

### Minimum Requirements
- **OS**: Any (tested on macOS 26 Tahoe)
- **Python**: 3.11+
- **RAM**: 20GB+
- **Storage**: 32GB free space

### Recommended Requirements
- **OS**: Any
- **Python**: 3.11+
- **RAM**: 18GB+
- **Storage**: 32GB free space
- **GPU**: Apple Silicon or NVIDIA GPU

## 📄 License

This project is for educational and research purposes. Please respect copyright laws when using generated content.


## 📞 Support & Contributing

I am unable to test the SongComposer component on my own device as I lack RAM. If you are able to test it and fix any bugs, please submit a PR.  

For issues and questions:
1. Check the troubleshooting section
2. Review existing issues
3. Create a new issue with detailed information

---

**Note**: This project is a demonstration of AI-powered music generation. Generated content should be used responsibly and in accordance with applicable laws and regulations.