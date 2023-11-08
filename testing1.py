import customtkinter as ctk
from tkinter import ttk
import time

root = ctk.CTk()
# root.geometry("200x200")

# current_time = time.localtime()
# print(current_time)

# curr_time = time.strftime("%d-%m-%Y %I:%M:%S %p")
# # print(curr_time)
# am_or_pm = time.strftime("%p")
# print(am_or_pm)

# spin = ttk.Spinbox(root)
# spin.pack()


# button = ctk.CTkButton(root)
# button.pack()
# button.bind("<Button-1>", lambda event, l=label: hello(l))

days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

weekd_days_frame = ctk.CTkFrame(root, fg_color="transparent")
weekd_days_frame.pack(pady=(0, 30))
day_checkboxes = []
for i, day in enumerate(days_of_week):
    day_var = ctk.StringVar(value="on")
    day_cb = ctk.CTkCheckBox(
        weekd_days_frame,
        text=day.lower(),
        corner_radius=50,
        border_width=2,
        font=("helvitca", 18),
        width=60,
        onvalue="on",
        offvalue="off",
        variable=day_var,
    )
    day_cb.grid(row=0, column=i + 1)
    day_checkboxes.append(day_var)
# Now you can access the state of each day's checkbox using day_checkboxes list.
sunday, monday, tuesday, wednesday, thursday, friday, saturday = day_checkboxes

print(day_checkboxes)
root.mainloop()
