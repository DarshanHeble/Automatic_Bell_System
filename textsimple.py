import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import ttk


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
            else:
                if event.delta > 0:
                    self.increment(minbtn, "minute")
                else:
                    self.decrement(minbtn, "minute")

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
        hr_Arrow_Up.pack(side="left")
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
        min_Arrow_Up.pack(side="right")
        arrowupframe.pack(fill="x", padx=28)
        min_Arrow_Up.bind("<MouseWheel>", lambda event: scroll_event(event, "min"))
        min_Arrow_Up.bind("<Down>", lambda event: self.increment(hrbtn, "min"))

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
            ipadx=10, ipady=10, padx=10, side="left"
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
        hr_Arrow_down.pack(side="left")
        hr_Arrow_down.bind("<MouseWheel>", lambda event: scroll_event(event, "hour"))

        min_Arrow_down = ctk.CTkButton(
            arrowdownframe,
            width=20,
            fg_color="transparent",
            text="",
            command=lambda: self.decrement(minbtn, "minute"),
            image=ctk.CTkImage(dark_image=arrowdown),
        )
        min_Arrow_down.pack(side="right")
        min_Arrow_down.bind("<MouseWheel>", lambda event: scroll_event(event, "minute"))

        arrowdownframe.pack(fill="x", padx=28)

        mainframe.pack(padx=20, pady=20)

    def increment(self, btn, time):
        value = int(btn.cget("text"))
        if time == "hour":
            if value == 12:
                btn.configure(text="01")
            else:
                btn.configure(text=f"{value+1 :02}")
        else:
            if value == 59:
                btn.configure(text="00")
            else:
                btn.configure(text=f"{value+1:02}")

    def decrement(self, btn, time):
        value = int(btn.cget("text"))
        if time == "hour":
            if value == 1:
                btn.configure(text="12")
            else:
                btn.configure(text=f"{value-1 :02}")
        else:
            if value == 0:
                btn.configure(text="59")
            else:
                btn.configure(text=f"{value-1 :02}")


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
