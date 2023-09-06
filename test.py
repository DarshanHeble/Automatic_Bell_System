import tkinter as tk
from tkinter import ttk
import schedule
import time
import threading
import pygame
from tkinter import simpledialog
import pickle

# Initialize pygame mixer
pygame.mixer.init()

# File path for storing data
DATA_FILE = "alarm_data.pkl"

# Create a list to store alarms
alarms = []


# Function to add an alarm card
def add_alarm_card():
    alarm_time = simpledialog.askstring("Add Alarm", "Enter Alarm Time (HH:MM):")
    if alarm_time:
        alarms.append(alarm_time)
        alarm_listbox.insert(tk.END, alarm_time)
        set_schedule()
        save_data()


# Function to delete a selected alarm
def delete_alarm():
    selected_index = alarm_listbox.curselection()
    if selected_index:
        alarms.pop(selected_index[0])
        alarm_listbox.delete(selected_index[0])
        set_schedule()
        save_data()


# Function to delete all alarms
def delete_all_alarms():
    alarm_listbox.delete(0, tk.END)  # Delete all items from the listbox
    alarms.clear()  # Clear the alarms list
    set_schedule()  # Update the schedule (no alarms left)


# Function to trigger the alarm
def trigger_alarm():
    for alarm_time in alarms:
        print(f"Ring the bell at {alarm_time}")
        # Play the alarm sound (adjust the path to your sound file)
        pygame.mixer.music.load("School-Period-bell.mp3")
        pygame.mixer.music.play()


# Function to set the schedule for alarms
def set_schedule():
    schedule.clear()
    for alarm_time in alarms:
        schedule.every().day.at(alarm_time).do(trigger_alarm)


# Function to start the scheduler in a separate thread
def start_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


# Function to save data to a file
def save_data():
    with open(DATA_FILE, "wb") as file:
        pickle.dump(alarms, file)


# Function to load data from a file
def load_data():
    try:
        with open(DATA_FILE, "rb") as file:
            saved_alarms = pickle.load(file)
            alarms.extend(saved_alarms)
            for alarm_time in saved_alarms:
                alarm_listbox.insert(tk.END, alarm_time)
            set_schedule()
    except FileNotFoundError:
        pass


# Create the main window
root = tk.Tk()
root.title("Automatic Bell System")
root.geometry("500x500")

# Set the window icon
root.iconbitmap("Musify.ico")

# Create a style for the button
button_style = ttk.Style()
button_style.configure("Custom.TButton", font=("Helvetica", 12), padding=(10, 10))

# Create UI elements
frame = ttk.Frame(root)
# frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
frame.pack()

title_label = ttk.Label(frame, text="School Bell Alarm", font=("Helvetica", 30))
title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

add_button = ttk.Button(
    frame, text="Add Alarm Card", style="Custom.TButton", command=add_alarm_card
)
add_button.grid(row=1, column=0, padx=5, pady=10, sticky="w")

delete_button = ttk.Button(
    frame, text="Delete Selected", style="Custom.TButton", command=delete_alarm
)
delete_button.grid(row=1, column=1, padx=5, pady=10, sticky="e")

delete_all_button = ttk.Button(
    frame, text="Delete All", style="Custom.TButton", command=delete_all_alarms
)
delete_all_button.grid(row=1, column=2, padx=5, pady=10, sticky="e")


# Create the alarm_listbox widget with a scrollbar
alarm_listbox_frame = ttk.Frame(frame)
alarm_listbox_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

alarm_listbox = tk.Listbox(
    alarm_listbox_frame, width=20, height=10, font=("Helvetica", 14)
)
alarm_listbox.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

scrollbar = ttk.Scrollbar(
    alarm_listbox_frame, orient="vertical", command=alarm_listbox.yview
)
scrollbar.grid(row=0, column=1, sticky="ns")
alarm_listbox.config(yscrollcommand=scrollbar.set)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=start_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

# Load saved data when the application starts
load_data()

root.mainloop()
