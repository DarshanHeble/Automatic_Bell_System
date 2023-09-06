import tkinter as tk


def show_custom_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Custom Alarm Dialog")
    dialog.geometry("300x100")  # Set the width and height

    label = tk.Label(dialog, text="Enter Alarm Time (HH:MM):")
    label.pack(pady=10)

    entry = tk.Entry(dialog)
    entry.pack()

    ok_button = tk.Button(dialog, text="OK", command=dialog.destroy)
    ok_button.pack(pady=10)


root = tk.Tk()
root.title("Custom Alarm Entry")
root.geometry("400x200")

button = tk.Button(root, text="Add Alarm", command=show_custom_dialog)
button.pack(pady=20)

root.mainloop()
