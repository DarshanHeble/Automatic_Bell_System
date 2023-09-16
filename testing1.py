import tkinter as tk
from tkinter import ttk


# Function to add a new card
def add_card():
    card = CardFrame(card_frame)
    card.pack(fill="x", padx=10, pady=5)


# Custom card widget
class CardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="solid", bd=1)

        # Create and arrange widgets
        self.label_entry = ttk.Entry(self, width=20)
        self.time_entry = ttk.Entry(self, width=8)

        self.weekday_vars = []
        self.checkboxes = []
        weekdays = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        for day in weekdays:
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(self, text=day, variable=var)
            self.weekday_vars.append(var)
            self.checkboxes.append(checkbox)

        self.label_entry.grid(row=0, column=0, padx=5, pady=5)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)

        for i, checkbox in enumerate(self.checkboxes):
            checkbox.grid(row=1, column=i, padx=5, pady=5)

        self.delete_button = ttk.Button(self, text="Delete Card", command=self.destroy)
        self.delete_button.grid(row=2, columnspan=len(weekdays), pady=5)


# Create the main window
root = tk.Tk()
root.title("Card Frame Example")

# Create a frame to hold the cards
card_frame = ttk.Frame(root)
card_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add a button to add new cards
add_button = ttk.Button(root, text="Add Card", command=add_card)
add_button.pack(pady=10)

# Add an initial card
add_card()

root.mainloop()
