import customtkinter
from tkinter import filedialog


class App(customtkinter.CTk):
    def __init__(self):
        # main setup
        super().__init__()
        # customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")
        self.title("Bell System")
        self.geometry("550x500")
        self.minsize(500, 500)
        # self.maxsize()

        # mainframe
        self.mainframe = MainFrame(self)

        self.mainloop()


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # mode
        self._set_appearance_mode("light")
        self.pack(fill="both", expand=True)
        self.Create_Scrollable_Frame()
        self.Create_Button()

    def Create_Scrollable_Frame(self):
        frame = customtkinter.CTkScrollableFrame(self)
        frame.pack(fill="both", expand=True)

        # widgets
        frame1 = customtkinter.CTkFrame(frame)
        frame1.pack(fill="both", padx=10, pady=10)

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

        weekd_days_frame = customtkinter.CTkFrame(frame1, fg_color="transparent")
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

    def Create_Button(self):
        def open_window():
            window = customtkinter.CTkFrame(self)
            # window.configure()
            # window.configure(width=self.winfo_width(), height=self.winfo_height())
            window.place(relx=0.5, rely=0.5, anchor="center")

            card = customtkinter.CTkFrame(window)
            card.pack(padx=1005, pady=1005)
            # window.pack(expand=True, fill="both")

            heading = customtkinter.CTkLabel(
                card,
                text="Add New Bell",
                font=("helvitica", 30, "bold"),
            )
            heading.pack(pady=20)

            def time():
                option_frame = customtkinter.CTkFrame(card, fg_color="transparent")
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
                    variable=minute,
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
                    variable=second,
                    width=100,
                    height=50,
                    font=("helvitica", 20),
                    dropdown_font=("helvitica", 15),
                )
                sec.grid(row=0, column=2, padx=10)

            def name():
                name_frame = customtkinter.CTkFrame(card, fg_color="transparent")
                name_frame.pack(pady=20, padx=25)

                name_label = customtkinter.CTkLabel(
                    name_frame, text="Label : ", font=("helvitica", 20)
                )
                name_label.pack(padx=5, side="left")
                name_entry = customtkinter.CTkEntry(name_frame, font=("helvitica", 20))
                name_entry.pack(padx=5)

            def weeks():
                weekd_days_frame = customtkinter.CTkFrame(card, fg_color="transparent")
                weekd_days_frame.pack(pady=15, padx=25)

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

            def music():
                def upload_music_file():
                    music_file = filedialog.askopenfilename(
                        title="select a music file", filetypes=[("MP3 files", "*.mp3")]
                    )
                    return music_file

                music_frame = customtkinter.CTkFrame(card, fg_color="transparent")
                music_frame.pack(pady=15)

                music_label = customtkinter.CTkLabel(
                    music_frame, text="Select Music : ", font=("helvitica", 20)
                )
                music_label.pack(side="left", padx=5)

                select_bell = customtkinter.CTkComboBox(music_frame)
                select_bell.pack(side="left", padx=5)

                upload_btn = customtkinter.CTkButton(
                    music_frame, text="Upload", width=20, command=upload_music_file
                )
                upload_btn.pack(padx=5, ipadx=5)

            def btn():
                btn_frame = customtkinter.CTkFrame(card)
                btn_frame.pack(padx=20, pady=20)

                cancel_btn = customtkinter.CTkButton(
                    btn_frame,
                    text="Cancel",
                    font=("helvitica", 20, "bold"),
                    command=window.destroy,
                )
                cancel_btn.pack(side="left")

                save_btn = customtkinter.CTkButton(
                    btn_frame, text="Save Bell", font=("helvitica", 20, "bold")
                )
                save_btn.pack()

            time()
            name()
            weeks()
            music()
            btn()

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
            # height=50,
            # fg_color="transparent",
            # corner_radius=10,
            font=("arial", 40),
            command=open_window,
        )
        btn.pack(ipadx=5, ipady=5, padx=5, pady=5)


App()

# {
#         frame2 = customtkinter.CTkFrame(frame)
#         frame2.pack(fill="both", padx=10, pady=10)

#         frame3 = customtkinter.CTkFrame(frame)
#         frame3.pack(fill="both", padx=10, pady=10)

#         frame3 = customtkinter.CTkFrame(frame)
#         frame3.pack(fill="both", padx=10, pady=10)

#         frame3 = customtkinter.CTkFrame(frame)
#         frame3.pack(fill="both", padx=10, pady=10)

#         frame3 = customtkinter.CTkFrame(frame)
#         frame3.pack(fill="both", padx=10, pady=10)
# }
