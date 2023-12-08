import tkinter as tk


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")
        self.resize_task = None
        self.previous_width = None
        self.column_length = 0

        self.master.bind("<Configure>", self.resize)

        self.row = 0

        self.create_widgets()
        self.display_frames()

    def resize(self, event):
        current_width = self.master.winfo_width()

        if current_width != self.previous_width:
            self.previous_width = current_width

            if self.resize_task is not None:
                self.master.after_cancel(self.resize_task)

            self.resize_task = self.master.after(1, self.update_frames)

    def update_frames(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        self.label.configure(text=(f"{width} {height}"))

        self.calculate_columns(width)
        self.display_frames()

    def calculate_columns(self, width):
        if 0 <= width < 500:
            self.column_length = 1
        elif 500 <= width < 1000:
            self.column_length = 2
        elif 1000 <= width < 1500:
            self.column_length = 3

    def create_widgets(self):
        self.label = tk.Label(self.master)
        self.label.pack()
        self.mainContainer = tk.Frame(self.master)
        self.mainContainer.pack(expand=True, fill="both")
        self.mainContainer.update_idletasks()

    def display_frames(self):
        n = 7
        row_length = int(n / (self.column_length + 1))
        row = 0
        col = 0

        self.delete_frames()
        for i in range(n):
            frame = tk.Frame(self.mainContainer, bg="green")
            frame.grid(
                row=row, column=col, ipadx=30, ipady=30, padx=30, pady=30, sticky="nesw"
            )

            label = tk.Label(frame, text=i)
            label.pack()
            col = col + 1
            if col == self.column_length + 1:
                col = 0
                row += 1

        # Set weight 1 for all columns in the main container
        for c in range(self.column_length + 1):
            self.mainContainer.columnconfigure(c, weight=1)

    def delete_frames(self):
        for widget in self.mainContainer.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = BellSystemApp(root)

    root.mainloop()
