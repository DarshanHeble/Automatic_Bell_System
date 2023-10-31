import customtkinter as ctk
import os

root = ctk.CTk()
# root.geometry("500x500")

tabview = ctk.CTkTabview(root)
tabview.pack(fill="both", expand=True, padx=20, pady=20)

tabview.add("tab1")
tabview.add("tab2")
tabview.add("tab3")
tabview.add("tab4")

tabview.set("tab2")

# tab1 =
mainframe = ctk.CTkFrame(tabview.tab("tab1"))
mainframe.pack(fill="both", expand=True)

Scrll_frame = ctk.CTkScrollableFrame(mainframe)
Scrll_frame.pack(fill="both", expand=True)

buttonframe = ctk.CTkFrame(
    mainframe,
)
buttonframe.place(relx=0.94, rely=0.94, anchor="se")

btn = ctk.CTkButton(
    buttonframe,
    text="+",
    width=50,
    height=50,
    font=("arial", 40),
    # command=open_window,
)
btn.pack(ipadx=5, ipady=5, padx=5, pady=5)

root.mainloop()
