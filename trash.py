import tkinter as tk
import customtkinter


def create_frame(label_text, color):
    """Creates a new frame with the given label text and color."""
    frame = customtkinter.CTkFrame(bg=color)
    label = customtkinter.CTkLabel(frame, text=label_text)
    label.pack()
    return frame


def add_frame(frame):
    """Adds the given frame to the window."""
    frames.append(frame)
    frames[-1].pack()


# Create a list to store the frames.
frames = []

root = customtkinter.CTk()

# Create three frames with different colors.
frames.append(create_frame("Red Frame", "red"))
frames.append(create_frame("Green Frame", "green"))
frames.append(create_frame("Blue Frame", "blue"))

# Add the frames to the window.
for frame in frames:
    add_frame(frame)

# Start the mainloop.
root.mainloop()
