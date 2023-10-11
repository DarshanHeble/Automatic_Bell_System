import customtkinter
import datetime, time, winsound

app = customtkinter.CTk()
app.minsize(400, 400)

heading = customtkinter.CTkLabel(
    app, text="Alarm Clock", font=("helvitica", 40, "bold")
)
heading.pack()

set_alarm = customtkinter.CTkLabel(app, text="Set Time", font=("helvitica", 20, "bold"))
set_alarm.pack()

frame = customtkinter.CTkFrame(app)
frame.pack()


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

hrs = customtkinter.CTkOptionMenu(frame, values=hour_options, variable=hour)
hrs.pack()
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

min = customtkinter.CTkOptionMenu(frame, values=minute_options, variable=hour)
min.pack()
# =============================hours===============================
# =============================hours===============================
options = (
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
hour.set(options[0])

hrs = customtkinter.CTkOptionMenu(frame, values=options, variable=hour)
hrs.pack()
# =============================hours===============================


buttom = customtkinter.CTkButton(app, text="Set Alarm", font=("helvitica", 20, "bold"))
buttom.pack()

app.mainloop()
