import customtkinter
import tkinter as tk
from tkinter import filedialog
import os
from os import listdir

root = customtkinter.CTk()
# customtkinter.set_appearance_mode("light")
root.geometry("500x500")

alarm_data = []
hour = customtkinter.StringVar()
minute = customtkinter.StringVar()
second = customtkinter.StringVar()
name = customtkinter.StringVar(value="bell")
sunday = customtkinter.StringVar(value="off")
monday = customtkinter.StringVar(value="on")
tuesday = customtkinter.StringVar(value="on")
wednesday = customtkinter.StringVar(value="on")
thursday = customtkinter.StringVar(value="on")
friday = customtkinter.StringVar(value="on")
saturday = customtkinter.StringVar(value="on")
# music_file
music_files = []
curr_music = customtkinter.StringVar()
frames = []
for frame in frames:
    frames[-1].pack()


def open_window():
    # def name_increment():
    #     global name
    window = customtkinter.CTkFrame(root)
    window.place(relx=0.5, rely=0.5, anchor="center")
    card = customtkinter.CTkFrame(window)
    card.pack(padx=1005, pady=1005)
    heading = customtkinter.CTkLabel(
        card,
        text="Add New Bell",
        font=("helvitica", 30, "bold"),
    )
    heading.pack(pady=20)

    def time():
        option_frame = customtkinter.CTkFrame(card, fg_color="transparent")
        option_frame.pack(pady=10, padx=10)
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
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
        )
        global hour
        hour.set(hour_options[0])
        hrs = customtkinter.CTkOptionMenu(
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
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "49",
            "41",
            "42",
            "43",
            "44",
            "45",
            "46",
            "47",
            "48",
            "49",
            "50",
            "51",
            "52",
            "53",
            "54",
            "55",
            "56",
            "57",
            "58",
            "59",
            "60",
        )
        global minute
        minute.set(minute_options[0])
        min = customtkinter.CTkOptionMenu(
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
        second_options = (
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
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "49",
            "41",
            "42",
            "43",
            "44",
            "45",
            "46",
            "47",
            "48",
            "49",
            "50",
            "51",
            "52",
            "53",
            "54",
            "55",
            "56",
            "57",
            "58",
            "59",
            "60",
        )
        global second
        second.set(second_options[0])
        sec = customtkinter.CTkOptionMenu(
            option_frame,
            values=second_options,
            variable=second,
            width=100,
            height=50,
            font=("helvitica", 20),
            dropdown_font=("helvitica", 15),
        )
        sec.grid(row=0, column=2, padx=10)

    def name():
        name_frame = customtkinter.CTkFrame(card, fg_color="transparent")
        name_frame.pack(pady=20, padx=25)
        name_label = customtkinter.CTkLabel(
            name_frame, text="Label : ", font=("helvitica", 20)
        )
        name_label.pack(padx=5, side="left")
        global name
        name_entry = customtkinter.CTkEntry(
            name_frame, font=("helvitica", 20), textvariable=name
        )
        name_entry.pack(padx=5)

    def weeks():
        weekd_days_frame = customtkinter.CTkFrame(card, fg_color="transparent")
        weekd_days_frame.pack(pady=15, padx=25)
        global sunday, monday, tuesday, wednesday, thursday, friday, saturday
        sun_cb = customtkinter.CTkCheckBox(
            weekd_days_frame,
            text="sun",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=sunday,
        )
        mon_cb = customtkinter.CTkCheckBox(
            weekd_days_frame,
            text="mon",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=monday,
        )
        tue_cb = customtkinter.CTkCheckBox(
            weekd_days_frame,
            text="tue",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=tuesday,
        )
        wed_cb = customtkinter.CTkCheckBox(
            weekd_days_frame,
            text="wed",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=wednesday,
        )
        thu_cb = customtkinter.CTkCheckBox(
            weekd_days_frame,
            text="thu",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=thursday,
        )
        fri_cb = customtkinter.CTkCheckBox(
            weekd_days_frame,
            text="fri",
            corner_radius=50,
            border_width=2,
            width=20,
            onvalue="on",
            offvalue="off",
            variable=friday,
        )
        sat_cb = customtkinter.CTkCheckBox(
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

        music_frame = customtkinter.CTkFrame(card, fg_color="transparent")
        music_frame.pack(pady=15)
        music_label = customtkinter.CTkLabel(
            music_frame, text="Select Music : ", font=("helvitica", 20)
        )
        music_label.pack(side="left", padx=5)
        music_files = get_music_files("music")
        curr_music.set(music_files[0])
        select_bell = customtkinter.CTkOptionMenu(
            music_frame,
            values=music_files,
            variable=curr_music,
        )
        print()
        select_bell.pack(side="left", padx=5)

    def btn():
        def save_data_and_display_card(window, hour, minute, second, name):
            def create_frame():
                # frame = tk.Frame()
                frame = customtkinter.CTkFrame(Scrll_frame)
                lab = customtkinter.CTkLabel(frame, text="this is a frame")
                lab.pack()
                window.destroy()
                return frame

            def save_data(name):
                card_item = {}
                # time
                hr = hour.get()
                mi = minute.get()
                sec = second.get()
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
                        "second": sec,
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
                print("data saved")

            def display_card():
                global frame
                # frames.append(create_frame())
                # frames[-1].pack(fill="both", padx=10, pady=10)
                frame = customtkinter.CTkFrame(Scrll_frame)
                lab = customtkinter.CTkLabel(frame, text="this is a frame")
                # lab.pack()
                window.destroy()
                frame.pack(fill="both", padx=10, pady=10)

            display_card()
            save_data(name)

        btn_frame = customtkinter.CTkFrame(card)
        btn_frame.pack(padx=20, pady=20)
        cancel_btn = customtkinter.CTkButton(
            btn_frame,
            text="Cancel",
            font=("helvitica", 20, "bold"),
            command=window.destroy,
        )
        cancel_btn.pack(side="left")
        global name, hour, minute, second
        save_btn = customtkinter.CTkButton(
            btn_frame,
            text="Save Bell",
            font=("helvitica", 20, "bold"),
            command=lambda: save_data_and_display_card(
                window, hour, minute, second, name
            ),
        )
        save_btn.pack()

    time()
    name()
    weeks()
    music()
    btn()


def create_frame():
    # frame = tk.Frame()
    frame = customtkinter.CTkFrame(Scrll_frame)
    lab = customtkinter.CTkLabel(frame, text="this is a frame")
    # lab.pack()
    frame.pack(fill="both", padx=10, pady=10)


mainframe = customtkinter.CTkFrame(root)
mainframe.pack(fill="both", expand=True)

Scrll_frame = customtkinter.CTkScrollableFrame(mainframe)
Scrll_frame.pack(fill="both", expand=True)

buttonframe = customtkinter.CTkFrame(
    mainframe,
)
buttonframe.place(relx=0.94, rely=0.94, anchor="se")

btn = customtkinter.CTkButton(
    buttonframe,
    text="+",
    width=50,
    height=50,
    font=("arial", 40),
    command=open_window,
)
btn.pack(ipadx=5, ipady=5, padx=5, pady=5)

root.mainloop()
