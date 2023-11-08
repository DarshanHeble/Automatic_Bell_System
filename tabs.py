import customtkinter as ctk
from tkinter import simpledialog
import os
import pickle
import time

root = ctk.CTk()
root.geometry("900x600")

# File path for storing data
DATA_FILE = "tabs_data.pkl"

alarm_data = []
hour = ctk.StringVar()
minute = ctk.StringVar()
am_pm = ctk.StringVar()
curr_hr = time.strftime("%I")
curr_min = time.strftime("%M")
curr_am_pm = time.strftime("%p")
name = ctk.StringVar(value="bell")
sunday = ctk.StringVar(value="off")
monday = ctk.StringVar(value="on")
tuesday = ctk.StringVar(value="on")
wednesday = ctk.StringVar(value="on")
thursday = ctk.StringVar(value="on")
friday = ctk.StringVar(value="on")
saturday = ctk.StringVar(value="on")
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


def open_window(f):
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
        global hour, curr_hr
        hour.set(curr_hr)
        hrs = ctk.CTkOptionMenu(
            option_frame,
            values=hour_options,
            variable=hour,
            width=100,
            height=50,
            font=("helvitica", 20),
            dropdown_font=("helvitica", 15),
        )
        hrs.grid(row=0, column=0, padx=10)
        # =============================hours===============================
        # =============================hours===============================
        minute_options = (
            "00",
            "05",
            "10",
            "15",
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
        global minute, curr_min
        minute.set(curr_min)
        min = ctk.CTkOptionMenu(
            option_frame,
            values=minute_options,
            variable=minute,
            width=100,
            height=50,
            font=("helvitica", 20),
            dropdown_font=("helvitica", 15),
        )
        min.grid(row=0, column=1, padx=10)
        # =============================hours===============================
        # =============================hours===============================
        am_pm_options = ("PM", "AM")
        global am_pm, curr_am_pm
        am_pm.set(curr_am_pm)
        ampm = ctk.CTkOptionMenu(
            option_frame,
            values=am_pm_options,
            variable=am_pm,
            width=100,
            height=50,
            font=("helvitica", 20),
            dropdown_font=("helvitica", 15),
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
        weekd_days_frame.pack(pady=15, padx=25)
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

    def btn(frame):
        def save_data_and_display_card(window, hour, minute, am_pm, name):
            def save_data(name):
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
                        "music": current_music,
                    }
                )
                # print(hour)
                # print(hr)
                # print("data saved")

                def display_card():
                    global frame
                    # frames.append(create_frame())
                    # frames[-1].pack(fill="both", padx=10, pady=10)

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
                    frame = ctk.CTkFrame(f, fg_color="green")
                    timeFrame = ctk.CTkFrame(frame, fg_color="transparent")
                    time = ctk.CTkLabel(
                        timeFrame, text=f"{hr} : {mi} {ampm}", font=("helvitica", 35)
                    )
                    name_label = ctk.CTkLabel(frame, text=name)
                    week = ctk.CTkLabel(frame, text=" ".join(week_days))
                    music_label = ctk.CTkLabel(frame, text=current_music)
                    delete_frame = ctk.CTkButton(
                        frame, text="Delete", command=frame.destroy
                    )

                    timeFrame.pack()
                    time.pack()
                    name_label.pack()
                    week.pack()
                    music_label.pack()
                    delete_frame.pack()
                    window.destroy()
                    frame.pack(fill="x", expand=True, padx=20, pady=20)

                display_card()

            save_data(name)

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

    name()
    time()
    weeks()
    music()
    btn(f)


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
scrol_frame0 = ctk.CTkScrollableFrame(frame0)
label0 = ctk.CTkLabel(frame0, text=button_list[0])

frame1 = ctk.CTkFrame(mainframe, fg_color="orange")
scrol_frame1 = ctk.CTkScrollableFrame(frame1)
label1 = ctk.CTkLabel(frame1, text=button_list[1])

frame2 = ctk.CTkFrame(mainframe, fg_color="magenta")
scrol_frame2 = ctk.CTkScrollableFrame(frame2)
label2 = ctk.CTkLabel(frame2, text=button_list[2])

frame3 = ctk.CTkFrame(mainframe, fg_color="royalblue")
scrol_frame3 = ctk.CTkScrollableFrame(frame3)
label3 = ctk.CTkLabel(frame3, text=button_list[3])

frame4 = ctk.CTkFrame(mainframe, fg_color="purple")
label4 = ctk.CTkLabel(frame4, text=button_list[4])
scrol_frame4 = ctk.CTkScrollableFrame(frame4)

frame5 = ctk.CTkFrame(mainframe, fg_color="crimson")
label5 = ctk.CTkLabel(frame5, text=button_list[5])
scrol_frame5 = ctk.CTkScrollableFrame(frame5)

frame6 = ctk.CTkFrame(mainframe, fg_color="teal")
scrol_frame6 = ctk.CTkScrollableFrame(frame6)
label6 = ctk.CTkLabel(frame6, text=button_list[6])


def btn():
    button0 = ctk.CTkButton(
        sidebar,
        text=button_list[0],
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

buttonframe = ctk.CTkFrame(frame0, corner_radius=0)
buttonframe.place(relx=0.94, rely=0.94, anchor="se")

btn = ctk.CTkButton(
    buttonframe,
    text="+",
    width=50,
    height=50,
    font=("arial", 40),
    command=lambda: open_window(scrol_frame0),
)
btn.pack(ipadx=5, ipady=5, padx=5, pady=5)


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
