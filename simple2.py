import tkinter as tk
from tkinter import simpledialog


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left Frame
        self.left_frame = tk.Frame(self.main_frame, width=200, bg="lightgray")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        # Right Frame
        self.right_frame = tk.Frame(self.main_frame, bg="white")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create 6 buttons in the left frame
        for i in range(1, 7):
            button_frame = tk.Frame(self.left_frame, bg="lightgray")
            button_frame.grid(row=i, column=0, pady=5, sticky="ew")

            button = tk.Button(button_frame, text=f"Button {i}")
            button.pack(expand=True, fill=tk.BOTH)
            button.bind(
                "<Double-Button-1>", lambda event, btn=button: self.rename_button(btn)
            )
            button.bind("<Button-1>", lambda event, idx=i: self.show_frame(idx))

        # Initial frame in the right frame
        self.default_frame = tk.Frame(self.right_frame, bg="white")
        self.default_frame.pack(fill=tk.BOTH, expand=True)
        label = tk.Label(self.default_frame, text="Default Frame")
        label.pack(pady=10)

    def rename_button(self, button):
        new_name = simpledialog.askstring("Rename Button", "Enter new name:")
        if new_name:
            button.config(text=new_name)

    def show_frame(self, idx):
        # Unpack all frames in the right frame
        for child in self.right_frame.winfo_children():
            child.pack_forget()

        # Create or show the specific frame based on the button clicked
        frame_name = f"Frame {idx}"
        frame = tk.Frame(self.right_frame, bg="white")
        frame.pack(fill=tk.BOTH, expand=True)
        label = tk.Label(frame, text=frame_name)
        label.pack(pady=10)

        # Button for each frame in the specific frame
        frame_button = tk.Button(
            frame, text=f"Frame {idx} Button", command=lambda: self.show_frame(idx)
        )
        frame_button.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    root = tk.Tk()
    app = BellSystemApp(root)
    root.mainloop()
