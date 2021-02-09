from tkinter import *


def _exit():
    root.destroy()


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
title_label.grid(row=0, column=0, columnspan=2, pady=[0, 20])

entry_label = Label(
    root,
    width=10,
    text="DVD Title:"
)
entry_label.grid(row=1, column=0)

entry_field = Entry(root, width=50)
entry_field.grid(row=1, column=1)

exit_button = Button(root, text="EXIT", width=10, command=_exit)
exit_button.grid(row=3, column=0, columnspan=2, pady=[20, 0])

root.mainloop()