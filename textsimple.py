import customtkinter as tk
import json


class ResizableWindow:
    def __init__(self):
        self.root = tk.CTk()
        self.root.title("Resizable Window")

        # Load width and height from the JSON file
        self.width, self.height = self.load_dimensions()

        print(self.width, self.height)

        # Set the initial size of the window
        self.root.geometry(f"{self.width}x{self.height}")

        # Bind the close event to the on_close method
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Add widgets and functionality here

    def on_close(self):
        # Save dimensions and close the window
        self.save_dimensions()
        self.root.destroy()

    def save_dimensions(self):
        data = {"width": self.root.winfo_width(), "height": self.root.winfo_height()}
        with open("dimensions.json", "w") as file:
            json.dump(data, file)

    def load_dimensions(self):
        try:
            with open("dimensions.json", "r") as file:
                data = json.load(file)
                return data.get("width", 800), data.get("height", 600)
        except FileNotFoundError:
            return 800, 600

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()


# Create an instance of ResizableWindow and run the application
app = ResizableWindow()
app.run()
