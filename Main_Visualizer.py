
# Audio Handling Imports
import librosa
import simpleaudio as sa

# Data Processing Imports
import numpy as np
import pandas as pd

# GUI Generation Imports
from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk



path = "mono-chill.wav"


def loadmusic():
    ax.clear()
    y, sr = librosa.load(path)
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    pd.Series(y).plot(lw=1, title="Raw Audio Data")
    canvas.draw()


# Window setup
screen_x = 1200
screen_y = 720

window = Tk()
window.title("Music Visualizer")
window.config(padx=50, pady=50, bg="white")
# window.geometry(f"{screen_x}x{screen_y}")

# Setup Plot of audio data
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor="w", fill= tk.X)


# Buttons and Labels

label = tk.Label(window, text="Music Visualizer", fg="white", bg="black")
label.pack(fill="both", expand=True, pady=10)

upld_btn = tk.Button(window, text="UPLOAD MUSIC FILE",command=loadmusic)
upld_btn.pack(fill="both", expand=True, pady=10)

exit_btn = tk.Button(window, text="EXIT",command=window.destroy)
exit_btn.pack(fill="both", expand=True, pady=10)

window.mainloop()