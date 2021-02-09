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
title_label.grid(row=0, column=0)


exit_button = Button(root, text="EXIT", width=20, command=_exit)
exit_button.grid(row=3)

root.mainloop()