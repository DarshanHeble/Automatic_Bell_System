import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import ttk
import time


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.minsize(600, 600)
        self.master.geometry("600x600")

        self.createwidgets()

    def createwidgets(self):
        def scroll_event(event, time):
            if time == "hour":
                if event.delta > 0:
                    self.increment(hrbtn, "hour")
                else:
                    self.decrement(hrbtn, "hour")
            elif time == "minute":
                if event.delta > 0:
                    self.increment(minbtn, "minute")
                else:
                    self.decrement(minbtn, "minute")
            else:
                if event.delta > 0:
                    ampmbtn.configure(text="am")
                else:
                    ampmbtn.configure(text="pm")

        arrowup = Image.open("Assets/Images/dark_mode_arrow_up.png")
        arrowdown = Image.open("Assets/Images/dark_mode_arrow_down.png")

        mainframe = ctk.CTkFrame(root)

        arrowupframe = ctk.CTkFrame(mainframe, fg_color="transparent")
        hr_Arrow_Up = ctk.CTkButton(
            arrowupframe,
            width=20,
            text="",
            fg_color="transparent",
            command=lambda: self.increment(hrbtn, "hour"),
            image=ctk.CTkImage(dark_image=arrowup),
        )
        hr_Arrow_Up.pack(side="left", padx=(0, 40))
        hr_Arrow_Up.bind("<MouseWheel>", lambda event: scroll_event(event, "hour"))
        hr_Arrow_Up.bind("<Down>", lambda event: self.increment(hrbtn, "hour"))

        min_Arrow_Up = ctk.CTkButton(
            arrowupframe,
            text="",
            fg_color="transparent",
            width=20,
            command=lambda: self.increment(minbtn, "minute"),
            image=ctk.CTkImage(dark_image=arrowup),
        )
        min_Arrow_Up.pack(side="left", padx=(45, 0))
        min_Arrow_Up.bind("<MouseWheel>", lambda event: scroll_event(event, "minute"))
        min_Arrow_Up.bind("<Down>", lambda event: self.increment(hrbtn, "min"))

        ampm_Arrow_Up = ctk.CTkButton(
            arrowupframe,
            text="",
            fg_color="transparent",
            width=20,
            command=lambda: self.increment(minbtn, "minute"),
            image=ctk.CTkImage(dark_image=arrowup),
        )
        ampm_Arrow_Up.pack(side="right", padx=(0, 10))
        ampm_Arrow_Up.bind("<MouseWheel>", lambda event: scroll_event(event, "ampm"))
        ampm_Arrow_Up.bind("<Down>", lambda event: self.increment(hrbtn, "ampm"))

        arrowupframe.pack(fill="x", padx=28)

        timeframe = ctk.CTkFrame(mainframe, fg_color="transparent", border_width=1)
        timeframe.highlightbackground = "blue"
        timeframe.highlightthickness = 2

        hrbtn = ctk.CTkButton(
            timeframe,
            text="01",
            width=55,
            fg_color="transparent",
            height=60,
            font=("arial", 40, "bold"),
        )
        hrbtn.pack(ipadx=10, ipady=10, padx=10, side="left")
        hrbtn.bind("<MouseWheel>", lambda event: scroll_event(event, "hour"))

        ctk.CTkLabel(timeframe, text=":", font=("arial", 40, "bold")).pack(
            ipadx=5, ipady=10, side="left"
        )

        minbtn = ctk.CTkButton(
            timeframe,
            text="00",
            width=55,
            fg_color="transparent",
            height=60,
            font=("arial", 40, "bold"),
        )
        minbtn.pack(ipadx=10, ipady=10, padx=10, side="left")
        minbtn.bind("<MouseWheel>", lambda event: scroll_event(event, "minute"))

        ampmbtn = ctk.CTkButton(
            timeframe,
            text="AM",
            width=75,
            fg_color="transparent",
            height=60,
            font=("arial", 40, "bold"),
        )
        ampmbtn.pack(ipadx=10, ipady=10, padx=10, side="left")
        ampmbtn.bind("<MouseWheel>", lambda event: scroll_event(event, "ampm"))

        timeframe.pack(ipadx=0, ipady=5)

        arrowdownframe = ctk.CTkFrame(
            mainframe,
            fg_color="transparent",
        )
        hr_Arrow_down = ctk.CTkButton(
            arrowdownframe,
            width=20,
            fg_color="transparent",
            text="",
            command=lambda: self.decrement(hrbtn, "hour"),
            image=ctk.CTkImage(dark_image=arrowdown),
        )
        hr_Arrow_down.pack(side="left", padx=(0, 40))
        hr_Arrow_down.bind("<MouseWheel>", lambda event: scroll_event(event, "hour"))

        min_Arrow_down = ctk.CTkButton(
            arrowdownframe,
            width=20,
            fg_color="transparent",
            text="",
            command=lambda: self.decrement(minbtn, "minute"),
            image=ctk.CTkImage(dark_image=arrowdown),
        )
        min_Arrow_down.pack(side="left", padx=(45, 0))
        min_Arrow_down.bind("<MouseWheel>", lambda event: scroll_event(event, "minute"))

        ampm_Arrow_down = ctk.CTkButton(
            arrowdownframe,
            width=20,
            fg_color="transparent",
            text="",
            command=lambda: self.decrement(minbtn, "minute"),
            image=ctk.CTkImage(dark_image=arrowdown),
        )
        ampm_Arrow_down.pack(side="right", padx=(0, 10))
        ampm_Arrow_down.bind("<MouseWheel>", lambda event: scroll_event(event, "ampm"))

        arrowdownframe.pack(fill="x", padx=28)

        mainframe.pack(padx=20, pady=20)

        ctk.CTkButton(
            mainframe,
            text="save",
            command=lambda: self.save(
                hrbtn.cget("text"), minbtn.cget("text"), ampmbtn.cget("text")
            ),
        ).pack()

    def save(self, hr, min, ampm):
        print(hr, " ", min, " ", ampm)

    def increment(self, btn, time):
        value = btn.cget("text")
        if time == "hour":
            if int(value) == 12:
                btn.configure(text="01")
            else:
                btn.configure(text=f"{int(value)+1 :02}")
        elif time == "minute":
            if int(value) == 59:
                btn.configure(text="00")
            else:
                btn.configure(text=f"{int(value)+1:02}")
        # else:
        #     if value == "pm":
        #         btn.configure(text="am")
        #     else:
        #         btn.configure(text="pm")

    def decrement(self, btn, time):
        value = btn.cget("text")
        if time == "hour":
            if int(value) == 1:
                btn.configure(text="12")
            else:
                btn.configure(text=f"{int(value)-1 :02}")
        elif time == "minute":
            if int(value) == 0:
                btn.configure(text="59")
            else:
                btn.configure(text=f"{int(value)-1 :02}")
        # else:
        #     if value == "am":
        #         btn.configure(text="pm")
        #     else:
        #         btn.configure(text="am")


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
