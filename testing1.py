from customtkinter import *
import tkinter as tk
from tkinter import *
from os import listdir

# from PIL import Image

app = CTk()
app.geometry("500x400")
set_appearance_mode("system")
set_default_color_theme("green")

mainFrame = CTkFrame(master=app)
mainFrame.pack(expand=True)

btn = CTkButton(
    master=app,
    text="add alarm",
    corner_radius=32,
    # fg_color="#C850C0",
    # fg_color="transparent",
    hover_color="#4158D0",
    border_color="#FFCC70",
    border_width=2,
)
btn.place(relx=0.5, rely=0.0)

checkbox = CTkCheckBox(master=app, text="mon", corner_radius=50, border_width=2)
checkbox.pack()
switch = CTkSwitch(master=app, text="schedule")
switch.pack()

# time = CTKTimePicker(master=app)
# time.pack()


def get_music_files(foler_path):
    music_files = []
    for file in os.listdir(foler_path):
        if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".ogg"):
            music_files.append(file)
    return music_files


music_files = get_music_files("music")
print(music_files)

lists = CTkComboBox(app, values=music_files)
lists.pack()

app.mainloop()
