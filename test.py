import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tkinter import ttk
from customtkinter import *
import threading
import time
import json

import pygame


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(expand=True, fill="both", pady=10, padx=20)
        self.frame.bind("<Configure>", lambda event: self.resize(event, "1"))

        self.frame1 = ctk.CTkFrame(self.master)
        self.frame1.pack(expand=True, fill="both", pady=10, padx=20)
        self.frame1.bind("<Configure>", lambda event: self.resize(event, "2"))
        self.frame.forget()

    def resize(self, event, str):
        print(event.width, str)


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
