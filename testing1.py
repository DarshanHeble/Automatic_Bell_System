import customtkinter as ctk
import os

root = ctk.CTk()
root.geometry("500x500")

alarm_data = []
frames = []
music_files = ["music_file1.mp3", "music_file2.mp3"]

hour = ctk.StringVar()
minute = ctk.StringVar()
second = ctk.StringVar()
name = ctk.StringVar(value="bell")
sunday = ctk.StringVar(value="off")
monday = ctk.StringVar(value="on")
tuesday = ctk.StringVar(value="on")
wednesday = ctk.StringVar(value="on")
thursday = ctk.StringVar(value="on")
friday = ctk.StringVar(value="on")
saturday = ctk.StringVar(value="on")
curr_music = ctk.StringVar()
curr_music.set(music_files[0])


def open_window(edit_idx=None):
    window = ctk.CTkFrame(root)
    window.place(relx=0.5, rely=0.5, anchor="center")

    card = ctk.CTkFrame(window)
    card.pack(padx=10, pady=10)

    heading = ctk.CTkLabel(
        card,
        text="Add New Bell" if edit_idx is None else "Edit Bell",
        font=("helvitica", 30, "bold"),
    )
    heading.pack(pady=20)

    def time():
        option_frame = ctk.CTkFrame(card, fg_color="transparent")
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
        sec = ctk.CTkOptionMenu(
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
        name_frame = ctk.CTkFrame(card, fg_color="transparent")
        name_frame.pack(pady=20, padx=25)
        name_label = ctk.CTkLabel(name_frame, text="Label : ", font=("helvitica", 20))
        name_label.pack(padx=5, side="left")
        global name
        name_entry = ctk.CTkEntry(name_frame, font=("helvitica", 20), textvariable=name)
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
        music_frame.pack(pady=15)
        music_label = ctk.CTkLabel(
            music_frame, text="Select Music : ", font=("helvitica", 20)
        )
        music_label.pack(side="left", padx=5)
        music_files = get_music_files("music")
        curr_music.set(music_files[0])
        select_bell = ctk.CTkOptionMenu(
            music_frame,
            values=music_files,
            variable=curr_music,
        )
        print()
        select_bell.pack(side="left", padx=5)

    def save_data_and_display_card(window, hour, minute, second, name):
        def save_data_and_display_card(window, hour, minute, second, name):
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
                    frame = ctk.CTkFrame(Scrll_frame)
                    time = ctk.CTkLabel(frame, text=hr)
                    time.pack()
                    delete_frame = ctk.CTkButton(
                        frame, text="Delete", command=frame.destroy
                    )
                    delete_frame.pack()
                    window.destroy()
                    frame.pack(fill="both", padx=10, pady=10)

                display_card()

            save_data(name)

        btn_frame = ctk.CTkFrame(card)
        btn_frame.pack(padx=20, pady=20)
        cancel_btn = ctk.CTkButton(
            btn_frame,
            text="Cancel",
            font=("helvitica", 20, "bold"),
            command=window.destroy,
        )
        cancel_btn.pack(side="left")
        # global name, hour, minute, second
        save_btn = ctk.CTkButton(
            btn_frame,
            text="Save Bell",
            font=("helvitica", 20, "bold"),
            command=lambda: save_data_and_display_card(
                window, hour, minute, second, name
            ),
        )
        save_btn.pack()

    def btn():
        btn_frame = ctk.CTkFrame(card)
        btn_frame.pack(padx=20, pady=20)

        cancel_btn = ctk.CTkButton(
            btn_frame,
            text="Cancel",
            font=("helvitica", 20, "bold"),
            command=window.destroy,
        )
        cancel_btn.pack(side="left")

        save_btn = ctk.CTkButton(
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


def display_card(data, edit_idx):
    frame = ctk.CTkFrame(Scrll_frame)
    time_label = ctk.CTkLabel(frame, text=data["Time"])
    time_label.pack()
    edit_button = ctk.CTkButton(
        frame, text="Edit", command=lambda idx=edit_idx: open_window(idx)
    )
    edit_button.pack()
    delete_button = ctk.CTkButton(
        frame, text="Delete", command=lambda idx=edit_idx: delete_bell(idx)
    )
    delete_button.pack()
    frame.pack(fill="both", padx=10, pady=10)


def delete_bell(idx):
    if idx < len(alarm_data):
        alarm_data.pop(idx)
        update_display()


def update_display():
    Scrll_frame.destroy()
    Scrll_frame = ctk.CTkScrollableFrame(mainframe)
    Scrll_frame.pack(fill="both", expand=True)

    for i, data in enumerate(alarm_data):
        display_card(data, i)


mainframe = ctk.CTkFrame(root)
mainframe.pack(fill="both", expand=True)

Scrll_frame = ctk.CTkScrollableFrame(mainframe)
Scrll_frame.pack(fill="both", expand=True)

buttonframe = ctk.CTkFrame(mainframe)
buttonframe.place(relx=0.94, rely=0.94, anchor="se")

btn = ctk.CTkButton(
    buttonframe, text="+", width=50, height=50, font=("arial", 40), command=open_window
)
btn.pack(ipadx=5, ipady=5, padx=5, pady=5)

root.mainloop()
