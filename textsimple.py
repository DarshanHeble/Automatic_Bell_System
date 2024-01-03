import customtkinter as ctk
from PIL import Image
import time


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.minsize(600, 600)
        self.master.geometry("600x600")

        self.sun = Image.open("Assets/Images/sunday.png")
        self.sunday_hover = Image.open("Assets/Images/sunday_hover.png")
        self.sunday_click = Image.open("Assets/Images/sunday_clicked.png")

        self.createwidgets()

    def createwidgets(self):
        frame = ctk.CTkFrame(self.master, fg_color="black")
        frame.pack(expand=True, fill="both")

        def OnEnter(btn):
            btn.configure(
                image=ctk.CTkImage(dark_image=self.sunday_hover, size=(50, 50))
            )

        def OnLeave(btn):
            btn.configure(image=ctk.CTkImage(dark_image=self.sun, size=(50, 50)))

        clicked = ctk.StringVar()
        btn = ctk.CTkButton(
            frame,
            text="",
            fg_color="transparent",
            hover_color="black",
            border_spacing=0,
            textvariable=clicked,
            anchor="w",
            image=ctk.CTkImage(
                dark_image=self.sun,
                size=(50, 50),
            ),
            command=lambda: self.click(btn, clicked),
        )
        btn.bind("<Enter>", lambda event: OnEnter(btn))
        btn.bind("<Leave>", lambda event: OnLeave(btn))
        btn.pack()

    def click(self, btn, var):
        btn.configure(
            image=ctk.CTkImage(
                dark_image=self.sunday_click,
                size=(50, 50),
            )
        )
        # self.sunday_hover = Image.open("Assets/Images/sunday_hover.png")
        print(var)


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
