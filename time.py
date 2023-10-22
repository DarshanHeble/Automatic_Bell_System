import customtkinter

root = customtkinter.CTk()
root.geometry("600x600")


card_data = []


def fun():
    card_item = {}
    name_entry = label_entry.get()
    hr = hour.get()
    mi = minute.get()
    sec = second.get()
    card_item.update({"hour": hr, "minute": mi, "second": sec})
    print(card_item)


hour = customtkinter.StringVar()
minute = customtkinter.StringVar()
second = customtkinter.StringVar()
label_entry = customtkinter.CTkEntry(root)


def time():
    option_frame = customtkinter.CTkFrame(root, fg_color="transparent")
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


time()
label_entry.pack()

btn = customtkinter.CTkButton(
    root, text="button", font=("arial", 20, "bold"), command=fun
)
btn.pack(pady=20)

root.mainloop()
