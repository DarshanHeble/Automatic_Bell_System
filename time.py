import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from customtkinter import *
import threading
import time
import json
import os
import pygame


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")

        self.create_button()

    def create_button(self):
        button = ctk.CTkButton(self.master, text="Open Message Box")
        button.pack()
        button.bind("<Button-1>", self.on_button_click)

    def on_button_click(self, event):
        # Show some error message
        CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)
    root.mainloop()
