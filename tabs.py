import customtkinter as ctk
from tkinter import simpledialog
import os


def open_window():
    # def name_increment():
    #     global name
    window = ctk.CTkFrame(root)
    window.place(relx=0.5, rely=0.5, anchor="center")
    card = ctk.CTkFrame(window)
    card.pack(padx=1005, pady=1005)
    heading = ctk.CTkLabel(
        card,
        text="Add New Bell",
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
        days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        weekd_days_frame = ctk.CTkFrame(card, fg_color="transparent")
        weekd_days_frame.pack(pady=15, padx=25)

        day_checkboxes = []
        for i, day in enumerate(days_of_week):
            day_var = ctk.StringVar(value="on")
            day_cb = ctk.CTkCheckBox(
                weekd_days_frame,
                text=day.lower(),
                corner_radius=50,
                border_width=2,
                width=20,
                onvalue="on",
                offvalue="off",
                variable=day_var,
            )
            day_cb.grid(row=0, column=i + 1, sticky="w")
            day_checkboxes.append(day_var)

        # Now you can access the state of each day's checkbox using day_checkboxes list.
        sunday, monday, tuesday, wednesday, thursday, friday, saturday = day_checkboxes

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

    def btn():
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
                print(hour)
                print(hr)
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
        global name, hour, minute, second
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


def createtab():
    dialog = ctk.CTkInputDialog(text="Enter a unique name", title="Name")
    tabName = dialog.get_input()
    tabview.add(tabName)


def deletetab():
    dialog = ctk.CTkInputDialog(text="Enter a unique name", title="Name")
    tabName = dialog.get_input()
    tabview.delete(tabName)
    # check = ctk.CTkTextbox(root)


def mode():
    appearence = ctk.get_appearance_mode()
    if appearence == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("Dark")


root = ctk.CTk()
root.geometry("900x600")

main = ctk.CTkFrame(root)
main.pack(fill="both", expand=True)

main.rowconfigure(0, weight=1)

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.columnconfigure(3, weight=1)
main.columnconfigure(4, weight=1)

sidebar = ctk.CTkFrame(main)
sidebar.grid(row=0, column=0, padx=20, pady=20, sticky="swen")

create_tab = ctk.CTkButton(
    sidebar,
    text="Add Tab",
    font=("arial", 25),
    height=60,
    command=createtab,
)
create_tab.pack()


mode = ctk.CTkButton(sidebar, text="Change Theme", command=mode)
mode.pack()

tabview = ctk.CTkTabview(main)
tabview.grid(row=0, column=1, columnspan=4, padx=20, pady=20, sticky="swen")

tabview.add("class")

tabmainframe = ctk.CTkFrame(tabview.tab("class"))
tabmainframe.pack(fill="both", expand=True)

Scrll_frame = ctk.CTkScrollableFrame(tabmainframe)
Scrll_frame.pack(fill="both", expand=True)

buttonframe = ctk.CTkFrame(
    tabmainframe,
)
buttonframe.place(relx=0.94, rely=0.94, anchor="se")

btn = ctk.CTkButton(
    buttonframe, text="+", width=50, height=50, font=("arial", 40), command=open_window
)
btn.pack(ipadx=5, ipady=5, padx=5, pady=5)
delete_tab = ctk.CTkButton(
    buttonframe,
    text="Delete Tab",
    font=("arial", 25),
    height=60,
    command=deletetab,
)
delete_tab.pack()

root.mainloop()

if __name__ == "__main__":
    main()
