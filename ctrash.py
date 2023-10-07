from customtkinter import *

root = CTk()
root.geometry("500x500")
# set_appearance_mode("light")
mainframe = CTkFrame(root)
mainframe.pack(fill="both", expand=TRUE)

frame = CTkScrollableFrame(mainframe)
frame.pack(fill="both", expand=TRUE)

frame1 = CTkFrame(frame, fg_color="yellow")
frame1.pack(fill="both", padx=20, pady=10)

frame2 = CTkFrame(frame, fg_color="red")
frame2.pack(fill="both", padx=20, pady=10)

frame3 = CTkFrame(frame, fg_color="blue")
frame3.pack(fill="both", padx=20, pady=10)

frame3 = CTkFrame(frame, fg_color="green")
frame3.pack(fill="both", padx=20, pady=10)

frame3 = CTkFrame(frame, fg_color="pink")
frame3.pack(fill="both", padx=20, pady=10)

frame3 = CTkFrame(frame, fg_color="yellow")
frame3.pack(fill="both", padx=20, pady=10)

buttonframe = CTkFrame(
    mainframe, fg_color="transparent", bg_color="transparent", corner_radius=40
)
buttonframe.place(relx=0.9, rely=0.9, anchor="se")

btn = CTkButton(buttonframe, text="Add", width=60)
btn.pack(ipadx=10, ipady=10, padx=5, pady=5)

# class CustomFrame(CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # Add widgets onto the frame, for example:
#         self.label = CTkLabel(self, text="Hello, Custom Frame!")
#         self.label.pack(pady=20)
#         self.btn = CTkButton(
#             self,
#             text="add alarm",
#             corner_radius=32,
#             # fg_color="#C850C0",
#             # fg_color="transparent",
#             hover_color="#4158D0",
#             border_color="#FFCC70",
#             border_width=2,
#             # anchor=SE,
#         )

#         self.btn.place(relx=0.7, rely=0.8)

#         # self.btn.pack()


# class CustomApp(CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x200")

#         Create a custom frame and add it to the main window
#         self.custom_frame = CustomFrame(master=self)
#         self.custom_frame.pack(fill="both", expand=True, padx=20, pady=20)


# if __name__ == "__main__":
#     app = CustomApp()
#     app.mainloop()

root.mainloop()
