import customtkinter as ctk
from tkinter import simpledialog
import pygame
from threading import Thread
import os
import pickle
import time

# Initialize pygame mixer
pygame.mixer.init()

root = ctk.CTk()
root.geometry("900x600")

# File path for storing data
DATA_FILE = "tabs_data.pkl"

frame0_data = []
frame1_data = []
frame2_data = []
frame3_data = []
frame4_data = []
frame5_data = []
frame6_data = []

hour = ctk.StringVar()
minute = ctk.StringVar()
am_pm = ctk.StringVar()


name = ctk.StringVar(value="bell")
sunday = ctk.StringVar(value="off")
monday = ctk.StringVar(value="on")
tuesday = ctk.StringVar(value="on")
wednesday = ctk.StringVar(value="on")
thursday = ctk.StringVar(value="on")
friday = ctk.StringVar(value="on")
saturday = ctk.StringVar(value="on")
# schedule_switch = ctk.StringVar(value="on")

# music_file
music_files = []
curr_music = ctk.StringVar()

button_list = [
    "button1",
    "button2",
    "button3",
    "button4",
    "button5",
    "button6",
    "button7",
]
counter = 0
labels_dict = {}
labels_list = []


def start_threading(
    hr,
    mi,
    ampm,
    name,
    sun,
    mon,
    tue,
    wed,
    thu,
    fri,
    sat,
    current_music,
    card_item,
):
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # getting current time and days
    curr_hr = time.strftime("%I")
    curr_min = time.strftime("%M")
    curr_am_pm = time.strftime("%p")

    # Get the current time as a struct_time object
    current_time = time.localtime()

    # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
    current_day_in_number = current_time.tm_wday

    # current_day
    current_day = days_of_week[current_day_in_number]
    print(current_day)
    print(sun)

    # proper music file path
    music_file_path = f"music/{current_music}"

    # checking the time until the specified time occures
    while (
        hr != curr_hr
        and mi != curr_min
        and ampm != curr_am_pm
        and (
            current_day != sun
            or current_day != mon
            or current_day != tue
            or current_day != wed
            or current_day != thu
            or current_day != fri
            or current_day != sat
        )
        and card_item["schedule_on_off"] != "on"
    ):
        curr_hr = time.strftime("%I")
        curr_min = time.strftime("%M")
        curr_am_pm = time.strftime("%p")

        current_day = days_of_week[current_day_in_number]

    # when time occures plat the music file
    if (
        hr == curr_hr
        and mi == curr_min
        and ampm == curr_am_pm
        and card_item["schedule_on_off"] == "on"
        and (
            current_day == sun
            or current_day == mon
            or current_day == tue
            or current_day == wed
            or current_day == thu
            or current_day == fri
            or current_day == sat
        )
    ):
        pygame.mixer.music.load(f"music/{current_music}")
        # time.sleep(5)
        pygame.mixer.music.play()


