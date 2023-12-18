import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tkinter import ttk
from customtkinter import *


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")

        self.frame = ctk.CTkFrame(self.master, width=1000, fg_color="blue")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

    def resize(self, event, str):
        print(event.width, str)


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
