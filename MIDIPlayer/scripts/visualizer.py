import numpy as np
import librosa  # loading audio
from opensimplex import OpenSimplex
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui
from PyQt6.QtWidgets import QApplication
import sys
import soundfile as sf
import os
import threading
import pygame

class Terrain(object):
    def __init__(self, audio_file_path: str):
        self.audio_file_path = audio_file_path
        self.audio_data, self.sr = librosa.load(audio_file_path, sr=44100, mono=True)
        self.frame_idx = 0


        # Initialize Qt application if not already initialized
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()
        
        self.window = gl.GLViewWidget()
        self.window.setWindowTitle('Swiftualizer - Press Q to quit')
        self.window.setGeometry(0, 110, 1920, 1080)
        self.window.setCameraPosition(distance=30, elevation=12)
        self.window.show()
        
        # Enable keyboard events
        self.window.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.window.keyPressEvent = self.keyPressEvent

        self.nsteps = 1.0  # Balanced resolution for smooth, beautiful terrain
        self.offset = 0
        self.ypoints = np.arange(-20, 20 + self.nsteps, self.nsteps)
        self.xpoints = np.arange(-20, 20 + self.nsteps, self.nsteps)
        self.nfaces = len(self.ypoints)

        self.CHUNK = len(self.xpoints) * len(self.ypoints)
        self.noise = OpenSimplex(seed=324)  # Perlin Noise object
        verts, faces, colors = self.mesh()  # create mesh

        self.main_mesh = gl.GLMeshItem(
            faces=faces,
            vertexes=verts,
            faceColor=colors,
            drawEdges=True,
            smooth=False,
        )
        self.main_mesh.setGLOptions('additive')
        self.window.addItem(self.main_mesh)

        self.total_chunks = len(self.audio_data) // self.CHUNK
        if len(self.audio_data) % self.CHUNK != 0:
            self.total_chunks += 1  # Add an extra chunk for the remainder
        self.audio_data = np.pad(self.audio_data, (0, self.CHUNK * self.total_chunks))
        
        with sf.SoundFile(audio_file_path) as f:
            self.audio_duration = len(f) / f.samplerate
            print(f"Correct duration: {self.audio_duration} seconds")

        self.chunk_duration = (self.audio_duration * 1000) / self.total_chunks  # in milliseconds
        
        # Initialize pygame for audio playback
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        self.audio_started = False
        
    def get_audio_chunk(self):
        start = self.frame_idx
        end = start + self.CHUNK
        chungus = self.audio_data[start:end]  # extract the chunk
        self.frame_idx += self.CHUNK
        return chungus * 15.0  # Moderate scaling for visible but beautiful changes

    def mesh(self, offset: float = 0.0, wf_data=None):
        if wf_data is None:
            wf_data = np.ones((len(self.xpoints), len(self.ypoints)))  # Default flat terrain
        else:
            wf_data = wf_data.reshape((len(self.xpoints), len(self.ypoints)))

        faces, colors = [], []
        vertices = np.array([
            [x, y, wf_data[xid][yid] * self.noise.noise2(x=xid / 4 + offset, y=yid / 4 + offset)] \
            for xid, x in enumerate(self.xpoints) for yid, y in enumerate(self.ypoints)
        ], dtype=np.float32)

        for yid in range(self.nfaces - 1):
            yoff = yid * self.nfaces
            for xid in range(self.nfaces - 1):
                faces.append([
                    xid + yoff,
                    xid + yoff + self.nfaces,
                    xid + yoff + self.nfaces + 1,
                ])
                faces.append([
                    xid + yoff,
                    xid + yoff + 1,
                    xid + yoff + self.nfaces + 1,
                ])
                # Beautiful gradient colors based on position
                colors.append([xid / self.nfaces, 1 - xid / self.nfaces, yid / self.nfaces, 0.7])
                colors.append([xid / self.nfaces, 1 - xid / self.nfaces, yid / self.nfaces, 0.8])

        faces = np.array(faces, dtype=np.uint32)
        colors = np.array(colors, dtype=np.float32)

        return vertices, faces, colors

    def update_mesh(self):
        if self.frame_idx >= len(self.audio_data):
            print("Audio finished. Stopping animation.")
            self.timer.stop()  # Stop the animation
            QtCore.QTimer.singleShot(1000, self.window.close)  # Close the window after 1 sec
            return

        wf_data = self.get_audio_chunk()
        verts, faces, colors = self.mesh(offset=self.offset, wf_data=wf_data)
        self.main_mesh.setMeshData(vertexes=verts, faces=faces, faceColors=colors)
        self.offset -= 0.08  # Smooth, elegant animation

    def keyPressEvent(self, event):
        """Handle keyboard events"""
        if event.key() == QtCore.Qt.Key.Key_Q:
            print("Quitting visualizer...")
            self.quit_visualizer()
        else:
            # Call the default key press event
            gl.GLViewWidget.keyPressEvent(self.window, event)
    
    def quit_visualizer(self):
        """Clean up and quit the visualizer"""
        if hasattr(self, 'timer'):
            self.timer.stop()
        if hasattr(self, 'audio_started') and self.audio_started:
            pygame.mixer.music.stop()
            print("🎵 Audio playback stopped")
        self.app.quit()
    
    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            self.app.exec()  # PyQT API changed (exec_ became exec)

    def start_audio_playback(self):
        """Start audio playback in a separate thread"""
        try:
            pygame.mixer.music.load(self.audio_file_path)
            pygame.mixer.music.play()
            print("🎵 Audio playback started!")
            self.audio_started = True
        except Exception as e:
            print(f"Error starting audio: {e}")

    def animate(self):
        # Start audio playback first
        self.start_audio_playback()
        
        # Start the timer with the calculated chunk duration
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_mesh)
        self.timer.start(int(self.chunk_duration))
        print("Song duration: ", self.audio_duration)
        print("Chunk duration: ", self.chunk_duration)
        print("Checking for synchronization:", self.chunk_duration * self.total_chunks)
        self.start()

if __name__ == '__main__':
    # Use the converted MIDI file
    audio_file_path = "../audio_files/ybwm.wav"
    if not os.path.exists(audio_file_path):
        print(f"Audio file {audio_file_path} not found!")
        sys.exit(1)
    terrain = Terrain(audio_file_path)
    terrain.animate()