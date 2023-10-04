import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import schedule
import time
import threading
import pickle

# Initialize the main window
root = tk.Tk()
root.title("Alarm Scheduler")
root.geometry("500x500")

# Create a list to store alarm cards
alarm_cards = []


# Function to open the subwindow for adding alarms
def open_subwindow():
    subwindow = tk.Toplevel(root)
    subwindow.title("Add Alarm")

    # Create and arrange widgets in the subwindow
    frame = ttk.Frame(subwindow, padding=20)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Define a larger font size
    large_font = ("Arial", 12)

    # Create a custom style for widgets with the larger font
    style = ttk.Style()
    style.configure("Large.TLabel", font=large_font)
    style.configure("Large.TCheckbutton", font=large_font)
    style.configure("Large.TButton", font=large_font)
    style.configure("Large.TEntry", font=large_font)

    # Time Entry
    time_label = ttk.Label(frame, text="Time (HH:MM):", style="Large.TLabel")
    time_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    time_entry = ttk.Entry(frame, width=10, style="Large.TEntry")
    time_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    # Select Days
    days_label = ttk.Label(frame, text="Select Days:", style="Large.TLabel")
    days_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    days_var = [tk.BooleanVar() for _ in range(7)]
    days_checkboxes = [
        ttk.Checkbutton(frame, text=day, variable=var, style="Large.TCheckbutton")
        for day, var in zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], days_var)
    ]
    for i, checkbox in enumerate(days_checkboxes):
        checkbox.grid(row=1, column=i + 1, padx=5, pady=5, sticky="w")

    # Scheduler On/Off
    scheduler_var = tk.BooleanVar()
    scheduler_checkbutton = ttk.Checkbutton(
        frame,
        text="Scheduler On/Off",
        variable=scheduler_var,
        style="Large.TCheckbutton",
    )
    scheduler_checkbutton.grid(
        row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w"
    )

    # Select Song
    def select_song():
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3 *.wav")]
        )
        if file_path:
            song_entry.delete(0, tk.END)  # Clear any previous text
            song_entry.insert(0, file_path)

    song_label = ttk.Label(frame, text="Select Song:", style="Large.TLabel")
    song_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    song_entry = ttk.Entry(frame, width=20, style="Large.TEntry")
    song_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="w")
    song_select_button = ttk.Button(
        frame, text="Select", command=select_song, style="Large.TButton"
    )
    song_select_button.grid(row=3, column=3, padx=10, pady=5, sticky="w")

    # Add Alarm button
    def add_alarm():
        alarm_time = time_entry.get()
        selected_days = [
            day
            for day, var in zip(
                ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], days_var
            )
            if var.get()
        ]
        scheduler_on = scheduler_var.get()
        song = song_entry.get()

        # Validate all options are filled
        if not alarm_time or not selected_days or not song:
            messagebox.showerror("Error", "Please fill in all options.")
            return

        # Create an alarm card
        card_text = f"Time: {alarm_time}, Days: {', '.join(selected_days)}, Scheduler: {'On' if scheduler_on else 'Off'}, Song: {song}"
        alarm_card = ttk.Label(
            root,
            text=card_text,
            relief="raised",
            borderwidth=2,
            padding=(10, 5),
            font=large_font,
        )
        alarm_card.pack(fill="x", padx=10, pady=5)
        alarm_cards.append(alarm_card)  # Add the card to the list

        # Save the alarm_cards list to a file using pickle
        with open("alarm_cards.pkl", "wb") as file:
            pickle.dump(alarm_cards, file)

        # Set the schedule for the alarm
        def trigger_alarm():
            print(f"Ring the bell at {alarm_time} on {', '.join(selected_days)}")
            # Play the alarm sound (adjust the path to your sound file)

        if scheduler_on:
            for day in selected_days:
                schedule.every().day.at(alarm_time).do(trigger_alarm)

        subwindow.destroy()  # Close the subwindow after adding the alarm

    add_button = ttk.Button(
        frame, text="Add Alarm", command=add_alarm, style="Large.TButton"
    )
    add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

    cancel_button = ttk.Button(
        frame, text="Cancel", command=subwindow.destroy, style="Large.TButton"
    )
    cancel_button.grid(row=4, column=2, columnspan=2, padx=10, pady=10, sticky="e")

    # Configure grid weights for proper resizing
    for i in range(5):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)


# Create a button for adding alarms
add_alarm_button = ttk.Button(
    root, text="Add Alarm", command=open_subwindow, style="Large.TButton"
)
add_alarm_button.pack(pady=10, ipadx=10, ipady=10)


# Function to start the scheduler in a separate thread
def start_scheduler():
    while True:
        schedule.run_pending()

        time.sleep(1)


# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=start_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

root.mainloop()
