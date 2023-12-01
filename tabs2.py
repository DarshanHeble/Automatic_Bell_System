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

        self.data1 = "data1.json"
        self.data2 = "data2.json"
        self.data3 = "data3.json"
        self.data4 = "data4.json"
        self.data5 = "data5.json"
        self.data6 = "data6.json"

        # load data
        # self.load_data()
        self.alarms1 = self.load_alarms(self.data1)
        self.alarms2 = self.load_alarms(self.data2)
        self.alarms3 = self.load_alarms(self.data3)
        self.alarms4 = self.load_alarms(self.data4)
        self.alarms5 = self.load_alarms(self.data5)
        self.alarms6 = self.load_alarms(self.data6)

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
        # for i in range(1, 7):
        #     # Check if button name exists in the loaded data
        #     if str(i) in self.button_names:
        #         button_name = self.button_names[str(i)]
        #     else:
        #         button_name = f"Button {i}"

        #     button_frame = ctk.CTkFrame(self.left_frame)
        #     button_frame.grid(row=i, column=0, pady=5, sticky="ew")

        #     button = ctk.CTkButton(button_frame, text=button_name)
        #     button.pack(expand=True, fill="both")
        #     button.bind(
        #         "<Double-Button-1>",
        #         lambda event, btn=button, idx=i: self.rename_button(btn, idx),
        #     )
        #     frame = f"frame{i}"
        #     button.bind(
        #         "<Button-1>",
        #         lambda event, btn_name=button_name, idx=i: self.open_frame(
        #             idx, btn_name
        #         ),
        #     )

        # Initial frame in the right frame
        # self.default_frame = ctk.CTkFrame(self.right_frame)
        # self.default_frame.pack(fill="both", expand=True)
        # label = ctk.CTkLabel(self.default_frame, text="Default Frame")
        # label.pack(pady=10)

        self.create_frames_for_right_frame(self.right_frame)
        self.create_buttons_for_left_frame(self.left_frame)

    def create_frames_for_right_frame(self, right_frame):
        self.frame1 = ctk.CTkFrame(right_frame, fg_color="orange")
        self.scrol_frame1 = ctk.CTkScrollableFrame(self.frame1, corner_radius=0)
        self.label1 = ctk.CTkLabel(self.frame1, text=self.button_names["1"])

        self.frame2 = ctk.CTkFrame(right_frame, fg_color="magenta")
        self.scrol_frame2 = ctk.CTkScrollableFrame(self.frame2, corner_radius=0)
        self.label2 = ctk.CTkLabel(self.frame2, text=self.button_names["2"])

        self.frame3 = ctk.CTkFrame(right_frame, fg_color="royalblue")
        self.scrol_frame3 = ctk.CTkScrollableFrame(self.frame3, corner_radius=0)
        self.label3 = ctk.CTkLabel(self.frame3, text=self.button_names["3"])

        self.frame4 = ctk.CTkFrame(right_frame, fg_color="purple")
        self.scrol_frame4 = ctk.CTkScrollableFrame(self.frame4, corner_radius=0)
        self.label4 = ctk.CTkLabel(self.frame4, text=self.button_names["4"])

        self.frame5 = ctk.CTkFrame(right_frame, fg_color="crimson")
        self.scrol_frame5 = ctk.CTkScrollableFrame(self.frame5, corner_radius=0)
        self.label5 = ctk.CTkLabel(self.frame5, text=self.button_names["5"])

        self.frame6 = ctk.CTkFrame(right_frame, fg_color="teal")
        self.scrol_frame6 = ctk.CTkScrollableFrame(self.frame6, corner_radius=0)
        self.label6 = ctk.CTkLabel(self.frame6, text=self.button_names["6"])

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
            self.scrol_frame1.pack(expand=True, fill="both")
            self.scrol_frame2.pack(expand=True, fill="both")
            self.scrol_frame3.pack(expand=True, fill="both")
            self.scrol_frame4.pack(expand=True, fill="both")
            self.scrol_frame5.pack(expand=True, fill="both")
            self.scrol_frame6.pack(expand=True, fill="both")
            self.frame1.forget()
            self.frame2.forget()
            self.frame3.forget()
            self.frame4.forget()
            self.frame5.forget()
            self.frame6.forget()
            self.frame1.pack(expand=True, fill="both")

        pack()
        self.create_buttons_for_right_frame_frames()

    def create_buttons_for_right_frame_frames(self):
        buttonframe = ctk.CTkFrame(self.frame1, corner_radius=0)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = ctk.CTkButton(
            buttonframe,
            text="+",
            width=50,
            height=50,
            font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame1, self.alarms1, self.data1
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = ctk.CTkFrame(self.frame2, corner_radius=0)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = ctk.CTkButton(
            buttonframe,
            text="+",
            width=50,
            height=50,
            font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame2, self.alarms2, self.data2
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = ctk.CTkFrame(self.frame3, corner_radius=0)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = ctk.CTkButton(
            buttonframe,
            text="+",
            width=50,
            height=50,
            font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame3, self.alarms3, self.data3
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = ctk.CTkFrame(self.frame4, corner_radius=0)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = ctk.CTkButton(
            buttonframe,
            text="+",
            width=50,
            height=50,
            font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame4, self.alarms4, self.data4
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = ctk.CTkFrame(self.frame5, corner_radius=0)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = ctk.CTkButton(
            buttonframe,
            text="+",
            width=50,
            height=50,
            font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame5, self.alarms5, self.data5
            ),
        )
        btn.pack(ipadx=5, ipady=5)
        buttonframe = ctk.CTkFrame(self.frame6, corner_radius=0)
        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = ctk.CTkButton(
            buttonframe,
            text="+",
            width=50,
            height=50,
            font=("arial", 40),
            command=lambda: self.open_add_alarm_window(
                self.scrol_frame6, self.alarms6, self.data6
            ),
        )
        btn.pack(ipadx=5, ipady=5)

    def create_buttons_for_left_frame(self, left_frame):
        button1 = ctk.CTkButton(
            self.left_frame,
            text=self.button_names["1"],
            text_color=("black", "white"),
            fg_color="transparent",
            hover_color="orange",
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

        button2 = ctk.CTkButton(
            self.left_frame,
            text=self.button_names["2"],
            text_color=("black", "white"),
            fg_color="transparent",
            hover_color="magenta",
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
        button3 = ctk.CTkButton(
            self.left_frame,
            text=self.button_names["3"],
            text_color=("black", "white"),
            fg_color="transparent",
            hover_color="royalblue",
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
        button4 = ctk.CTkButton(
            self.left_frame,
            text=self.button_names["4"],
            text_color=("black", "white"),
            fg_color="transparent",
            hover_color="teal",
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
        button5 = ctk.CTkButton(
            self.left_frame,
            text=self.button_names["5"],
            text_color=("black", "white"),
            fg_color="transparent",
            hover_color="crimson",
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
        button6 = ctk.CTkButton(
            self.left_frame,
            text=self.button_names["6"],
            text_color=("black", "white"),
            fg_color="transparent",
            hover_color="teal",
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

        alarm.append(alarm_data)
        self.save_data(alarm, data)

        add_alarm_window.destroy()
        self.display_alarms(scrol_frame, alarm, data)

    def display_alarms(self, scrol_frame, alarm, data):
        # Clear existing widgets in the display frame
        for widget in scrol_frame.winfo_children():
            widget.destroy()

        # Display alarms in the display frame
        for i, alar in enumerate(alarm):
            alarm_frame = ctk.CTkFrame(scrol_frame)
            alarm_frame.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

            ctk.CTkLabel(alarm_frame, text=f"Time: {alar['time']}").grid(
                row=0, column=0, sticky="w"
            )
            ctk.CTkLabel(alarm_frame, text=f"Text: {alar['text']}").grid(
                row=1, column=0, sticky="w"
            )
            ctk.CTkLabel(alarm_frame, text=f"Days: {', '.join(alar['days'])}").grid(
                row=2, column=0, sticky="w"
            )

            switch_var = ctk.BooleanVar(value=alar["switch_state"])
            switch_widget = ctk.CTkSwitch(
                alarm_frame,
                variable=switch_var,
                command=lambda: self.toggle_switch(alar, switch_var, alarm, data),
            )
            switch_widget.grid(row=0, column=1, rowspan=3, padx=10)

            delete_button = ctk.CTkButton(
                alarm_frame,
                text="Delete",
                command=lambda a=alar, scrol_frame=scrol_frame, alarm=alarm, data=data: self.delete_alarm(
                    a, scrol_frame, alarm, data
                ),
            )
            delete_button.grid(row=3, column=0, pady=5)

            edit_button = ctk.CTkButton(
                alarm_frame, text="Edit", command=lambda a=alar: self.edit_alarm(a)
            )
            edit_button.grid(row=3, column=1, pady=5)

    def rename_button(self, button, button_index, label):
        current_text = button.cget("text")

        # new_name = simpledialog.askstring(
        #     "Rename Button", "Enter new name:", initialvalue=current_text
        # )
        new_name = ctk.CTkInputDialog(
            title="Rename Button", text="Enter new name:"
        ).get_input()
        if new_name:
            button.configure(text=new_name)
            label.configure(text=new_name)
            # Update the button name in the loaded data
            self.button_names[str(button_index)] = new_name
            # Save the updated data to the JSON file
            self.save_button_names()

    def toggle_switch(self, alar, switch_var, alarm, data):
        alar["switch_state"] = switch_var.get()
        self.save_data(alarm, data)

    def delete_alarm(self, alar, scrol_frame, alarm, data):
        alarm.remove(alar)
        self.save_data(alarm, data)
        self.display_alarms(scrol_frame, alarm, data)

    def edit_alarm(self, alarm):
        edit_alarm_window = tk.Toplevel(self.master)
        edit_alarm_window.title("Edit Alarm")

        # Widgets in the sub-window
        ttk.Label(edit_alarm_window, text="Edit Alarm").grid(
            row=0, column=0, columnspan=2
        )

        hour_label = ttk.Label(edit_alarm_window, text="Hour:")
        hour_label.grid(row=1, column=0, pady=5)
        hour_var = tk.StringVar(edit_alarm_window)
        hour_var.set(alarm["time"].split(":")[0])
        hour_entry = ttk.Combobox(
            edit_alarm_window,
            textvariable=hour_var,
            values=[str(i).zfill(2) for i in range(1, 13)],
        )
        hour_entry.grid(row=1, column=1, pady=5)

        minute_label = ttk.Label(edit_alarm_window, text="Minute:")
        minute_label.grid(row=2, column=0, pady=5)
        minute_var = tk.StringVar(edit_alarm_window)
        minute_var.set(alarm["time"].split(":")[1].split()[0])
        minute_entry = ttk.Combobox(
            edit_alarm_window,
            textvariable=minute_var,
            values=[str(i).zfill(2) for i in range(60)],
        )
        minute_entry.grid(row=2, column=1, pady=5)

        am_pm_label = ttk.Label(edit_alarm_window, text="AM/PM:")
        am_pm_label.grid(row=3, column=0, pady=5)
        am_pm_var = tk.StringVar(edit_alarm_window)
        am_pm_var.set(alarm["time"].split()[1])
        am_pm_entry = ttk.Combobox(
            edit_alarm_window, textvariable=am_pm_var, values=["AM", "PM"]
        )
        am_pm_entry.grid(row=3, column=1, pady=5)

        text_label = ttk.Label(edit_alarm_window, text="Text:")
        text_label.grid(row=4, column=0, pady=5)
        text_var = tk.StringVar(edit_alarm_window)
        text_var.set(alarm["text"])
        text_entry = ttk.Entry(edit_alarm_window, textvariable=text_var)
        text_entry.grid(row=4, column=1, pady=5)

        days_label = ttk.Label(edit_alarm_window, text="Days:")
        days_label.grid(row=5, column=0, pady=5)
        days_var = {}
        for i, day in enumerate(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]):
            days_var[day] = tk.BooleanVar(
                edit_alarm_window, value=(day in alarm["days"])
            )
            ttk.Checkbutton(edit_alarm_window, text=day, variable=days_var[day]).grid(
                row=5, column=i + 1, pady=5
            )

        cancel_button = ttk.Button(
            edit_alarm_window, text="Cancel", command=edit_alarm_window.destroy
        )
        cancel_button.grid(row=6, column=0, columnspan=2, pady=10)

        save_button = ttk.Button(
            edit_alarm_window,
            text="Save",
            command=lambda: self.save_edited_alarm(
                hour_var.get(),
                minute_var.get(),
                am_pm_var.get(),
                text_var.get(),
                days_var,
                alarm,
                edit_alarm_window,
            ),
        )
        save_button.grid(row=6, column=0, columnspan=2, pady=10)

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
        frame.pack(expand=True, fill="both")

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
            pass

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
    root = ctk.CTk()
    app = BellSystemApp(root)
    root.mainloop()
