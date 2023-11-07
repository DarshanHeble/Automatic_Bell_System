import customtkinter as ct
from tkinter import ttk
import time

root = ct.CTk()
root.geometry("200x200")

# current_time = time.localtime()
# print(current_time)

curr_time = time.strftime("%d-%m-%Y %I:%M:%S %p")
print(curr_time)


spin = ttk.Spinbox(root)
spin.pack()


button = ct.CTkButton(root)
button.pack()
# button.bind("<Button-1>", lambda event, l=label: hello(l))
# root.mainloop()