def open_window(f, framelist, curr_hr, curr_min, curr_am_pm):
    window = ctk.CTkFrame(root)
    window.place(relx=0.5, rely=0.5, anchor="center")
    card = ctk.CTkFrame(window)
    card.pack(padx=1005, pady=1005, ipadx=30)

    heading = ctk.CTkLabel(
        card,
        text="Add New Bell",
        # width=300,
        font=("helvitica", 30, "bold"),
        # bg_color="yellow",
    )
    heading.pack(pady=20)

    def time():
        option_frame = ctk.CTkFrame(card, fg_color="transparent")
        option_frame.pack(pady=(0, 30))
        # =============================hours===============================
        hour_options = (
            "00",
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        )

        global hour
        hour.set(curr_hr)
        hrs = ctk.CTkOptionMenu(
            option_frame,
            values=hour_options,
            variable=hour,
            width=100,
            height=50,
            font=("helvitica", 25),
            dropdown_font=("helvitica", 20),
        )
        hrs.grid(row=0, column=0, padx=10)
        # =============================hours===============================
        # =============================hours===============================
        minute_options = (
            "00",
            "05",
            "10",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "25",
            "30",
            "35",
            "40",
            "45",
            "50",
            "55",
            "60",
        )
        global minute
        minute.set(curr_min)
        min = ctk.CTkOptionMenu(
            option_frame,
            values=minute_options,
            variable=minute,
            width=100,
            height=50,
            font=("helvitica", 25),
            dropdown_font=("helvitica", 20),
        )
        min.grid(row=0, column=1, padx=10)
        # =============================hours===============================
        # =============================hours===============================
        am_pm_options = ("PM", "AM")
        global am_pm
        am_pm.set(curr_am_pm)
        ampm = ctk.CTkOptionMenu(
            option_frame,
            values=am_pm_options,
            variable=am_pm,
            width=100,
            height=50,
            font=("helvitica", 25),
            dropdown_font=("helvitica", 20),
        )
        ampm.grid(row=0, column=2, padx=10)

    def name():
        name_frame = ctk.CTkFrame(card, fg_color="transparent")
        name_frame.pack(pady=(0, 30))
        name_label = ctk.CTkLabel(name_frame, text="Label : ", font=("helvitica", 25))
        name_label.pack(padx=5, side="left")
        global name
        name_entry = ctk.CTkEntry(
            name_frame, font=("helvitica", 25), width=200, textvariable=name
        )
        name_entry.pack(padx=5)

    def weeks():
        weekd_days_frame = ctk.CTkFrame(card, fg_color="transparent")
        weekd_days_frame.pack(pady=(0, 30))
        global sunday, monday, tuesday, wednesday, thursday, friday, saturday
        sun_cb = ctk.CTkCheckBox(
            weekd_days_frame,
            text="sun",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=sunday,
            checkbox_height=30,
            checkbox_width=30,
        )

        mon_cb = ctk.CTkCheckBox(
            weekd_days_frame,
            text="mon",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=monday,
            checkbox_height=30,
            checkbox_width=30,
        )
        tue_cb = ctk.CTkCheckBox(
            weekd_days_frame,
            text="tue",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=tuesday,
            checkbox_height=30,
            checkbox_width=30,
        )
        wed_cb = ctk.CTkCheckBox(
            weekd_days_frame,
            text="wed",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=wednesday,
            checkbox_height=30,
            checkbox_width=30,
        )
        thu_cb = ctk.CTkCheckBox(
            weekd_days_frame,
            text="thu",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=thursday,
            checkbox_height=30,
            checkbox_width=30,
        )
        fri_cb = ctk.CTkCheckBox(
            weekd_days_frame,
            text="fri",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=friday,
            checkbox_height=30,
            checkbox_width=30,
        )
        sat_cb = ctk.CTkCheckBox(
            weekd_days_frame,
            text="sat",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=saturday,
            checkbox_height=30,
            checkbox_width=30,
        )
        sun_cb.grid(row=0, column=1, sticky="w")
        mon_cb.grid(row=0, column=2, sticky="w", padx=10)
        tue_cb.grid(row=0, column=3, sticky="w")
        wed_cb.grid(row=0, column=4, sticky="w", padx=10)
        thu_cb.grid(row=0, column=5, sticky="w")
        fri_cb.grid(row=0, column=6, sticky="w", padx=10)
        sat_cb.grid(row=0, column=7, sticky="w")

    def music():
        def get_music_files(folder_path):
            global music_files
            for file in os.listdir(folder_path):
                if (
                    file.endswith(".mp3")
                    or file.endswith(".wav")
                    or file.endswith(".ogg")
                    or file.endswith(".aiff")
                    or file.endswith(".flac")
                    or file.endswith(".acc")
                    or file.endswith(".wma")
                ):
                    music_files.append(file)
            return music_files

        music_frame = ctk.CTkFrame(card, fg_color="transparent")
        music_frame.pack(pady=(0, 30))
        music_label = ctk.CTkLabel(
            music_frame, text="Select Music : ", font=("helvitica", 23)
        )
        music_label.pack(side="left", padx=5)
        music_files = get_music_files("music")
        curr_music.set(music_files[0])
        select_bell = ctk.CTkOptionMenu(
            music_frame, values=music_files, variable=curr_music, font=("helvitica", 16)
        )
        select_bell.pack(
            side="left",
        )

    def schedule():
        global schedule_switch
        switch_frame = ctk.CTkFrame(card, fg_color="transparent")
        schedule = ctk.CTkSwitch(
            switch_frame,
            text="Schedule",
            # variable=schedule_switch,
            onvalue="on",
            offvalue="off",
            switch_height=25,
            switch_width=50,
        )
        schedule.pack(pady=(0, 30))
        switch_frame.pack()
        print("schedule_switch", schedule_switch.get())

    def save_data_and_display_card(window, hour, minute, am_pm, name):
        card_item = {}
        # time
        hr = hour.get()
        mi = minute.get()
        # print(mi)
        ampm = am_pm.get()
        # name
        name = name.get()
        # weeks
        sun = sunday.get()
        mon = monday.get()
        tue = tuesday.get()
        wed = wednesday.get()
        thu = thursday.get()
        fri = friday.get()
        sat = saturday.get()
        # music
        current_music = curr_music.get()
        card_item.update(
            {
                "hour": hr,
                "minute": mi,
                "am_pm": ampm,
                "name": name,
                "sunday": sun,
                "monday": mon,
                "tuesday": tue,
                "wednesday": wed,
                "thursday": thu,
                "friday": fri,
                "saturday": sat,
                "schedule_on_off": "on",
                "music": current_music,
            }
        )

        # print(card_item)
        framelist.append(card_item)
        # print(framelist)
        print("\n")
        # print("data saved")

        display_card(
            framelist,
            hr,
            mi,
            ampm,
            name,
            sun,
            mon,
            tue,
            wed,
            thu,
            fri,
            sat,
            current_music,
            card_item,
        )

    def display_card(
        framelist,
        hr,
        mi,
        ampm,
        name,
        sun,
        mon,
        tue,
        wed,
        thu,
        fri,
        sat,
        current_music,
        card_item,
    ):
        week_days = []

        def display_weeks():
            if sun == "on":
                week_days.append("sun")
            if mon == "on":
                week_days.append("mon")
            if tue == "on":
                week_days.append("tue")
            if wed == "on":
                week_days.append("wed")
            if thu == "on":
                week_days.append("thu")
            if fri == "on":
                week_days.append("fri")
            if sat == "on":
                week_days.append("sat")

        display_weeks()

        def switcher(switch):
            # print(switch.get())
            diction = framelist[0]
            data = switch.get()

            diction["schedule_on_off"] = data
            # print(card_item)
            # print(data)

        frame = ctk.CTkFrame(f)
        innerFrame = ctk.CTkFrame(frame)
        timeFrame = ctk.CTkFrame(innerFrame, fg_color="transparent")
        time = ctk.CTkLabel(
            timeFrame, text=f"{hr} : {mi} {ampm}", font=("helvitica", 60, "bold")
        )
        name_label = ctk.CTkLabel(
            innerFrame, text=name, font=("helvitica", 30, "normal")
        )
        week = ctk.CTkLabel(
            innerFrame, text=" ".join(week_days), font=("helvitica", 30, "normal")
        )
        music_label = ctk.CTkLabel(innerFrame, text=current_music)
        schedule_Switch = ctk.CTkSwitch(
            innerFrame,
            text="",
            onvalue="on",
            offvalue="off",
            switch_height=25,
            switch_width=50,
            command=lambda: switcher(
                schedule_Switch,
            ),
        )
        schedule_Switch.select()
        delete_frame = ctk.CTkButton(innerFrame, text="Delete", command=frame.destroy)
        # print(schedule_label.cget())

        timeFrame.pack()
        time.pack()
        schedule_Switch.pack()
        name_label.pack()
        week.pack()
        music_label.pack()
        delete_frame.pack()
        window.destroy()
        innerFrame.pack(fill="x", expand=True, padx=20, pady=20)
        frame.pack(fill="x", expand=True, padx=20, pady=20)

        # threading.Thread(target=start_threading).start()
        # start_threading()
        # threading.Thread.join()
        new_thread = Thread(
            target=start_threading,
            args=(
                hr,
                mi,
                ampm,
                name,
                sun,
                mon,
                tue,
                wed,
                thu,
                fri,
                sat,
                current_music,
                card_item,
            ),
        )
        new_thread.start()

    def btn(frame, framelist):
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(pady=(0, 30))
        cancel_btn = ctk.CTkButton(
            btn_frame,
            text="Cancel",
            # width=70,
            font=("helvitica", 20, "bold"),
            command=window.destroy,
        )
        cancel_btn.pack(side="left", padx=10)
        global name, hour, minute, am_pm
        save_btn = ctk.CTkButton(
            btn_frame,
            text="Save Bell",
            # width=70,
            font=("helvitica", 20, "bold"),
            command=lambda: save_data_and_display_card(
                window, hour, minute, am_pm, name
            ),
        )
        save_btn.pack(padx=10)

    # schedule()
    name()
    time()
    weeks()
    music()
    btn(f, framelist)


