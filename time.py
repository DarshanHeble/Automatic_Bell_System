import customtkinter
import datetime, time, winsound

app = customtkinter.CTk()
app.minsize(400, 400)

heading = customtkinter.CTkLabel(
    app,
    text="Add New Bell",
    font=("helvitica", 30, "bold"),
)
heading.pack(pady=20)

option_frame = customtkinter.CTkFrame(app)
option_frame.pack(pady=10,padx=10)

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

hrs = customtkinter.CTkOptionMenu(option_frame, values=hour_options, variable=hour,width=100,height=50,font=("helvitica",20),)
hrs.grid(row=0,column=0,padx=10)
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

min = customtkinter.CTkOptionMenu(option_frame, values=minute_options, variable=hour,width=100,font=("helvitica",20))
min.grid(row=0,column=1,padx=10)
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

sec = customtkinter.CTkOptionMenu(option_frame, values=second_options, variable=hour,width=100,font=("helvitica",20))
sec.grid(row=0,column=2,padx=10)
# =============================hours===============================


buttom = customtkinter.CTkButton(app, text="Set Alarm", font=("helvitica", 20, "bold"))
buttom.pack()

app.mainloop()
