import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")

style = ttk.Style()
style.configure("Large.Tbutton", font=("arial", 20))

add_bell_button = ttk.Button(root, text="button", style="Large.Tbutton")
add_bell_button.pack(anchor="ne")

root.mainloop()