def mode():
    appearence = ctk.get_appearance_mode()
    if appearence == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("Dark")


def open_frame(i, frame):
    frame0.forget()
    frame1.forget()
    frame2.forget()
    frame3.forget()
    frame4.forget()
    frame5.forget()
    frame6.forget()
    # print(i)
    frame.pack(expand=True, fill="both")


def double_click(b, button, l):
    input = ctk.CTkInputDialog().get_input()
    for i in range(len(button_list)):
        if button_list[i] == b:
            if input == None:
                pass
            else:
                button_list[i] = input
                button.configure(text=input)
                l.configure(text=input)
                # print(button_list[i])
    print(input)
    print(button_list)
    print(b)


main = ctk.CTkFrame(root)
main.pack(expand=True, fill="both")

main.rowconfigure(0, weight=1)

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.columnconfigure(3, weight=1)
main.columnconfigure(4, weight=1)

# ========================sidebar========================

sidebar = ctk.CTkFrame(main)
sidebar.grid(row=0, column=0, padx=20, pady=20, sticky="swen")


bellFrame = ctk.CTkFrame(sidebar)
bellFrame.pack(side="top", fill="x")

bellabel = ctk.CTkLabel(bellFrame, text="Bell Labels", font=("Times", 20))
bellabel.pack(side="left", anchor="s")

