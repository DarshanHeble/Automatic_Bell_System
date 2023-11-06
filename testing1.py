import tkinter as tk
from tkinter import ttk


def add_label():
    label_text = label_entry.get()
    if label_text:
        create_label(label_text)
        create_frame()


def create_label(label_text):
    label = ttk.Label(left_frame, text=label_text)
    label.bind("<Button-1>", lambda event, text=label_text: display_frame(label_text))
    label.grid(sticky="w", padx=5, pady=5)


def create_frame():
    frame = ttk.Frame(right_frame)
    # frame.configure()  # Set background color
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_remove()
    label_frame_dict[id(frame)] = frame
    label_display_dict[id(frame)] = False


def display_frame(frame_id):
    for frame_id, frame in label_frame_dict.items():
        if label_display_dict[frame_id]:
            frame.grid_remove()
            label_display_dict[frame_id] = False

    selected_frame = label_frame_dict[frame_id]
    selected_frame.grid()
    label_display_dict[frame_id] = True


root = tk.Tk()
root.title("Dynamic Tabs Example")

left_frame = ttk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

right_frame = ttk.Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

label_entry = ttk.Entry(left_frame)
label_entry.grid(row=0, column=0, padx=5, pady=5, sticky="w")

add_button = ttk.Button(left_frame, text="Add Label", command=add_label)
add_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

label_frame_dict = {}
label_display_dict = {}

# Example initial labels and frames
create_label("Label 1")
create_frame()

create_label("Label 2")
create_frame()

root.mainloop()
