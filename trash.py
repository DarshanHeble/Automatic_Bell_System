import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import schedule
import time
import threading
import pickle

# Initialize the main window
root = tk.Tk()
root.title("Alarm Scheduler")
root.geometry("800x500")

# Create a list to store alarm data dictionaries
alarm_data = []


# Function to load saved alarm data from a file
def load_alarm_data():
    global alarm_data
    try:
        with open("alarm_data.pkl", "rb") as file:
            alarm_data = pickle.load(file)
    except FileNotFoundError:
        alarm_data = []


# Function to save alarm data to a pickle file
def save_alarm_data():
    with open("alarm_data.pkl", "wb") as file:
        pickle.dump(alarm_data, file)


# Load alarm data when the program starts
load_alarm_data()

# Create a custom style for widgets with the larger font
style = ttk.Style()
style.configure("Large.TLabel", font=("Arial", 12))
style.configure("Large.TCheckbutton", font=("Arial", 12))
style.configure("Large.TButton", font=("Arial", 15))
style.configure("Large.TEntry", font=("Arial", 12))


# Function to open the subwindow for adding alarms
def open_subwindow():
    subwindow = tk.Toplevel(root)
    subwindow.title("Add Alarm")

    # Create and arrange widgets in the subwindow
    frame = ttk.Frame(subwindow, padding=20)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

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

        # Create a dictionary for this alarm's data
        alarm_dict = {
            "time": alarm_time,
            "days": selected_days,
            "scheduler": scheduler_on,
            "song": song,
        }

        # Append the dictionary to the alarm_data list
        alarm_data.append(alarm_dict)

        # Set the schedule for the alarm
        def trigger_alarm():
            print(f"Ring the bell at {alarm_time} on {', '.join(selected_days)}")
            # Play the alarm sound (adjust the path to your sound file)

        if scheduler_on:
            for day in selected_days:
                schedule.every().day.at(alarm_time).do(trigger_alarm)

        subwindow.destroy()  # Close the subwindow after adding the alarm

        # Update the main window with the alarm cards
        update_alarm_cards()

        # Save the alarm data to a pickle file
        save_alarm_data()

    add_button = ttk.Button(
        frame, text="Add Alarm", command=add_alarm, style="Large.TButton"
    )
    add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

    cancel_button = ttk.Button(
        frame, text="Cancel", command=subwindow.destroy, style="Large.TButton"
    )
    cancel_button.grid(row=4, column=2, columnspan=2, padx=10, pady=10, sticky="e")
    # Configure grid weights for proper resizing
    for i in range(6):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)


# Function to update the main window with alarm cards
def update_alarm_cards():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the existing widgets

    # Create a button for adding alarms
    add_alarm_button = ttk.Button(
        root,
        text="Add Alarm",
        command=open_subwindow,
        style="Large.TButton",
        padding=10,
    )
    add_alarm_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    if not alarm_data:
        return

    # Create and display alarm cards based on alarm_data
    for idx, alarm in enumerate(alarm_data, start=1):
        card_text = f"Alarm {idx} - Time: {alarm['time']},\n Days: {', '.join(alarm['days'])},\n Scheduler: {'On' if alarm['scheduler'] else 'Off'},\n Song: {alarm['song']}"

        def delete_alarm(index):
            del alarm_data[index - 1]  # Subtract 1 to match the list index
            update_alarm_cards()
            save_alarm_data()  # Save the updated alarm data

        alarm_card = ttk.Label(
            root, text=card_text, relief="raised", borderwidth=2, padding=(10, 5)
        )
        alarm_card.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

        # Create a delete button for each alarm card
        delete_button = ttk.Button(
            root,
            text="Delete",
            command=lambda idx=idx: delete_alarm(idx),
            style="Large.TButton",
        )
        delete_button.grid(row=idx, column=1, padx=10, pady=5, sticky="w")


# Call the update_alarm_cards function initially to display any existing alarms
update_alarm_cards()


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