mainframe = ctk.CTkFrame(main)
mainframe.grid(row=0, column=1, columnspan=5, sticky="swen")


frame0 = ctk.CTkFrame(mainframe, fg_color="green")
scrol_frame0 = ctk.CTkScrollableFrame(frame0, corner_radius=0)
label0 = ctk.CTkLabel(frame0, text=button_list[0])

frame1 = ctk.CTkFrame(mainframe, fg_color="orange")
scrol_frame1 = ctk.CTkScrollableFrame(frame1, corner_radius=0)
label1 = ctk.CTkLabel(frame1, text=button_list[1])

frame2 = ctk.CTkFrame(mainframe, fg_color="magenta")
scrol_frame2 = ctk.CTkScrollableFrame(frame2, corner_radius=0)
label2 = ctk.CTkLabel(frame2, text=button_list[2])

frame3 = ctk.CTkFrame(mainframe, fg_color="royalblue")
scrol_frame3 = ctk.CTkScrollableFrame(frame3, corner_radius=0)
label3 = ctk.CTkLabel(frame3, text=button_list[3])

frame4 = ctk.CTkFrame(mainframe, fg_color="purple")
scrol_frame4 = ctk.CTkScrollableFrame(frame4, corner_radius=0)
label4 = ctk.CTkLabel(frame4, text=button_list[4])

frame5 = ctk.CTkFrame(mainframe, fg_color="crimson")
scrol_frame5 = ctk.CTkScrollableFrame(frame5, corner_radius=0)
label5 = ctk.CTkLabel(frame5, text=button_list[5])

