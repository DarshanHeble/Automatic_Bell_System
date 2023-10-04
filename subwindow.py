import tkinter as tk
from tkinter import ttk

subwindow = tk.Tk()

subwindow.title("subwindow")
subwindow.iconbitmap("musify.ico")

labelframe = ttk.Frame(subwindow)
time_label = ttk.Label(labelframe, text="Time (HH:MM):", font=("Helvetica", 15))
time_label.grid(row=0, column=0, padx=10, pady=5)
time_entry = ttk.Entry(labelframe, width=15, font=("Helvetica", 15))
time_entry.grid(row=0, column=1, padx=10, pady=5)
labelframe.pack(padx=20, pady=20)

daysframe = ttk.Frame(subwindow)
days_label = ttk.Label(daysframe, text="Select Days:", font=("Helvetica", 15))
days_label.grid(row=1, column=0, padx=10, pady=5)

days_var = [tk.BooleanVar() for _ in range(7)]
days_checkboxes = [
    ttk.Checkbutton(daysframe, text=day, variable=var)
    for day, var in zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], days_var)
]
for i, checkbox in enumerate(days_checkboxes):
    checkbox.grid(row=1, column=i + 1)
daysframe.pack()

songframe = ttk.Frame(subwindow)
song_label = ttk.Label(songframe, text="Select Song:", font=("Helvetica", 15))
song_label.grid(row=3, column=0, padx=10, pady=5)
song_entry = ttk.Entry(songframe, width=20, font=("Helvetica", 15))
song_entry.grid(row=3, column=1, padx=10, pady=5)
song_select_button = ttk.Button(songframe, text="Select")
# , command=select_song
song_select_button.grid(row=3, column=2, padx=10, pady=5)
songframe.pack()

subwindow.mainloop()
