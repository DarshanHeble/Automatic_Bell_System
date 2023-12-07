import customtkinter as ctk
from customtkinter import *


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")
        self.resize_task = None

        # Bind the resize method to the Configure event of the root window
        self.master.bind("<Configure>", self.resize)

        # Initialize empty frame dictionary
        self.frames = {}

        # self.rows = 0
        # self.columns = 0

        # create all widgets
        self.create_widgets()
        self.display_frames(1)

    def resize(self, event):
        # Cancel any scheduled update
        if self.resize_task is not None:
            self.master.after_cancel(self.resize_task)

        # Schedule update with a delay of 100 milliseconds
        self.resize_task = self.master.after(100, self.update_frames)

    def update_frames(self):
        width = str(self.master.winfo_width())
        height = str(self.master.winfo_height())
        self.label.configure(text=(width + " " + height))
        self.text = width

        if width >= "500" and width <= "1000":
            self.display_frames(3)

    # def resize(self, event):
    #     width = str(self.master.winfo_width())
    #     height = str(self.master.winfo_height())

    #     self.label.configure(text=(width + " " + height))
    #     self.text = width
    #     # print(f"w= {width} \t h= {height}")
    #     if width >= "500" or width <= "1000":
    #         print("1000")
    #         # self.columns = 3

    #         # Cancel any scheduled update
    #         self.master.after_cancel(self.resize_task)

    #         # Schedule update with a delay of 100 milliseconds
    #         self.resize_task = self.master.after(100, self.update_frames)

    def create_widgets(self):
        # Main Frame
        self.label = ctk.CTkLabel(self.master)
        self.label.pack()
        self.mainContainer = ctk.CTkScrollableFrame(self.master)
        self.mainContainer.pack(expand=True, fill="both")

    def display_frames(self, column_length):
        n = 7
        row_length = int(n / (column_length + 1))
        row = 0
        col = 0
        print(column_length + 1)
        print(row_length)
        self.delete_frames()
        for i in range(n):
            if col == column_length + 1:
                col = 0
                row += 1
            frame = ctk.CTkFrame(self.mainContainer, fg_color="green")
            frame.grid(row=row, column=col, padx=15, pady=15, sticky="nesw")
            col = col + 1
            print(col)
            # frame.pack()

    def delete_frames(self):
        for widget in self.mainContainer.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
