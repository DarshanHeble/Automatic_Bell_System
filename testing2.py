import tkinter as tk
from tkinter import ttk, simpledialog
import schedule
import time
import threading  # Import the threading module

# Initialize the main window
root = tk.Tk()
root.title("Alarm Scheduler")


# Function to open the subwindow for adding alarms
def open_subwindow():
    subwindow = tk.Toplevel(root)
    subwindow.title("Add Alarm")

    # Create and arrange widgets in the subwindow
    time_label = ttk.Label(subwindow, text="Time (HH:MM):")
    time_label.grid(row=0, column=0, padx=10, pady=5)
    time_entry = ttk.Entry(subwindow, width=10)
    time_entry.grid(row=0, column=1, padx=10, pady=5)

    days_label = ttk.Label(subwindow, text="Select Days:")
    days_label.grid(row=1, column=0, padx=10, pady=5)
    days_var = [tk.BooleanVar() for _ in range(7)]
    days_checkboxes = [
        ttk.Checkbutton(subwindow, text=day, variable=var)
        for day, var in zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], days_var)
    ]
    for i, checkbox in enumerate(days_checkboxes):
        checkbox.grid(row=1, column=i + 1)

    scheduler_var = tk.BooleanVar()
    scheduler_checkbutton = ttk.Checkbutton(
        subwindow, text="Scheduler On/Off", variable=scheduler_var
    )
    scheduler_checkbutton.grid(row=2, columnspan=2, padx=10, pady=5)

    song_label = ttk.Label(subwindow, text="Select Song:")
    song_label.grid(row=3, column=0, padx=10, pady=5)
    song_entry = ttk.Entry(subwindow, width=20)
    song_entry.grid(row=3, column=1, padx=10, pady=5)

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

        # Create an alarm card
        card_text = f"Time: {alarm_time}, Days: {', '.join(selected_days)}, Scheduler: {'On' if scheduler_on else 'Off'}, Song: {song}"
        alarm_card = ttk.Label(alarm_frame, text=card_text)
        alarm_card.pack(fill="x", padx=10, pady=5)

        # Set the schedule for the alarm
        def trigger_alarm():
            print(f"Ring the bell at {alarm_time} on {', '.join(selected_days)}")
            # Play the alarm sound (adjust the path to your sound file)
            # You can use pygame.mixer.music here

        if scheduler_on:
            for day in selected_days:
                schedule.every().day.at(alarm_time).do(trigger_alarm)

        subwindow.destroy()

    add_button = ttk.Button(subwindow, text="Add Alarm", command=add_alarm)
    add_button.grid(row=4, column=0, padx=10, pady=5)

    cancel_button = ttk.Button(subwindow, text="Cancel", command=subwindow.destroy)
    cancel_button.grid(row=4, column=1, padx=10, pady=5)


# Create a frame for displaying alarms with a scrollbar
alarm_frame = ttk.Frame(root)
alarm_frame.pack(fill="both", expand=True, padx=10, pady=10)
scrollbar = ttk.Scrollbar(alarm_frame, orient="vertical")
alarm_listbox = tk.Listbox(alarm_frame, yscrollcommand=scrollbar.set)
scrollbar.config(command=alarm_listbox.yview)
alarm_listbox.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create a button for adding alarms
add_alarm_button = ttk.Button(root, text="Add Alarm", command=open_subwindow)
add_alarm_button.pack(pady=10)


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
