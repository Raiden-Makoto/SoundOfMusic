import fluidsynth
import time

fs = fluidsynth.Synth()
fs.start(driver="coreaudio")  # "dsound" on Windows
sfid = fs.sfload("FluidR3_GM.sf2")
fs.program_select(0, sfid, 0, 0)

# Play MIDI file using FluidSynth command line
import subprocess
subprocess.run(["fluidsynth", "-i", "FluidR3_GM.sf2", "ybwm.mid"])