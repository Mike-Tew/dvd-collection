from tkinter import *


def show_collection():
    dvd_output_field.delete(0, END)
    for index, dvd in enumerate(dvd_collection):
        dvd_output_field.insert(index, dvd)


def submit_title():
    """Submit a DVD title to the collection."""

    title = title_entry.get()

    if title.strip():
        dvd_collection.append(title)
        title_entry.delete(0, END)
        print(title)
        show_collection()


dvd_collection = [
    "Lord of the Rings",
    "Harry Potter",
    "Schilnder's List",
    "Inception",
    "Star Wars",
]


root = Tk()
root.title("DVD Collection")

title_label = Label(
    root,
    text="DVD COLLECTION",
    width=30,
    height=2,
    font=("Helvetica 16 bold"),
    bg="#bfbfbf",
)
title_label.grid(row=0, column=0, columnspan=3, pady=[0, 20])

entry_label = Label(root, text="Enter DVD Title:")
entry_label.grid(row=1, column=0, sticky="e")

title_entry = Entry(root)
title_entry.grid(row=1, column=1, sticky="ew")

submit_button = Button(root, text="SUBMIT", width=10, command=submit_title)
submit_button.grid(row=1, column=2)

dvd_output_field = Listbox(root, justify="center")
dvd_output_field.grid(
    row=2, column=0, columnspan=3, padx=60, pady=20, sticky="nsew"
)

exit_button = Button(root, text="EXIT", width=10, command=lambda: root.destroy())
exit_button.grid(row=3, column=1, pady=[0, 20])


show_collection()
root.mainloop()