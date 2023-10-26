import tkinter as tk


def create_frame():
    """Creates a new frame."""
    frame = tk.Frame()
    label = tk.Label(frame, text="This is a frame.")
    label.pack()
    return frame


def handle_button_click():
    """Adds a frame to the window."""
    frames.append(create_frame())
    frames[-1].pack()


# Create a list to store the frames.
frames = []

root = tk.Tk()

# Create the button.
button = tk.Button(root, text="Add Frame", command=handle_button_click)
button.pack()

# Add the frames to the window.
for frame in frames:
    frame.pack()

# Start the mainloop.
root.mainloop()
