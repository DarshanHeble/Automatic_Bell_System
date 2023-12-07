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

        # Track previous window width
        self.previous_width = None

        self.row = 0
        self.column_length = 0

        # create all widgets
        self.create_widgets()
        self.display_frames(self.column_length)

    def resize(self, event):
        # Get current window width
        current_width = str(self.master.winfo_width())

        # Check if window size changed
        if current_width != self.previous_width:
            # Update previous width
            self.previous_width = current_width

            # Cancel any scheduled update
            if self.resize_task is not None:
                self.master.after_cancel(self.resize_task)

            # Schedule update with a delay of 100 milliseconds
            self.resize_task = self.master.after(1, self.update_frames)

    def update_frames(self):
        width = str(self.master.winfo_width())
        height = str(self.master.winfo_height())
        self.label.configure(text=(width + " " + height))
        self.text = width

        if width <= "500":
            self.column_length = 1
            # print(self.column_length)
        elif width >= "500" and width <= "1000":
            self.column_length = 2
            print(self.column_length + "red")

        # Only run display_frames if width changed

        if width != self.previous_width:
            print(self.column_length)
            self.display_frames(self.column_length)

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
        # print(column_length + 1)
        # print(row_length)
        print("displaing")
        self.delete_frames()
        for i in range(n):
            frame = ctk.CTkFrame(self.mainContainer, fg_color="green", width=300)
            frame.grid(row=row, column=col, padx=15, pady=15, sticky="nesw")
            col = col + 1
            if col == column_length + 1:
                col = 0
                row += 1

    def delete_frames(self):
        for widget in self.mainContainer.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
