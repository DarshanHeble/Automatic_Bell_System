import tkinter as tk


def on_resize(event):
    # Get the current window size
    window_width = event.width

    # Determine the number of columns based on the window width
    columns = 3 if window_width >= 600 else 2

    # Clear existing grid configuration
    for i in range(rows):
        parent_frame.grid_rowconfigure(i, weight=0)
    for j in range(columns):
        parent_frame.grid_columnconfigure(j, weight=0)

    # Configure the grid columns
    for j in range(columns):
        parent_frame.grid_columnconfigure(j, weight=1)

    # Update the global variable
    global columns
    columns = columns


# Create the main window
root = tk.Tk()
root.geometry("500x400")  # Initial window size

# Parent Frame
parent_frame = tk.Frame(root, bg="lightgray")
parent_frame.pack(expand=True, fill=tk.BOTH)


# Function to add child frames automatically
def add_child_frame(color):
    frame = tk.Frame(parent_frame, width=100, height=100, bg=color)
    frame.grid(sticky="nsew")
    return frame


# Add child frames
frames = [
    add_child_frame("red"),
    add_child_frame("green"),
    add_child_frame("blue"),
    add_child_frame("yellow"),
]

# Configure grid weights for resizing
rows = 2
columns = 2
for i in range(rows):
    parent_frame.grid_rowconfigure(i, weight=1)
for j in range(columns):
    parent_frame.grid_columnconfigure(j, weight=1)

# Bind the window resize event
root.bind("<Configure>", on_resize)

root.mainloop()
