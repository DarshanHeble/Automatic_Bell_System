import customtkinter
from tkinter import ttk
import datetime, time, winsound

app = customtkinter.CTk()
app.minsize(400, 400)
customtkinter.set_appearance_mode("light")

heading = customtkinter.CTkLabel(
    app,
    text="Add New Bell",
    font=("helvitica", 30, "bold"),
)
heading.pack(pady=20)

option_frame = customtkinter.CTkFrame(app, fg_color="transparent")
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
hour = customtkinter.StringVar()
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
minute = customtkinter.StringVar()
minute.set(minute_options[0])

min = customtkinter.CTkOptionMenu(
    option_frame,
    values=minute_options,
    variable=hour,
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
second = customtkinter.StringVar()
second.set(second_options[0])

sec = customtkinter.CTkOptionMenu(
    option_frame,
    values=second_options,
    variable=hour,
    width=100,
    height=50,
    font=("helvitica", 20),
    dropdown_font=("helvitica", 15),
)
sec.grid(row=0, column=2, padx=10)
# =============================hours===============================

name_frame = customtkinter.CTkFrame(app, fg_color="transparent")
name_frame.pack(pady=10, padx=25, anchor="w")

name_label = customtkinter.CTkLabel(name_frame, text="Label", font=("helvitica", 20))
name_label.grid(row=0, column=0, padx=5)
name_entry = customtkinter.CTkEntry(name_frame, font=("helvitica", 20))
name_entry.grid(row=0, column=1, padx=5)

weekd_days_frame = customtkinter.CTkFrame(app, fg_color="transparent")
weekd_days_frame.pack(padx=25)

mon_cb = customtkinter.CTkCheckBox(
    weekd_days_frame,
    text="sun",
    corner_radius=50,
    border_width=2,
    width=20,
)
mon_cb.grid(row=0, column=1, sticky="w")
mon_cb = customtkinter.CTkCheckBox(
    weekd_days_frame,
    text="mon",
    corner_radius=50,
    border_width=2,
    width=20,
)
mon_cb.grid(row=0, column=2, sticky="w", padx=10)
mon_cb = customtkinter.CTkCheckBox(
    weekd_days_frame,
    text="tue",
    corner_radius=50,
    border_width=2,
    width=20,
)
mon_cb.grid(row=0, column=3, sticky="w")
mon_cb = customtkinter.CTkCheckBox(
    weekd_days_frame,
    text="wed",
    corner_radius=50,
    border_width=2,
    width=20,
)
mon_cb.grid(row=0, column=4, sticky="w", padx=10)
mon_cb = customtkinter.CTkCheckBox(
    weekd_days_frame,
    text="thu",
    corner_radius=50,
    border_width=2,
    width=20,
)
mon_cb.grid(row=0, column=5, sticky="w")
mon_cb = customtkinter.CTkCheckBox(
    weekd_days_frame,
    text="fri",
    corner_radius=50,
    border_width=2,
    width=20,
)
mon_cb.grid(row=0, column=6, sticky="w", padx=10)
mon_cb = customtkinter.CTkCheckBox(
    weekd_days_frame,
    text="sat",
    corner_radius=50,
    border_width=2,
    width=20,
)
mon_cb.grid(row=0, column=7, sticky="w")

buttom = customtkinter.CTkButton(app, text="Set Alarm", font=("helvitica", 20, "bold"))
buttom.pack()

app.mainloop()
