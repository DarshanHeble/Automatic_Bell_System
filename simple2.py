import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
import json


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
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left Frame
        self.left_frame = tk.Frame(self.main_frame, width=200, bg="lightgray")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        # Right Frame
        self.right_frame = tk.Frame(self.main_frame, bg="white")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create 6 buttons in the left frame
        for i in range(1, 7):
            # Check if button name exists in the loaded data
            if str(i) in self.button_names:
                button_name = self.button_names[str(i)]
            else:
                button_name = f"Button {i}"

            button_frame = tk.Frame(self.left_frame, bg="lightgray")
            button_frame.grid(row=i, column=0, pady=5, sticky="ew")

            button = tk.Button(button_frame, text=button_name)
            button.pack(expand=True, fill=tk.BOTH)
            button.bind(
                "<Double-Button-1>",
                lambda event, btn=button, idx=i: self.rename_button(btn, idx),
            )
            button.bind(
                "<Button-1>", lambda event, idx=i: self.show_frame(idx, button_name)
            )

        # Initial frame in the right frame
        self.default_frame = tk.Frame(self.right_frame, bg="white")
        self.default_frame.pack(fill=tk.BOTH, expand=True)
        label = tk.Label(self.default_frame, text="Default Frame")
        label.pack(pady=10)

    def rename_button(self, button, button_index):
        current_text = button.cget("text")
        new_name = simpledialog.askstring(
            "Rename Button", "Enter new name:", initialvalue=current_text
        )
        if new_name:
            button.config(text=new_name)
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

    def open_add_alarm_window(self):
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
            ),
        )
        save_button.grid(row=6, column=0, columnspan=2, pady=10)

    def save_alarm(self, hour, minute, am_pm, text, days_var, add_alarm_window):
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

        self.alarms.append(alarm_data)
        # self.save_data()

        add_alarm_window.destroy()
        self.display_alarms()

    def display_alarms(self):
        # Clear existing widgets in the display frame
        for widget in self.display_alarms_frame.winfo_children():
            widget.destroy()

        # Display alarms in the display frame
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

    def save_data(self):
        with open("data2.json", "w") as file:
            json.dump(self.alarms, file, indent=2)

    def load_data(self):
        try:
            with open("data2.json", "r") as file:
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
