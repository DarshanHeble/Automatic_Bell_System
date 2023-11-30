import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from customtkinter import CTkSwitch
import threading
import time
import json
import pygame


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")

        self.load_data()
        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left Frame
        self.left_frame = tk.Frame(self.main_frame, width=200, bg="lightgray")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create buttons and associate them with dynamic frames
        button_labels = [
            "Button 1",
            "Button 2",
            "Button 3",
            "Button 4",
            "Button 5",
            "Button 6",
        ]
        self.frames = []
        for label in button_labels:
            frame = tk.Frame(self.main_frame, bg="white")
            self.frames.append(frame)

            button = tk.Button(
                self.left_frame, text=label, command=lambda f=frame: self.show_frame(f)
            )
            button.pack(fill=tk.X, pady=10)

        # Right Frame (default to the first frame)
        self.current_frame = self.frames[0]
        self.current_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Add Alarm Button
        add_alarm_button = tk.Button(
            self.current_frame, text="Add Alarm", command=self.add_alarm
        )
        add_alarm_button.pack(pady=10)

        # Display Alarms Frame
        self.display_alarms_frame = tk.Frame(self.current_frame)
        self.display_alarms_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Start background thread
        self.check_alarm_thread = threading.Thread(target=self.check_alarm)
        self.check_alarm_thread.daemon = True
        self.check_alarm_thread.start()

        # Load and display existing alarms for the current frame
        self.display_alarms()

    def show_frame(self, frame):
        # Hide the current frame
        self.current_frame.pack_forget()
        # Show the selected frame
        frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.current_frame = frame
        # Load and display existing alarms for the current frame
        self.display_alarms()

    def add_alarm(self):
        # Sub-window for adding alarm
        add_alarm_window = tk.Toplevel(self.master)
        add_alarm_window.title("Add Alarm")

        # Widgets in the sub-window
        ttk.Label(add_alarm_window, text="Add Alarm").grid(
            row=0, column=0, columnspan=2
        )

        hour_label = ttk.Label(add_alarm_window, text="Hour:")
        hour_label.grid(row=1, column=0, pady=5)
        hour_var = tk.StringVar(add_alarm_window)
        hour_var.set("00")
        hour_entry = ttk.Combobox(
            add_alarm_window,
            textvariable=hour_var,
            values=[str(i).zfill(2) for i in range(1, 13)],
        )
        hour_entry.grid(row=1, column=1, pady=5)

        minute_label = ttk.Label(add_alarm_window, text="Minute:")
        minute_label.grid(row=2, column=0, pady=5)
        minute_var = tk.StringVar(add_alarm_window)
        minute_var.set("00")
        minute_entry = ttk.Combobox(
            add_alarm_window,
            textvariable=minute_var,
            values=[str(i).zfill(2) for i in range(60)],
        )
        minute_entry.grid(row=2, column=1, pady=5)

        am_pm_label = ttk.Label(add_alarm_window, text="AM/PM:")
        am_pm_label.grid(row=3, column=0, pady=5)
        am_pm_var = tk.StringVar(add_alarm_window)
        am_pm_var.set("AM")
        am_pm_entry = ttk.Combobox(
            add_alarm_window, textvariable=am_pm_var, values=["AM", "PM"]
        )
        am_pm_entry.grid(row=3, column=1, pady=5)

        text_label = ttk.Label(add_alarm_window, text="Text:")
        text_label.grid(row=4, column=0, pady=5)
        text_entry = ttk.Entry(add_alarm_window)
        text_entry.grid(row=4, column=1, pady=5)

        days_label = ttk.Label(add_alarm_window, text="Days:")
        days_label.grid(row=5, column=0, pady=5)
        days_var = {}
        for i, day in enumerate(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]):
            days_var[day] = tk.BooleanVar(add_alarm_window)
            ttk.Checkbutton(add_alarm_window, text=day, variable=days_var[day]).grid(
                row=5, column=i + 1, pady=5
            )

        cancel_button = ttk.Button(
            add_alarm_window, text="Cancel", command=add_alarm_window.destroy
        )
        cancel_button.grid(row=6, column=0, columnspan=2, pady=10)

        save_button = ttk.Button(
            add_alarm_window,
            text="Save",
            command=lambda: self.save_alarm(
                hour_var.get(),
                minute_var.get(),
                am_pm_var.get(),
                text_entry.get(),
                days_var,
                add_alarm_window,
                self.current_frame,
            ),
        )
        save_button.grid(row=6, column=0, columnspan=2, pady=10)

    def save_alarm(
        self, hour, minute, am_pm, text, days_var, add_alarm_window, current_frame
    ):
        alarm_time = f"{hour}:{minute} {am_pm}"
        days_selected = [day for day, var in days_var.items() if var.get()]

        if not days_selected:
            messagebox.showwarning("Error", "Select at least one day for the alarm.")
            return

        alarm_data = {
            "time": alarm_time,
            "text": text,
            "days": days_selected,
            "switch_state": True,  # default to True
        }

        # Save data to the main list
        self.alarms.append(alarm_data)
        self.save_data()

        add_alarm_window.destroy()
        self.display_alarms()

        # Save data to the specific frame's list
        current_frame_data = getattr(current_frame, "alarm_data", [])
        current_frame_data.append(alarm_data)
        current_frame.alarm_data = current_frame_data

        self.save_data()

        add_alarm_window.destroy()
        self.display_alarms()

    def display_alarms(self):
        # Clear existing widgets in the display frame
        for widget in self.display_alarms_frame.winfo_children():
            widget.destroy()

        # Display alarms in the display frame for the current frame
        current_frame_data = getattr(self.current_frame, "alarm_data", [])
        for i, alarm in enumerate(self.alarms):
            alarm_frame = tk.Frame(self.display_alarms_frame, bd=2, relief=tk.GROOVE)
            alarm_frame.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

            ttk.Label(alarm_frame, text=f"Time: {alarm['time']}").grid(
                row=0, column=0, sticky="w"
            )
            ttk.Label(alarm_frame, text=f"Text: {alarm['text']}").grid(
                row=1, column=0, sticky="w"
            )
            ttk.Label(alarm_frame, text=f"Days: {', '.join(alarm['days'])}").grid(
                row=2, column=0, sticky="w"
            )

            switch_var = tk.BooleanVar(value=alarm["switch_state"])
            switch_widget = CTkSwitch(
                alarm_frame,
                variable=switch_var,
                command=lambda: self.toggle_switch(alarm, switch_var),
            )
            switch_widget.grid(row=0, column=1, rowspan=3, padx=10)

            delete_button = ttk.Button(
                alarm_frame, text="Delete", command=lambda a=alarm: self.delete_alarm(a)
            )
            delete_button.grid(row=3, column=0, pady=5)

            edit_button = ttk.Button(
                alarm_frame, text="Edit", command=lambda a=alarm: self.edit_alarm(a)
            )
            edit_button.grid(row=3, column=1, pady=5)

    def check_alarm(self):
        current_time = time.strftime("%I:%M %p")
        current_day = time.strftime("%a")

        # Initialize pygame outside the loop (call it once)
        pygame.mixer.init()

        # Load the sound file once
        sound = pygame.mixer.Sound("School-Period-bell.mp3")

        # print(f"Current Time: {current_time}, Current Day: {current_day}")

        for alarm in self.alarms:
            # print(f"Checking alarm: {alarm}")
            if (
                alarm["time"] == current_time
                and current_day in alarm["days"]
                and alarm["switch_state"]
            ):
                # print(f"Playing sound for alarm: {alarm}")
                sound.play()
                time.sleep(120)

        # Schedule the check_alarm function to run again after 1000 milliseconds (1 second)
        self.master.after(1000, self.check_alarm)

    def delete_alarm(self, alarm):
        self.alarms.remove(alarm)
        self.save_data()
        self.display_alarms()

    def load_data(self):
        try:
            with open("data.json", "r") as file:
                self.alarms = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.alarms = []

    def save_data(self):
        with open("data.json", "w") as file:
            json.dump(self.alarms, file, indent=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = BellSystemApp(root)
    root.mainloop()
