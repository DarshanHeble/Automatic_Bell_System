import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tkinter import ttk
from customtkinter import *
import threading
import time
import json
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")

        # Load button names from JSON file
        self.button_names = self.load_button_names()

        # load data
        # self.load_data()
        self.alarms1 = self.load_alarms("data1.json")
        self.alarms2 = self.load_alarms("data2.json")
        self.alarms3 = self.load_alarms("data3.json")
        self.alarms4 = self.load_alarms("data4.json")
        self.alarms5 = self.load_alarms("data5.json")
        self.alarms6 = self.load_alarms("data6.json")

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
                "<Button-1>",
                lambda event, btn_name=button_name, idx=i: self.show_frame(
                    idx, btn_name
                ),
            )

        # Initial frame in the right frame
        self.default_frame = ctk.CTkFrame(self.right_frame)
        self.default_frame.pack(fill="both", expand=True)
        label = ctk.CTkLabel(self.default_frame, text="Default Frame")
        label.pack(pady=10)

    def open_add_alarm_window(self):
        # Sub-window for adding alarm
        add_alarm_window = ctk.CTkToplevel(self.master)
        add_alarm_window.title("Add Alarm")

        # Widgets in the sub-window
        ctk.CTkLabel(add_alarm_window, text="Add Alarm").grid(
            row=0, column=0, columnspan=2
        )

        hour_label = ctk.CTkLabel(add_alarm_window, text="Hour:")
        hour_label.grid(row=1, column=0, pady=5)
        hour_var = ctk.StringVar(add_alarm_window)
        hr = time.strftime("%I")
        hour_var.set(hr)
        hour_entry = ttk.Combobox(
            add_alarm_window,
            textvariable=hour_var,
            font=("arial", 15),
            values=[str(i).zfill(2) for i in range(1, 13)],
        )
        hour_entry.grid(row=1, column=1, pady=5, padx=5)

        minute_label = ctk.CTkLabel(add_alarm_window, text="Minute:")
        minute_label.grid(row=2, column=0, pady=5)
        minute_var = ctk.StringVar(add_alarm_window)
        min = time.strftime("%M")
        minute_var.set(min)
        minute_entry = ttk.Combobox(
            add_alarm_window,
            font=("arial", 15),
            textvariable=minute_var,
            values=[str(i).zfill(2) for i in range(60)],
        )
        minute_entry.grid(row=2, column=1, pady=5)

        am_pm_label = ctk.CTkLabel(add_alarm_window, text="AM/PM:")
        am_pm_label.grid(row=3, column=0, pady=5)
        am_pm_var = ctk.StringVar(add_alarm_window)
        ampm = time.strftime("%p")
        am_pm_var.set(ampm)
        am_pm_entry = ttk.Combobox(
            add_alarm_window,
            textvariable=am_pm_var,
            values=["AM", "PM"],
            font=("arial", 15),
        )
        am_pm_entry.grid(row=3, column=1, pady=5)

        text_label = ctk.CTkLabel(add_alarm_window, text="Text:")
        text_label.grid(row=4, column=0, pady=5)
        text_entry = ctk.CTkEntry(add_alarm_window)
        text_entry.grid(row=4, column=1, pady=5)

        days_label = ctk.CTkLabel(add_alarm_window, text="Days:")
        days_label.grid(row=5, column=0, pady=5)
        days_var = {}
        for i, day in enumerate(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]):
            days_var[day] = ctk.BooleanVar(add_alarm_window)
            ctk.CTkCheckBox(add_alarm_window, text=day, variable=days_var[day]).grid(
                row=5, column=i + 1, pady=5
            )

        cancel_button = ctk.CTkButton(
            add_alarm_window, text="Cancel", command=add_alarm_window.destroy
        )
        cancel_button.grid(row=6, column=0, columnspan=2, pady=10)

        save_button = ctk.CTkButton(
            add_alarm_window,
            text="Save",
            command=lambda: self.save_alarm(
                hour_var.get(),
                minute_var.get(),
                am_pm_var.get(),
                text_entry.get(),
                days_var,
                add_alarm_window,
            ),
        )
        save_button.grid(row=6, column=0, columnspan=2, pady=10)

    def save_alarm(self, hour, minute, am_pm, text, days_var, add_alarm_window):
        alarm_time = f"{hour}:{minute} {am_pm}"
        days_selected = [day for day, var in days_var.items() if var.get()]

        if not days_selected:
            CTkMessagebox(
                title="warning", message="Something went wrong!!!", icon="cancel"
            )
            return

        alarm_data = {
            "time": alarm_time,
            "text": text,
            "days": days_selected,
            "switch_state": True,  # default to True
        }

        self.alarms.append(alarm_data)
        self.save_data()

        add_alarm_window.destroy()
        self.display_alarms()

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
        frame = ctk.CTkFrame(self.right_frame)
        frame.pack(fill="both", expand=True, padx=20)
        label = ctk.CTkLabel(frame, text=f"{frame_name} - {button_name}")
        label.pack(pady=10)

        # Button for each frame in the specific frame
        frame_button = ctk.CTkButton(
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
            with open("data.json", "r") as file:
                self.alarms = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.alarms = []

    def load_alarms(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)
    root.mainloop()
