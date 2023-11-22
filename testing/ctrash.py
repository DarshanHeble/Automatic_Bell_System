from customtkinter import *

root = CTk()
root.geometry("500x500")
set_appearance_mode("light")
mainframe = CTkFrame(root)
mainframe.pack(fill="both", expand=TRUE)


frame = CTkScrollableFrame(mainframe)
frame.pack(fill="both", expand=TRUE)

frame1 = CTkFrame(frame)
frame1.pack(fill="both", padx=10, pady=10)


frame2 = CTkFrame(frame)
frame2.pack(fill="both", padx=10, pady=10)

frame3 = CTkFrame(frame)
frame3.pack(fill="both", padx=10, pady=10)

frame3 = CTkFrame(frame)
frame3.pack(fill="both", padx=10, pady=10)

frame3 = CTkFrame(frame)
frame3.pack(fill="both", padx=10, pady=10)

frame3 = CTkFrame(frame)
frame3.pack(fill="both", padx=10, pady=10)

# ===================================contents============================================
frame1.rowconfigure((0, 1, 2), weight=1)
frame1.columnconfigure((0, 1, 2, 3), weight=1)

time_label = CTkLabel(frame1, text="01:21", font=("arial", 70, "bold"))
time_label.grid(row=0, column=0, columnspan=2, padx=15, pady=5, sticky="w")

name_label = CTkLabel(frame1, text="Bell(1)", font=("arial", 20, "bold"))
name_label.grid(row=1, column=0, padx=15, pady=5, sticky="w")

weekd_days_frame = CTkFrame(frame1)
weekd_days_frame.grid(row=2, column=0, columnspan=4, padx=15, pady=5, sticky="wnes")
weekd_days_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

# check box
mon_cb = CTkCheckBox(weekd_days_frame, text="sun", corner_radius=50, border_width=2)
mon_cb.grid(row=0, column=1, sticky="w")
mon_cb = CTkCheckBox(weekd_days_frame, text="mon", corner_radius=50, border_width=2)
mon_cb.grid(row=0, column=2, sticky="w")
mon_cb = CTkCheckBox(weekd_days_frame, text="tue", corner_radius=50, border_width=2)
mon_cb.grid(row=0, column=3, sticky="w")
mon_cb = CTkCheckBox(weekd_days_frame, text="wed", corner_radius=50, border_width=2)
mon_cb.grid(row=0, column=4, sticky="w")
mon_cb = CTkCheckBox(weekd_days_frame, text="thu", corner_radius=50, border_width=2)
mon_cb.grid(row=0, column=5, sticky="w")
mon_cb = CTkCheckBox(weekd_days_frame, text="fri", corner_radius=50, border_width=2)
mon_cb.grid(row=0, column=6, sticky="w")
mon_cb = CTkCheckBox(weekd_days_frame, text="sat", corner_radius=50, border_width=2)
mon_cb.grid(row=0, column=7, sticky="w")

# ===================================contents============================================
# ===================================button============================================

buttonframe = CTkFrame(
    mainframe,
    # fg_color="transparent",
    # bg_color="transparent",
    # corner_radius=40,
    # height=200,
)
buttonframe.place(relx=0.94, rely=0.94, anchor="se")

btn = CTkButton(
    buttonframe,
    text="+",
    width=50,
    height=50,
    # fg_color="transparent",
    # corner_radius=10,
    font=("arial", 40),
)
btn.pack(ipadx=5, ipady=5, padx=5, pady=5)

# ===================================button============================================
root.mainloop()
