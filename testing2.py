import customtkinter as ctk
import pickle

master = ctk.CTk()

counter = 0


def add_label():
    global counter
    counter += 1

    label_name = ctk.CTkInputDialog(text="enter name").get_input()

    # Check if the label name is unique
    if label_name in labels:
        print("The label name is not unique. Please enter a unique name.")
        return

    # Create a new label
    label = ctk.CTkLabel(master, text=label_name)
    label.pack()
    print(label_name)

    # Bind the label to button 1
    label.bind("<Button-1>", lambda event: change_label_color(label_name))

    # Add the label to the dictionary
    # labels[label_name] = label

    # Save the labels to a pickle file
    # with open("labels.pickle", "wb") as f:
    #     pickle.dump(labels, f)


def delete_label():
    label_name = ctk.CTkInputDialog(
        master, title="Delete Label", prompt="Enter the label name to delete: "
    ).get_input()

    # Check if the label name exists
    if label_name not in labels:
        print("The label name does not exist.")
        return

    # Delete the label
    label = labels[label_name]
    label.destroy()

    # Remove the label from the dictionary
    del labels[label_name]


def change_label_color(label):
    # Make the clicked label opaque
    label.configure(fg_color="black", bg_color="white")

    # Make other labels transparent
    for other_label in labels.values():
        if other_label != label:
            other_label.configure(fg_color="gray", bg_color="transparent")


# Create a dictionary to store the labels
labels = {}

# Create a button to add a new label
add_button = ctk.CTkButton(master, text="Add Label", command=add_label)
add_button.pack()

# Start the mainloop
master.mainloop()
