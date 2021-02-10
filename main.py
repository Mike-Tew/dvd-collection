from tkinter import *


def _exit():
    root.destroy()


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

entry_field = Entry(root)
entry_field.grid(row=1, column=1, sticky="ew")

submit_button = Button(root, text="SUBMIT", width=10)
submit_button.grid(row=1, column=2)

dvd_output_field = Listbox(root)
dvd_output_field.grid(row=2, column=0, columnspan=2, padx=[40, 0], pady=20, sticky="nsew")

for index, dvd in enumerate(dvd_collection):
    dvd_output_field.insert(index, dvd)

view_button = Button(root, text="VIEW", width=10)
view_button.grid(row=2, column=2)

exit_button = Button(root, text="EXIT", width=10, command=_exit)
exit_button.grid(row=3, column=1, pady=[0, 20])

root.mainloop()