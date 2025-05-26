
# Audio Handling Imports
import librosa
import simpleaudio as sa

# Data Processing Imports
import numpy as np
import pandas as pd

# GUI Generation Imports
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk



path = "C:/Users/Ant PC/Downloads/mono-chill.wav"
audiopath = str

def loadmusic():
    global audiopath
    audiopath = filedialog.askopenfilename(initialdir="/", title="Select music file to visualize")
    label.config(text=audiopath)

    y, sr = librosa.load(audiopath)
    D = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

    ax.clear()

    pd.Series(y).plot(ax=ax)
    canvas.draw()
    print(audiopath)
    print(str(audiopath))


def playmusic():
    wave_obj = sa.WaveObject.from_wave_file(audiopath)
    play_obj = wave_obj.play()

def exitwindow():
    sa.stop_all()
    window.destroy()



# Window setup
screen_x = 1200
screen_y = 720

window = Tk()
window.title("Music Visualizer")
window.config(padx=30, pady=30, bg="white")
# window.geometry(f"{screen_x}x{screen_y}")

# Setup Plot of audio data
fig, ax = plt.subplots(figsize=(10,5))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.TOP)


toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor="w", fill= tk.X)


# Buttons and Labels

label = tk.Label(window, text="Music Visualizer", fg="white", bg="black")
label.pack(fill="both", expand=True, pady=10)

upld_btn = tk.Button(window, text="UPLOAD MUSIC FILE",command=loadmusic)
upld_btn.pack(fill="both", expand=True, pady=10)

play_btn = tk.Button(window, text="PLAY MUSIC FILE",command=playmusic)
play_btn.pack(fill="both", expand=True, pady=10)

exit_btn = tk.Button(window, text="EXIT",command=exitwindow)
exit_btn.pack(fill="both", expand=True, pady=10)


window.mainloop()
