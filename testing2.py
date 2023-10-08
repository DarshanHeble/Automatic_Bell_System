import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        # main setup
        super().__init__()
        self._set_appearance_mode("light")
        self.title("Bell System")
        self.geometry("500x500")
        self.minsize(500, 500)

        # mainframe
        self.mainframe = MainFrame(self)

        self.mainloop()


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self._set_appearance_mode("light")

        self.pack(fill="both", expand=True)
        self.Create_Scrollable_Frame()

    def Create_Scrollable_Frame(self):
        frame = customtkinter.CTkScrollableFrame(self)
        frame.pack(fill="both", expand=True)
        self._set_appearance_mode("light")

        # widgets
        frame1 = customtkinter.CTkFrame(frame)
        frame1.pack(fill="both", padx=10, pady=10)

        frame2 = customtkinter.CTkFrame(frame)
        frame2.pack(fill="both", padx=10, pady=10)

        frame3 = customtkinter.CTkFrame(frame)
        frame3.pack(fill="both", padx=10, pady=10)

        frame3 = customtkinter.CTkFrame(frame)
        frame3.pack(fill="both", padx=10, pady=10)

        frame3 = customtkinter.CTkFrame(frame)
        frame3.pack(fill="both", padx=10, pady=10)

        frame3 = customtkinter.CTkFrame(frame)
        frame3.pack(fill="both", padx=10, pady=10)

        frame1.rowconfigure((0, 1, 2), weight=1)
        frame1.columnconfigure((0, 1, 2, 3), weight=1)

        time_label = customtkinter.CTkLabel(
            frame1, text="01:21", font=("arial", 70, "bold")
        )
        time_label.grid(row=0, column=0, columnspan=2, padx=15, pady=5, sticky="w")

        name_label = customtkinter.CTkLabel(
            frame1, text="Bell(1)", font=("arial", 20, "bold")
        )
        name_label.grid(row=1, column=0, padx=15, pady=5, sticky="w")

        weekd_days_frame = customtkinter.CTkFrame(frame1)
        weekd_days_frame.grid(
            row=2, column=0, columnspan=4, padx=15, pady=5, sticky="wnes"
        )
        weekd_days_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # check box
        mon_cb = customtkinter.CTkCheckBox(
            weekd_days_frame, text="sun", corner_radius=50, border_width=2
        )
        mon_cb.grid(row=0, column=1, sticky="w")
        mon_cb = customtkinter.CTkCheckBox(
            weekd_days_frame, text="mon", corner_radius=50, border_width=2
        )
        mon_cb.grid(row=0, column=2, sticky="w")
        mon_cb = customtkinter.CTkCheckBox(
            weekd_days_frame, text="tue", corner_radius=50, border_width=2
        )
        mon_cb.grid(row=0, column=3, sticky="w")
        mon_cb = customtkinter.CTkCheckBox(
            weekd_days_frame, text="wed", corner_radius=50, border_width=2
        )
        mon_cb.grid(row=0, column=4, sticky="w")
        mon_cb = customtkinter.CTkCheckBox(
            weekd_days_frame, text="thu", corner_radius=50, border_width=2
        )
        mon_cb.grid(row=0, column=5, sticky="w")
        mon_cb = customtkinter.CTkCheckBox(
            weekd_days_frame, text="fri", corner_radius=50, border_width=2
        )
        mon_cb.grid(row=0, column=6, sticky="w")
        mon_cb = customtkinter.CTkCheckBox(
            weekd_days_frame, text="sat", corner_radius=50, border_width=2
        )
        mon_cb.grid(row=0, column=7, sticky="w")

        buttonframe = customtkinter.CTkFrame(
            self,
            # fg_color="transparent",
            # bg_color="transparent",
            # corner_radius=40,
            # height=200,
        )

        buttonframe.place(relx=0.94, rely=0.94, anchor="se")

        btn = customtkinter.CTkButton(
            buttonframe,
            text="+",
            width=50,
            height=50,
            # fg_color="transparent",
            # corner_radius=10,
            font=("arial", 40),
        )
        btn.pack(ipadx=5, ipady=5, padx=5, pady=5)


App()
