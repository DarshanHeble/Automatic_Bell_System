from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")
set_appearance_mode("")

btn = CTkButton(
    master=app,
    text="add alarm",
    corner_radius=32,
    # fg_color="#C850C0",
    fg_color="transparent",
    hover_color="#4158D0",
    border_color="#FFCC70",
    border_width=2,
)
# btn.pack(relx=0.5, rely=0.5, anchor="center")
btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()
