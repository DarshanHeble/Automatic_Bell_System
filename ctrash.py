from customtkinter import *


class CustomFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Add widgets onto the frame, for example:
        self.label = CTkLabel(self, text="Hello, Custom Frame!")
        self.label.pack(pady=20)
        self.btn = CTkButton(
            self,
            text="add alarm",
            corner_radius=32,
            # fg_color="#C850C0",
            # fg_color="transparent",
            hover_color="#4158D0",
            border_color="#FFCC70",
            border_width=2,
            # anchor=SE,
        )

        # btn.place(relx=0.5, rely=0.0)
        self.btn.lift()
        self.btn.pack()


class CustomApp(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")

        # Create a custom frame and add it to the main window
        self.custom_frame = CustomFrame(master=self)
        self.custom_frame.pack(fill="both", expand=True, padx=20, pady=20)


if __name__ == "__main__":
    app = CustomApp()
    app.mainloop()
