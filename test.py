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

        self.frame = ctk.CTkScrollableFrame(self.master)
        self.frame.pack(expand=True, fill="both", ipadx=200)

        self.frame1 = ctk.CTkFrame(self.frame, fg_color="grey")
        self.frame1.pack(pady=10, expand=True, fill="both")
        self.frame2 = ctk.CTkFrame(self.frame, fg_color="grey")
        self.frame2.pack(pady=10, expand=True, fill="both")
        self.frame3 = ctk.CTkFrame(self.frame, fg_color="grey")
        self.frame3.pack(pady=10, expand=True, fill="both")

    def resize(self, event, str):
        print(event.width, str)


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
