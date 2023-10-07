import tkinter as tk


class FixedWidget(tk.Frame):
    def __init__(self, master, x, y):
        super().__init__(master)

        self.x = x
        self.y = y

        self.place(x=self.x, y=self.y)

        # Set the fixed property to True
        self.canvas.itemconfig(self, fixed=True)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a Canvas widget
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        # Create a fixed widget
        fixed_widget = FixedWidget(self.canvas, 100, 100)

        # Raise the fixed widget to the top of the stacking order
        self.canvas.tag_raise(fixed_widget)


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
