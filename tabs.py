import customtkinter as ctk
from tkinter import simpledialog
import os
import pickle

root = ctk.CTk()
root.geometry("900x600")

# File path for storing data
DATA_FILE = "tabs_data.pkl"

alarm_data = []
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
# music_file
music_files = []
curr_music = ctk.StringVar()

counter = 0
labels_dict = {}
labels_list = []


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


def mode():
    appearence = ctk.get_appearance_mode()
    if appearence == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("Dark")


def save_labels():
    with open(DATA_FILE, "wb") as f:
        pickle.dump(labels_list, f)


def load_labels():
    with open(DATA_FILE, "rb") as f:
        saved_labels = pickle.load(f)
        labels_list.extend(saved_labels)
        print(labels_list)


def addNewTab():
    global labels_dict, counter

    input = ctk.CTkInputDialog(text="Enter a unique tab name", title="Add Tab")
    label_name = input.get_input()
    if label_name in labels_dict:
        print("not unique")
        return

    label = ctk.CTkLabel(bellFrame, text=label_name)
    label.pack(padx=(10, 0))
    label.bind("<Button-1>", lambda event: change_color(label))
    # print(label)

    labels_dict[label_name] = label
    labels_list.append(label_name)
    print(labels_list)
    # print(labels_dict)

    save_labels()


def change_color(label):
    label.configure(fg_color="red", corner_radius=10)

    for other_label in labels_dict.values():
        if other_label != label:
            other_label.configure(fg_color="transparent", corner_radius=10)


def deleteNewTab():
    dialog = ctk.CTkInputDialog(text="Enter a tab name", title="Delete Tab")
    label_name = dialog.get_input()
    if label_name not in labels_dict:
        print("does not exist")
        return

    label = labels_dict[label_name]
    label.destroy()

    del labels_dict[label_name]
    labels_list.remove(label_name)
    print(labels_list)
    save_labels()


main = ctk.CTkFrame(root)
main.pack(fill="both", expand=True)

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
bellabel.pack(anchor="s")


btnframe = ctk.CTkFrame(bellFrame)
btnframe.pack(side="bottom")

addtabbtn = ctk.CTkButton(btnframe, text="Add Tab", command=addNewTab)
addtabbtn.pack(side="left")
deletetabbtn = ctk.CTkButton(btnframe, text="Delete Tab", command=deleteNewTab)
deletetabbtn.pack(side="right")

mode = ctk.CTkButton(sidebar, text="Change Theme", command=mode)
mode.pack(side="bottom")

# ========================sidebar========================
# ========================Frame========================

Scrll_frame = ctk.CTkScrollableFrame(main)
Scrll_frame.grid(row=0, column=1, columnspan=5, padx=20, pady=20, sticky="swen")

buttonframe = ctk.CTkFrame(
    Scrll_frame,
)
buttonframe.place(relx=0.94, rely=0.94, anchor="se")

btn = ctk.CTkButton(
    buttonframe, text="+", width=50, height=50, font=("arial", 40), command=open_window
)
btn.pack(ipadx=5, ipady=5, padx=5, pady=5)

load_labels()
root.mainloop()
# ========================Frame========================

# def change_color(event):
#     print("click")
#     le.configure(fg_color="red", corner_radius=10)


# le = ctk.CTkLabel(Scrll_frame, text="darshan")
# # le.pack()
# le.bind("<Button-1>", change_color)


# delete_tab = ctk.CTkButton(
#     buttonframe,
#     text="Delete Tab",
#     font=("arial", 25),
#     height=60,
#     command=deletetab,
# )
# delete_tab.pack()


# def change_color(event):
#     global labels
#     label = event.widget

#     for label in labels:
#         label.configure(fg_color="transparent", corner_radius=20)
# label.configure(fg_color="red", corner_radius=20)
# label1.configure(fg_color="transparent", corner_radius=20)


# label = ctk.CTkLabel(bellFrame, text="class")
# label.bind("<Button-1>", change_color)
# label.pack(padx=(10, 0))

# label1 = ctk.CTkLabel(bellFrame, text="exam")
# label1.bind("<Button-1>", change_color)
# label1.pack(padx=(10, 0))
