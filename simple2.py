import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import json
import pygame
import customtkinter as ctk


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x500")
        self.master.title("Bell System")

        self.resize_task = None
        self.previous_width = None
        self.column_length = 0

        # Load button names from JSON file
        self.button_names = self.load_button_names()

        # Taking all files names to a variable
        self.data1 = "Assets/json/data1.json"
        self.data2 = "Assets/json/data2.json"
        self.data3 = "Assets/json/data3.json"
        self.data4 = "Assets/json/data4.json"
        self.data5 = "Assets/json/data5.json"
        self.data6 = "Assets/json/data6.json"

        # Load all alarm data to its List
        self.alarms1 = self.load_alarms(self.data1)
        self.alarms2 = self.load_alarms(self.data2)
        self.alarms3 = self.load_alarms(self.data3)
        self.alarms4 = self.load_alarms(self.data4)
        self.alarms5 = self.load_alarms(self.data5)
        self.alarms6 = self.load_alarms(self.data6)

        # create all widgets
        self.create_widgets()

        # self.master.bind("<Configure>", self.resize)

    def resize(self, event, scrol_frame, alarm, data):
        current_width = self.master.winfo_width()

        if current_width != self.previous_width:
            self.previous_width = current_width

            if self.resize_task is not None:
                self.master.after_cancel(self.resize_task)

            self.resize_task = self.master.after(
                1,
                lambda: self.update_frames(scrol_frame, alarm, data),
            )

    def update_frames(self, scrol_frame, alarm, data):
        width = self.master.winfo_width()
        height = self.master.winfo_height()

        self.calculate_columns(width)
        self.display_alarms(scrol_frame, alarm, data)

    def calculate_columns(self, width):
        if 0 <= width < 400:
            self.column_length = 1
        elif 400 <= width < 800:
            self.column_length = 2
        elif 800 <= width < 1200:
            self.column_length = 3
        elif 1200 <= width < 1600:
            self.column_length = 4

    def create_widgets(self):
        # Main Frame
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill="both", expand=True)

        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.columnconfigure(3, weight=1)
        self.main_frame.columnconfigure(4, weight=1)

        # Left Frame
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0, sticky="swne")

        # Right Frame
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=1, columnspan=5, sticky="swen")

        # Initial frame in the right frame
        # self.default_frame = tk.Frame(self.right_frame)
        # self.default_frame.pack(fill="both", expand=True)
        # label = tk.Label(self.default_frame, text="Default Frame")
        # label.pack(pady=10)

        self.create_frames_for_right_frame(self.right_frame)
        self.create_buttons_for_left_frame(self.left_frame)

    def create_frames_for_right_frame(self, right_frame):
        self.frame1 = tk.Frame(right_frame)
        self.scrol_frame1 = tk.Frame(self.frame1, bg="red")
        self.scrol_frame1.update_idletasks()
        self.master.bind(
            "<Configure>",
            lambda event: self.resize(
                event, self.scrol_frame1, self.alarms1, self.data1
            ),
        )
        self.label1 = tk.Label(self.frame1, text=self.button_names["1"])

        self.frame2 = tk.Frame(right_frame)
        self.scrol_frame2 = tk.Frame(self.frame2)
        self.label2 = tk.Label(self.frame2, text=self.button_names["2"])

        self.frame3 = tk.Frame(right_frame)
        self.scrol_frame3 = tk.Frame(self.frame3)
        self.label3 = tk.Label(self.frame3, text=self.button_names["3"])

        self.frame4 = tk.Frame(right_frame)
        self.scrol_frame4 = tk.Frame(self.frame4)
        self.label4 = tk.Label(self.frame4, text=self.button_names["4"])

        self.frame5 = tk.Frame(right_frame)
        self.scrol_frame5 = tk.Frame(self.frame5)
        self.label5 = tk.Label(self.frame5, text=self.button_names["5"])

        self.frame6 = tk.Frame(right_frame)
        self.scrol_frame6 = tk.Frame(self.frame6)
        self.label6 = tk.Label(self.frame6, text=self.button_names["6"])

        self.display_alarms(self.scrol_frame1, self.alarms1, self.data1)
        self.display_alarms(self.scrol_frame2, self.alarms2, self.data2)
        self.display_alarms(self.scrol_frame3, self.alarms3, self.data3)
        self.display_alarms(self.scrol_frame4, self.alarms4, self.data4)
        self.display_alarms(self.scrol_frame5, self.alarms5, self.data5)
        self.display_alarms(self.scrol_frame6, self.alarms6, self.data6)

        def pack():
            self.frame1.pack()
            self.frame2.pack()
            self.frame3.pack()
            self.frame4.pack()
            self.frame5.pack()
            self.frame6.pack()
            self.label1.pack()
            self.label2.pack()
            self.label3.pack()
            self.label4.pack()
            self.label5.pack()
            self.label6.pack()
            self.scrol_frame1.pack(fill=tk.BOTH, expand=True)
            self.scrol_frame2.pack(fill=tk.BOTH, expand=True)
            self.scrol_frame3.pack(fill=tk.BOTH, expand=True)
            self.scrol_frame4.pack(fill=tk.BOTH, expand=True)
            self.scrol_frame5.pack(fill=tk.BOTH, expand=True)
            self.scrol_frame6.pack(fill=tk.BOTH, expand=True)
            self.frame1.forget()
            self.frame2.forget()
            self.frame3.forget()
            self.frame4.forget()
            self.frame5.forget()
            self.frame6.forget()
            self.frame1.pack(fill=tk.BOTH, expand=True)

        pack()
        self.create_buttons_for_right_frame_frames()

    def create_buttons_for_right_frame_frames(self):
        buttonframe = tk.Frame(self.frame1)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = tk.Button(
            buttonframe,
            text="+",
            width=10,
            bg="blue",
            # height=50,
            # font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame1, self.alarms1, self.data1
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = tk.Frame(self.frame2)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = tk.Button(
            buttonframe,
            text="+",
            width=10,
            bg="blue",
            # height=50,
            # font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame2, self.alarms2, self.data2
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = tk.Frame(self.frame3)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = tk.Button(
            buttonframe,
            text="+",
            width=10,
            bg="blue",
            # height=50,
            # font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame3, self.alarms3, self.data3
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = tk.Frame(self.frame4)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = tk.Button(
            buttonframe,
            text="+",
            width=10,
            bg="blue",
            # height=50,
            # font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame4, self.alarms4, self.data4
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = tk.Frame(self.frame5)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = tk.Button(
            buttonframe,
            text="+",
            width=10,
            bg="blue",
            # height=50,
            # font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame5, self.alarms5, self.data5
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = tk.Frame(self.frame6)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = tk.Button(
            buttonframe,
            text="+",
            width=10,
            bg="blue",
            # height=50,
            # font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame6, self.alarms6, self.data6
            ),
        )
        btn.pack(ipadx=5, ipady=5)

    def create_buttons_for_left_frame(self, left_frame):
        button1 = tk.Button(
            self.left_frame,
            text=self.button_names["1"],
            font=("Times", 15),
            command=lambda: self.open_frame(self.frame1),
        )
        button1.pack()
        button1.bind(
            "<Double-Button-1>",
            lambda event, btn=button1, idx=1, label=self.label1: self.rename_button(
                btn, idx, label
            ),
        ),

        button2 = tk.Button(
            self.left_frame,
            text=self.button_names["2"],
            font=("Times", 15),
            command=lambda: self.open_frame(self.frame2),
        )
        button2.pack()
        button2.bind(
            "<Double-Button-1>",
            lambda event, btn=button2, idx=2, label=self.label2: self.rename_button(
                btn, idx, label
            ),
        ),
        button3 = tk.Button(
            self.left_frame,
            text=self.button_names["3"],
            font=("Times", 15),
            command=lambda: self.open_frame(self.frame3),
        )
        button3.pack()
        button3.bind(
            "<Double-Button-1>",
            lambda event, btn=button3, idx=3, label=self.label3: self.rename_button(
                btn, idx, label
            ),
        ),
        button4 = tk.Button(
            self.left_frame,
            text=self.button_names["4"],
            font=("Times", 15),
            command=lambda: self.open_frame(self.frame4),
        )
        button4.pack()
        button4.bind(
            "<Double-Button-1>",
            lambda event, btn=button4, idx=4, label=self.label4: self.rename_button(
                btn, idx, label
            ),
        ),
        button5 = tk.Button(
            self.left_frame,
            text=self.button_names["5"],
            font=("Times", 15),
            command=lambda: self.open_frame(self.frame5),
        )
        button5.pack()
        button5.bind(
            "<Double-Button-1>",
            lambda event, btn=button5, idx=5, label=self.label5: self.rename_button(
                btn, idx, label
            ),
        ),
        button6 = tk.Button(
            self.left_frame,
            text=self.button_names["6"],
            font=("Times", 15),
            command=lambda: self.open_frame(self.frame6),
        )
        button6.pack()
        button6.bind(
            "<Double-Button-1>",
            lambda event, btn=button6, idx=6, label=self.label6: self.rename_button(
                btn, idx, label
            ),
        ),

    def open_add_alarm_window(self, scrol_frame, alarm, data):
        # Sub-window for adding alarm
        add_alarm_window = tk.Toplevel(self.master)
        add_alarm_window.title("Add Alarm")

        # Widgets in the sub-window
        tk.Label(add_alarm_window, text="Add Alarm").grid(row=0, column=0, columnspan=2)

        hour_label = tk.Label(add_alarm_window, text="Hour:")
        hour_label.grid(row=1, column=0, pady=5)
        hour_var = tk.StringVar(add_alarm_window)
        hr = time.strftime("%I")
        hour_var.set(hr)
        hour_entry = ttk.Combobox(
            add_alarm_window,
            textvariable=hour_var,
            values=[str(i).zfill(2) for i in range(1, 13)],
        )
        hour_entry.grid(row=1, column=1, pady=5)

        minute_label = tk.Label(add_alarm_window, text="Minute:")
        minute_label.grid(row=2, column=0, pady=5)
        minute_var = tk.StringVar(add_alarm_window)
        min = time.strftime("%M")
        minute_var.set(min)
        minute_entry = ttk.Combobox(
            add_alarm_window,
            textvariable=minute_var,
            values=[str(i).zfill(2) for i in range(60)],
        )
        minute_entry.grid(row=2, column=1, pady=5)

        am_pm_label = tk.Label(add_alarm_window, text="AM/PM:")
        am_pm_label.grid(row=3, column=0, pady=5)
        am_pm_var = tk.StringVar(add_alarm_window)
        ampm = time.strftime("%p")
        am_pm_var.set(ampm)
        am_pm_entry = ttk.Combobox(
            add_alarm_window, textvariable=am_pm_var, values=["AM", "PM"]
        )
        am_pm_entry.grid(row=3, column=1, pady=5)

        text_label = tk.Label(add_alarm_window, text="Text:")
        text_label.grid(row=4, column=0, pady=5)
        text_entry = tk.Entry(add_alarm_window)
        text_entry.grid(row=4, column=1, pady=5)

        days_label = tk.Label(add_alarm_window, text="Days:")
        days_label.grid(row=5, column=0, pady=5)
        days_var = {}
        for i, day in enumerate(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]):
            days_var[day] = tk.BooleanVar(add_alarm_window)
            tk.Checkbutton(add_alarm_window, text=day, variable=days_var[day]).grid(
                row=5, column=i + 1, pady=5
            )

        cancel_button = tk.Button(
            add_alarm_window, text="Cancel", command=add_alarm_window.destroy
        )
        cancel_button.grid(row=6, column=0, columnspan=2, pady=10)

        save_button = tk.Button(
            add_alarm_window,
            text="Save",
            command=lambda: self.save_alarm(
                hour_var.get(),
                minute_var.get(),
                am_pm_var.get(),
                text_entry.get(),
                days_var,
                add_alarm_window,
                scrol_frame,
                alarm,
                data,
            ),
        )
        save_button.grid(row=7, column=0, columnspan=2, pady=10)

    def save_alarm(
        self,
        hour,
        minute,
        am_pm,
        text,
        days_var,
        add_alarm_window,
        scrol_frame,
        alarm,
        data,
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

        alarm.append(alarm_data)
        self.save_data(alarm, data)

        add_alarm_window.destroy()
        self.display_alarms(scrol_frame, alarm, data)

    def display_alarms(self, scrol_frame, alarm, data):
        row = 0
        col = 0
        # Clear existing widgets in the display frame
        for widget in scrol_frame.winfo_children():
            widget.destroy()

        # List to store switch variables
        switch_vars = []

        # Display alarms in the display frame
        for i, alar in enumerate(alarm):
            alarm_frame = tk.Frame(scrol_frame, bg="green")
            alarm_frame.grid(row=row, column=col, pady=5, padx=5, sticky="ew")

            tk.Label(alarm_frame, text=f"Time: {alar['time']}").grid(
                row=0, column=0, sticky="w"
            )
            tk.Label(alarm_frame, text=f"Text: {alar['text']}").grid(
                row=1, column=0, sticky="w"
            )
            tk.Label(alarm_frame, text=f"Days: {', '.join(alar['days'])}").grid(
                row=2, column=0, sticky="w"
            )

            switch_var = tk.BooleanVar(value=alar["switch_state"])
            # store variable in list
            switch_vars.append(switch_var)

            switch_widget = ctk.CTkSwitch(
                alarm_frame,
                variable=switch_var,
                command=lambda alar=alar, sv=switch_var, alarm=alarm, data=data: self.toggle_switch(
                    alar, sv, alarm, data
                ),
            )
            switch_widget.grid(row=0, column=1, rowspan=3, padx=10)

            delete_button = tk.Button(
                alarm_frame,
                text="Delete",
                command=lambda a=alar, scrol_frame=scrol_frame, alarm=alarm, data=data: self.delete_alarm(
                    a, scrol_frame, alarm, data
                ),
            )
            delete_button.grid(row=3, column=0, pady=5)

            # update row and col
            col = col + 1
            if col == self.column_length + 1:
                col = 0
                row += 1

    def toggle_switch(self, alar, switch_var, alarm, data):
        alar["switch_state"] = switch_var.get()
        self.save_data(alarm, data)

    def delete_alarm(self, alar, scrol_frame, alarm, data):
        alarm.remove(alar)
        self.save_data(alarm, data)
        self.display_alarms(scrol_frame, alarm, data)

    def open_frame(self, frame):
        # Unpack all frames in the right frame
        # for child in self.right_frame.winfo_children():
        #     child.pack_forget()
        self.frame1.forget()
        self.frame2.forget()
        self.frame3.forget()
        self.frame4.forget()
        self.frame5.forget()
        self.frame6.forget()
        # print(i)
        frame.pack(fill=tk.BOTH, expand=True)

    def save_button_names(self):
        # Save the button names to a JSON file
        with open("Assets/json/button_names.json", "w") as file:
            json.dump(self.button_names, file, indent=2)

    def load_button_names(self):
        # Load button names from a JSON file
        try:
            with open("Assets/json/button_names.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def load_alarms(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self, alarm, data):
        with open(data, "w") as file:
            json.dump(alarm, file, indent=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = BellSystemApp(root)

    root.mainloop()
