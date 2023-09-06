import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Define a custom font for the button text
button_font = (
    "Helvetica",
    16,
)  # Change 'Helvetica' to your desired font family and 16 to the desired font size

# Create a style for the button
button_style = ttk.Style()

# Configure the custom style to use the custom font
button_style.configure("Custom.TButton", font=button_font)

button_style.configure("MyCustomButton", font=button_font)
add_button = ttk.Button(
    frame,
    text="Add Alarm Card",
    style="MyCustomButton",
)
# Create a frame
frame = ttk.Frame(root)
frame.pack()

# Create a button with the custom style
add_button = ttk.Button(
    frame,
    text="Add Alarm Card",
    style="MyCustomButton",
)
add_button.grid(row=1, column=0, padx=5, pady=10, sticky="w")

root.mainloop()
