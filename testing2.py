import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        # main setup
        super().__init__()
        self.title("Bell System")
        self.geometry("500x500")
        self.minsize(500, 500)

        # mainframe
        self.mainframe = MainFrame(self)

        self.mainloop()


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)


App()
