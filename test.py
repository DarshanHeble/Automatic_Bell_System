import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tkinter import ttk
from customtkinter import *
import win32gui
import ctypes
import winreg


class BellSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Bell System")
        set_appearance_mode("light")
        set_appearance_mode("dark")

        def get_accent_color():
            # Open the registry key containing the accent color information
            key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent"
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                    # Read the accent color value
                    value, _ = winreg.QueryValueEx(key, "AccentColorMenu")
                    return value
            except FileNotFoundError:
                return None

        def convert_to_hex(rgb_tuple):
            return "#{:02X}{:02X}{:02X}".format(*rgb_tuple)

        # Get the accent color
        accent_color = get_accent_color()

        if accent_color is not None:
            # Extract the RGB values
            red = accent_color & 0xFF
            green = (accent_color >> 8) & 0xFF
            blue = (accent_color >> 16) & 0xFF

            # Convert to hex and print the color code
            hex_color = convert_to_hex((red, green, blue))
            print(f"Windows Accent Color Code: {hex_color}")
        else:
            print("Unable to retrieve the accent color.")

        self.frame = ctk.CTkFrame(self.master, fg_color=hex_color)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.btn = ctk.CTkButton(self.master)
        self.btn.pack()

    def resize(self, event, str):
        print(event.width, str)


if __name__ == "__main__":
    root = ctk.CTk()
    app = BellSystemApp(root)

    root.mainloop()
