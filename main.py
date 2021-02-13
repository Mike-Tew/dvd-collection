# TODO
# Generate a SQL database
# View collection from SQL database
# Allow insertions into SQL database

from tkinter import *
import os
import sqlite3


conn = sqlite3.connect("dvd_collection.db")
cur = conn.cursor()
# cur.execute("""CREATE TABLE dvd_collection (title text)""")
# cur.execute("INSERT INTO dvd_collection VALUES(?)", ("Lord of the Rings",))
# cur.execute("INSERT INTO dvd_collection VALUES(?)", ("Harry Potter",))
# cur.execute("INSERT INTO dvd_collection VALUES(?)", ("Inception",))

# cur.execute("SELECT title FROM dvd_collection")
# dvd_collection = cur.fetchall()
conn.commit()
conn.close()

# print(dvd_collection)
# for title in dvd_collection:
#     print(title)

def fetch_collection():
    """Fetch the DVD collection from the database and return it as a list."""

    conn = sqlite3.connect("dvd_collection.db")
    cur = conn.cursor()
    cur.execute("SELECT title FROM dvd_collection")
    dvd_collection = []
    for dvd in cur.fetchall():
        dvd_collection.append(dvd[0])
    conn.close()
    print(dvd_collection)
    return dvd_collection


def show_collection():
    """Show DVD collection in the text field."""

    dvd_collection = fetch_collection()
    dvd_output_field.delete(0, END)
    for index, dvd in enumerate(dvd_collection):
        dvd_output_field.insert(index, dvd)


def submit_title():
    """Submit a DVD title to the collection."""

    title = title_entry.get()

    if title.strip():
        dvd_collection.append(title)
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
dvd_output_field.grid(row=2, column=0, columnspan=3, padx=60, pady=20, sticky="nsew")

exit_button = Button(root, text="EXIT", width=10, command=lambda: root.destroy())
exit_button.grid(row=3, column=1, pady=[0, 20])

test_button = Button(root, text="For testing only", width=20, command=fetch_collection)
test_button.grid(row=4)

show_collection()
root.mainloop()