frame6 = ctk.CTkFrame(mainframe, fg_color="teal")
scrol_frame6 = ctk.CTkScrollableFrame(frame6, corner_radius=0)
label6 = ctk.CTkLabel(frame6, text=button_list[6])


def btn():
    button0 = ctk.CTkButton(
        sidebar,
        text=button_list[0],
        text_color=("black", "white"),
        fg_color="transparent",
        # border_color="yellow",
        # border_width=1,
        hover_color="green",
        font=("Times", 15),
        command=lambda: open_frame(button_list[0], frame0),
    )
    button0.pack()
    button0.bind(
        "<Double-Button-1>",
        lambda event, b=button_list[0], button=button0, l=label0: double_click(
            b, button, l
        ),
    )

    button1 = ctk.CTkButton(
        sidebar,
        text=button_list[1],
        text_color=("black", "white"),
        fg_color="transparent",
        hover_color="orange",
        font=("Times", 15),
        command=lambda: open_frame(button_list[1], frame1),
    )
    button1.pack()
    button1.bind(
        "<Double-Button-1>",
        lambda event, b=button_list[1], button=button1, l=label1: double_click(
            b, button, l
        ),
    )
    button2 = ctk.CTkButton(
        sidebar,
        text=button_list[2],
        text_color=("black", "white"),
        fg_color="transparent",
        hover_color="magenta",
        font=("Times", 15),
        command=lambda: open_frame(button_list[2], frame2),
    )
    button2.pack()
    button2.bind(
        "<Double-Button-1>",
        lambda event, b=button_list[2], button=button2, l=label2: double_click(
            b, button, l
        ),
    )
    button3 = ctk.CTkButton(
        sidebar,
        text=button_list[3],
        text_color=("black", "white"),
        fg_color="transparent",
        hover_color="royalblue",
        font=("Times", 15),
        command=lambda: open_frame(button_list[3], frame3),
    )
    button3.pack()
    button3.bind(
        "<Double-Button-1>",
        lambda event, b=button_list[3], button=button3, l=label3: double_click(
            b, button, l
        ),
    )
    button4 = ctk.CTkButton(
        sidebar,
        text=button_list[4],
        text_color=("black", "white"),
        fg_color="transparent",
        hover_color="teal",
        font=("Times", 15),
        command=lambda: open_frame(button_list[4], frame4),
    )
    button4.pack()
    button4.bind(
        "<Double-Button-1>",
        lambda event, b=button_list[4], button=button4, l=label4: double_click(
            b, button, l
        ),
    )
    button5 = ctk.CTkButton(
        sidebar,
        text=button_list[5],
        text_color=("black", "white"),
        fg_color="transparent",
        hover_color="crimson",
        font=("Times", 15),
        command=lambda: open_frame(button_list[5], frame5),
    )
    button5.pack()
    button5.bind(
        "<Double-Button-1>",
        lambda event, b=button_list[5], button=button5, l=label5: double_click(
            b, button, l
        ),
    )
    button6 = ctk.CTkButton(
        sidebar,
        text=button_list[6],
        text_color=("black", "white"),
        fg_color="transparent",
        hover_color="teal",
        font=("Times", 15),
        command=lambda: open_frame(button_list[6], frame6),
    )
    button6.pack()
    button6.bind(
        "<Double-Button-1>",
        lambda event, b=button_list[6], button=button6, l=label6: double_click(
            b, button, l
        ),
    )


btn()

mode = ctk.CTkButton(sidebar, text="Change Theme", command=mode)
mode.pack(side="bottom")


