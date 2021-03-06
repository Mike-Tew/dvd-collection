from tkinter import Tk, Button, Listbox, Entry, Label, END
import os
import sqlite3


_DBPATH = "./dvd_collection.db"

if os.path.isfile(_DBPATH) == False:
    conn = sqlite3.connect(_DBPATH)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE dvd_collection (title text)""")
    conn.commit()
    conn.close()


def delete_dvd():
    """Delete a DVD from the collection"""

    collection_items = dvd_output_field.get(0, END)

    try:
        selected_title = collection_items[dvd_output_field.curselection()[0]]
        conn = sqlite3.connect(_DBPATH)
        cur = conn.cursor()
        cur.execute("""DELETE FROM dvd_collection WHERE title = ?""", (selected_title,))
        conn.commit()
        conn.close()
    except:
        print("Please select a DVD")

    show_collection()


def fetch_collection():
    """Fetch the DVD collection from the database and return it as a list."""

    conn = sqlite3.connect(_DBPATH)
    cur = conn.cursor()
    cur.execute("SELECT title FROM dvd_collection")

    dvd_collection = []
    for dvd in cur.fetchall():
        dvd_collection.append(dvd[0])

    conn.close()
    return dvd_collection


def show_collection():
    """Show DVD collection in the text field."""

    dvd_collection = fetch_collection()
    dvd_output_field.delete(0, END)
    for index, dvd in enumerate(dvd_collection):
        dvd_output_field.insert(index, dvd)


def submit_title():
    """Submit a DVD title to the database and refresh the collection."""

    title = title_entry.get().strip()

    if title:
        conn = sqlite3.connect(_DBPATH)
        cur = conn.cursor()
        cur.execute("INSERT INTO dvd_collection VALUES(?)", (title,))
        conn.commit()
        conn.close()

        title_entry.delete(0, END)
        show_collection()


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
    row=2, column=0, columnspan=3, padx=60, pady=[20, 10], sticky="nsew"
)

delete_button = Button(root, text="DELETE SELECTED DVD", width=20, command=delete_dvd)
delete_button.grid(row=3, column=1)

exit_button = Button(root, text="EXIT", width=10, command=lambda: root.destroy())
exit_button.grid(row=4, column=1, pady=20)

show_collection()
root.mainloop()