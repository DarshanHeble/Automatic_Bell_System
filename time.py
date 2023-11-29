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

        # Load button names from JSON file
        self.button_names = self.load_button_names()

        # load data
        self.load_data()

        # create all widgets
        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        self.main_frame = ctk.CTkFrame(self.master)
        self.main_frame.pack(fill="both", expand=True)

        # Left Frame
        self.left_frame = ctk.CTkFrame(self.main_frame, width=200)
        self.left_frame.pack(side=LEFT, fill="both")

        # Right Frame
        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.pack(side=RIGHT, fill="both", expand=True)

        # Create 6 buttons in the left frame
        for i in range(1, 7):
            # Check if button name exists in the loaded data
            if str(i) in self.button_names:
                button_name = self.button_names[str(i)]
            else:
                button_name = f"Button {i}"

            button_frame = ctk.CTkFrame(self.left_frame)
            button_frame.grid(row=i, column=0, pady=5, sticky="ew")

            button = ctk.CTkButton(button_frame, text=button_name)
            button.pack(expand=True, fill="both")
            button.bind(
                "<Double-Button-1>",
                lambda event, btn=button, idx=i: self.rename_button(btn, idx),
            )
            button.bind(
                "<Button-1>", lambda event, idx=i: self.show_frame(idx, button_name)
            )

        # Initial frame in the right frame
        self.default_frame = ctk.CTkFrame(self.right_frame)
        self.default_frame.pack(fill="both", expand=True)
        label = ctk.CTkLabel(self.default_frame, text="Default Frame")
        label.pack(pady=10)

    def rename_button(self, button, button_index):
        current_text = button.cget("text")

        # new_name = simpledialog.askstring(
        #     "Rename Button", "Enter new name:", initialvalue=current_text
        # )
        new_name = ctk.CTkInputDialog(
            title="Rename Button", text="Enter new name:"
        ).get_input()
        if new_name:
            button.configure(text=new_name)
            # Update the button name in the loaded data
            self.button_names[str(button_index)] = new_name
            # Save the updated data to the JSON file
            self.save_button_names()

    def show_frame(self, idx, button_name):
        # Unpack all frames in the right frame
        for child in self.right_frame.winfo_children():
            child.pack_forget()

        # Create or show the specific frame based on the button clicked
        frame_name = f"Frame {idx}"
        frame = tk.Frame(self.right_frame, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=20)
        label = tk.Label(frame, text=f"{frame_name} - {button_name}")
        label.pack(pady=10)

        # Button for each frame in the specific frame
        frame_button = tk.Button(
            frame,
            text="Add Alarm",
            # command=lambda: self.show_frame(idx, button_name),
            command=self.open_add_alarm_window,
        )
        frame_button.pack()

    def save_button_names(self):
        # Save the button names to a JSON file
        with open("button_names.json", "w") as file:
            json.dump(self.button_names, file, indent=2)

    def load_button_names(self):
        # Load button names from a JSON file
        try:
            with open("button_names.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def load_data(self):
        try:
            with open("data2.json", "r") as file:
                self.alarms = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.alarms = []


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)
    root.mainloop()
    # def on_button_click(self, event):
    #     # Show some error message
    #     CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
