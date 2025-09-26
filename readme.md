# SoundOfMusic 🎵

A complete AI-powered music generation pipeline that creates pop songs in Taylor Swift's style. The system generates lyrics using a fine-tuned GPT-2 model, creates melodies with a Transformer model, and provides real-time audio visualization.

## 🎯 Project Overview

This project consists of two main components:
- **LyricsGenerator**: AI-powered lyric generation using a fine-tuned GPT-2 model
- **MIDIPlayer**: MIDI playback, harmonization, and 3D audio visualization

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- macOS (tested on macOS 25.0.0)
- Homebrew (for Python installation)

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

### Generate Lyrics
```bash
# Generate lyrics starting with "In the morning light"
./LyricsGenerator/lyrics.sh "In the morning light"

# Output will be generated lyrics in Taylor Swift's style
```

### Play MIDI with Visualization
```bash
# Start the 3D audio visualizer
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
- **RAM**: 8GB+
- **Storage**: 2GB free space

### Recommended Requirements
- **OS**: Any
- **Python**: 3.11+
- **RAM**: 16GB+
- **Storage**: 5GB free space
- **GPU**: Apple Silicon or NVIDIA GPU

## 📄 License

This project is for educational and research purposes. Please respect copyright laws when using generated content.


## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review existing issues
3. Create a new issue with detailed information

---

**Note**: This project is a demonstration of AI-powered music generation. Generated content should be used responsibly and in accordance with applicable laws and regulations.