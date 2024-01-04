import tkinter as tk


def toggle_fullscreen(window):
    if window.attributes("-fullscreen"):
        window.attributes("-fullscreen", False)
    else:
        window.attributes("-fullscreen", True)


def check_fullscreen(window):
    return window.attributes("-fullscreen")


def print_hi(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    if window_width == screen_width and window_height == screen_height:
        print("Hi")


# Create the main window
root = tk.Tk()
root.title("Fullscreen Example")

# Create a button to toggle fullscreen
toggle_button = tk.Button(
    root, text="Toggle Fullscreen", command=lambda: toggle_fullscreen(root)
)
toggle_button.pack(pady=20)

# Create a label to display fullscreen status
status_label = tk.Label(root, text="")
status_label.pack()


# Function to update the status label and print "Hi" when maximized
def update_status(event):
    status_label.config(text="Fullscreen: " + str(check_fullscreen(root)))
    print_hi(root)


# Set up an event to update the status label when the window is resized
root.bind("<Configure>", update_status)

# Run the Tkinter main loop
root.mainloop()
