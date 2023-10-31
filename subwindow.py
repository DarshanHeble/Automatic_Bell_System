import tkinter as tk

# Create an empty list to store data from each frame
data_list = []


def open_input_window(edit_idx=None):
    input_window = tk.Toplevel(root)
    input_window.geometry("200x200")
    input_window.title("Time Input and Weekdays")

    # Create variables to store time and weekdays
    time_var = tk.StringVar()
    weekdays_vars = {}

    # Create labels and entry for time
    tk.Label(input_window, text="Enter Time:").pack()
    time_entry = tk.Entry(input_window, textvariable=time_var)
    time_entry.pack()

    # Create checkboxes for weekdays
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
        weekdays_vars[day] = tk.BooleanVar()
        checkbox = tk.Checkbutton(input_window, text=day, variable=weekdays_vars[day])
        checkbox.pack()

    if edit_idx is not None:
        # If editing, populate the fields with existing data
        data = data_list[edit_idx]
        time_var.set(data["Time"])
        for day, var in weekdays_vars.items():
            var.set(day in data["Weekdays"])

    def save_data():
        time = time_var.get()
        selected_weekdays = [day for day, var in weekdays_vars.items() if var.get()]
        data = {"Time": time, "Weekdays": selected_weekdays}
        if edit_idx is not None:
            # If editing, replace the data
            data_list[edit_idx] = data
        else:
            data_list.append(data)
        update_display()
        input_window.destroy()

    # Create a button to save data
    save_button = tk.Button(input_window, text="Save", command=save_data)
    save_button.pack()


def delete_frame(frame_idx):
    data_list.pop(frame_idx)
    update_display()


def update_display():
    # Clear the existing display
    for widget in display_frame.winfo_children():
        widget.destroy()

    # Create labels for each frame's data, along with edit and delete buttons
    for i, data in enumerate(data_list):
        label = tk.Label(
            display_frame,
            text=f"Frame {i + 1}: Time - {data['Time']}, Weekdays - {', '.join(data['Weekdays'])}",
        )
        label.pack()

        edit_button = tk.Button(
            display_frame, text="Edit", command=lambda i=i: open_input_window(i)
        )
        edit_button.pack()

        delete_button = tk.Button(
            display_frame, text="Delete", command=lambda i=i: delete_frame(i)
        )
        delete_button.pack()


root = tk.Tk()
root.geometry("500x500")
root.title("Data Frames")

open_window_button = tk.Button(
    root, text="Open Input Window", command=open_input_window
)
open_window_button.pack()

display_frame = tk.Frame(root)
display_frame.pack()

root.mainloop()
