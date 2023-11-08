# framee = ctk.CTkFrame(mainframe, width=2000, height=2000)
# framee.pack(expand=True, fill="both")
# bu = ctk.CTkButton(framee, command=framee.destroy)
# bu.pack()

# Scrll_frame = ctk.CTkScrollableFrame(mainframe)
# Scrll_frame.pack(expand=True, fill="both", padx=20, pady=20)

# label = ctk.CTkLabel(Scrll_frame, text="hello")
# label.pack()
# label.forget()
# buttonframe = ctk.CTkFrame(
#     mainframe,
# )
# buttonframe.place(relx=0.94, rely=0.94, anchor="se")

# btn = ctk.CTkButton(
#     buttonframe, text="+", width=50, height=50, font=("arial", 40), command=open_window
# )
# btn.pack(ipadx=5, ipady=5, padx=5, pady=5)

# load_labels()
# ========================Frame========================

# def change_color_and_open_tab(event):
#     print("click")
#     le.configure(fg_color="red", corner_radius=10)


# le = ctk.CTkLabel(Scrll_frame, text="darshan")
# # le.pack()
# le.bind("<Button-1>", change_color_and_open_tab)


# delete_tab = ctk.CTkButton(
#     buttonframe,
#     text="Delete Tab",
#     font=("arial", 25),
#     height=60,
#     command=deletetab,
# )
# delete_tab.pack()


# def change_color_and_open_tab(event):
#     global labels
#     label = event.widget

#     for label in labels:
#         label.configure(fg_color="transparent", corner_radius=20)
# label.configure(fg_color="red", corner_radius=20)
# label1.configure(fg_color="transparent", corner_radius=20)


# label = ctk.CTkLabel(bellFrame, text="class")
# label.bind("<Button-1>", change_color_and_open_tab)
# label.pack(padx=(10, 0))

# label1 = ctk.CTkLabel(bellFrame, text="exam")
# label1.bind("<Button-1>", change_color_and_open_tab)
# label1.pack(padx=(10, 0))
# def change_color_and_open_tab(label):
#     label_name = label.cget("text")
#     frame_name = label.cget("text")
#     # print(label_name)
#     frame_name = ctk.CTkFrame(mainframe)

#     sframe = ctk.CTkScrollableFrame(frame_name)
#     sframe.pack(expand=True, fill="both", padx=10, pady=20)
#     labela = ctk.CTkLabel(sframe, text=label_name)
#     labela.pack()
#     b = ctk.CTkButton(sframe, command=frame_name.destroy)
#     b.pack()
#     frame_name.cget(labela)
#     frame_name.pack(fill="x")
#     # print(label)
#     label.configure(fg_color="red", corner_radius=10)

#     for other_label in labels_dict.values():
#         if other_label != label:
#             other_label.configure(fg_color="transparent", corner_radius=10)
#             name = label.cget("text")
#             # name.des

# btnframe = ctk.CTkFrame(bellFrame)
# btnframe.pack(side="bottom")


# addtabbtn = ctk.CTkButton(btnframe, text="Add Tab", command=addNewTab)
# addtabbtn.pack(side="left")
# deletetabbtn = ctk.CTkButton(btnframe, text="Delete Tab", command=deleteNewTab)
# deletetabbtn.pack(side="right")

# def save_labels():
#     with open(DATA_FILE, "wb") as f:
#         pickle.dump(labels_list, f)


# def load_labels():
#     with open(DATA_FILE, "rb") as f:
#         saved_labels = pickle.load(f)
#         labels_list.extend(saved_labels)
#         for label_name in labels_list:
#             label = ctk.CTkLabel(bellFrame, text=label_name)
#             label.pack(padx=(10, 0))
#             tab_frame = ctk.CTkScrollableFrame(mainframe)
#             tab_frame.forget()
#             label.bind(
#                 "<Button-1>",
#                 lambda event, l=label: change_color_and_open_tab(l),
#             )
#             labels_dict[label_name] = label
#         # print(labels_list)
#         # print(labels_dict)


# def addNewTab():
#     global labels_dict, counter

#     input = ctk.CTkInputDialog(text="Enter a unique tab name", title="Add Tab")
#     label_name = input.get_input()
#     if label_name in labels_dict:
#         print("not unique")
#         popup = ctk.CTkToplevel(root)
#         # popup.geometry("200x100")
#         sentence = ctk.CTkLabel(popup, text="Please Use Unique Name Next Time")
#         sentence.pack(padx=20, pady=20)
#         close = ctk.CTkButton(popup, text="Close", command=popup.destroy)
#         close.pack(pady=(0, 20))
#         close.focus()
#         close.bind("<Return>", lambda event, b=close: b.invoke())
#         # popup.pack()
#         return

#     label = ctk.CTkLabel(bellFrame, text=label_name)
#     label.pack(padx=(10, 0))
#     label.bind("<Button-1>", lambda event: change_color_and_open_tab(label))
#     # print(label)

#     labels_dict[label_name] = label
#     labels_list.append(label_name)
#     # print(labels_list)
#     # print(labels_dict)


#     change_color_and_open_tab(label)
#     save_labels()
# def deleteNewTab():
#     dialog = ctk.CTkInputDialog(text="Enter a tab name", title="Delete Tab")
#     label_name = dialog.get_input()
#     if label_name not in labels_dict:
#         print("does not exist")
#         return

#     label = labels_dict[label_name]
#     label.destroy()

#     del labels_dict[label_name]
#     labels_list.remove(label_name)
#     print(labels_list)
#     save_labels()