def button_diff_frames():
    buttonframe = ctk.CTkFrame(frame0, corner_radius=0)
    buttonframe.place(relx=0.94, rely=0.94, anchor="se")

    btn = ctk.CTkButton(
        buttonframe,
        text="+",
        width=50,
        height=50,
        font=("arial", 40),
        command=lambda: open_window(
            scrol_frame0,
            frame0_data,
            time.strftime("%I"),
            time.strftime("%M"),
            time.strftime("%p"),
        ),
    )
    btn.pack(ipadx=5, ipady=5)

    buttonframe = ctk.CTkFrame(frame1, corner_radius=0)
    buttonframe.place(relx=0.94, rely=0.94, anchor="se")

    btn = ctk.CTkButton(
        buttonframe,
        text="+",
        width=50,
        height=50,
        font=("arial", 40),
        command=lambda: open_window(
            scrol_frame1,
            frame1_data,
            time.strftime("%I"),
            time.strftime("%M"),
            time.strftime("%p"),
        ),
    )
    btn.pack(ipadx=5, ipady=5)
    buttonframe = ctk.CTkFrame(frame2, corner_radius=0)
    buttonframe.place(relx=0.94, rely=0.94, anchor="se")

    btn = ctk.CTkButton(
        buttonframe,
        text="+",
        width=50,
        height=50,
        font=("arial", 40),
        command=lambda: open_window(
            scrol_frame2,
            frame2_data,
            time.strftime("%I"),
            time.strftime("%M"),
            time.strftime("%p"),
        ),
    )
    btn.pack(ipadx=5, ipady=5)
    buttonframe = ctk.CTkFrame(frame3, corner_radius=0)
    buttonframe.place(relx=0.94, rely=0.94, anchor="se")

    btn = ctk.CTkButton(
        buttonframe,
        text="+",
        width=50,
        height=50,
        font=("arial", 40),
        command=lambda: open_window(
            scrol_frame3,
            frame3_data,
            time.strftime("%I"),
            time.strftime("%M"),
            time.strftime("%p"),
        ),
    )
    btn.pack(ipadx=5, ipady=5)
    buttonframe = ctk.CTkFrame(frame4, corner_radius=0)
    buttonframe.place(relx=0.94, rely=0.94, anchor="se")

    btn = ctk.CTkButton(
        buttonframe,
        text="+",
        width=50,
        height=50,
        font=("arial", 40),
        command=lambda: open_window(
            scrol_frame4,
            frame4_data,
            time.strftime("%I"),
            time.strftime("%M"),
            time.strftime("%p"),
        ),
    )
    btn.pack(ipadx=5, ipady=5)
    buttonframe = ctk.CTkFrame(frame5, corner_radius=0)
    buttonframe.place(relx=0.94, rely=0.94, anchor="se")

    btn = ctk.CTkButton(
        buttonframe,
        text="+",
        width=50,
        height=50,
        font=("arial", 40),
        command=lambda: open_window(
            scrol_frame5,
            frame5_data,
            time.strftime("%I"),
            time.strftime("%M"),
            time.strftime("%p"),
        ),
    )
    btn.pack(ipadx=5, ipady=5)
    buttonframe = ctk.CTkFrame(frame6, corner_radius=0)
    buttonframe.place(relx=0.94, rely=0.94, anchor="se")

    btn = ctk.CTkButton(
        buttonframe,
        text="+",
        width=50,
        height=50,
        font=("arial", 40),
        command=lambda: open_window(
            scrol_frame6,
            frame6_data,
            time.strftime("%I"),
            time.strftime("%M"),
            time.strftime("%p"),
        ),
    )
    btn.pack(ipadx=5, ipady=5)


button_diff_frames()


def pack():
    frame0.pack()
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()
    frame5.pack()
    frame6.pack()
    label0.pack()
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    label6.pack()
    scrol_frame0.pack(expand=True, fill="both")
    scrol_frame1.pack(expand=True, fill="both")
    scrol_frame2.pack(expand=True, fill="both")
    scrol_frame3.pack(expand=True, fill="both")
    scrol_frame4.pack(expand=True, fill="both")
    scrol_frame5.pack(expand=True, fill="both")
    scrol_frame6.pack(expand=True, fill="both")
    frame0.forget()
    frame1.forget()
    frame2.forget()
    frame3.forget()
    frame4.forget()
    frame5.forget()
    frame6.forget()
    frame0.pack(expand=True, fill="both")


pack()
root.mainloop()
