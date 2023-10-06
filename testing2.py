import customtkinter as ctk


class CustomButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Set the button's position to the bottom right corner of the frame.
        self.place(relx=1.0, rely=1.0, anchor="se")

        # Load the plus image.
        plus_icon = ctk.CTkImage(Image.open("plus_icon.png"))

        # Set the button's image to the plus icon.
        self.config(image=plus_icon)


if __name__ == "__main__":
    root = ctk.CTk()

    # Create a new Tkinter frame to contain the button.
    frame = ctk.CTkFrame(root)
    frame.pack()

    # Create a new instance of the custom button class and add it to the frame.
    button = CustomButton(frame)
    button.pack()

    # Start the mainloop.
    root.mainloop()
