import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


import datetime
import os
import shutil
import sqlite3
import time


def close(self):
    """Asks user if they would like to quit the application,
    and if so, kills the program.
    """
    if messagebox.askokcancel("Exit Program",
                              "Are you sure you want to close the application?"):
        self.master.destroy()
        os._exit(0)


def create_db(self):
    """Establishes connection with database, and creates the table
    if it does not already exist.
    """
    conn = sqlite3.connect('file_xfer.db')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS timestamps(unix REAL)")
        conn.commit()
        c.close()
    conn.close()

    def read_db(self):
        """Reads the max unix value from the timestamps table, and
        populates the tkinter label widget.
        """
        conn = sqlite3.connect('file_xfer.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT MAX(unix) FROM timestamps")
            most_recent = c.fetchone()[0]
            most_recent = time.ctime(most_recent)
            c.close()
        conn.close()

        # create and populate the label_print widget
        self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
        self.label_print.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

    read_db(self)


def get_source(self):
    """Clears the current entry box, then replaces it with
    the selected file path.
    """
    self.text_source.delete(0, 60)
    self.custom_source = filedialog.askdirectory()
    self.text_source.insert(0, self.custom_source)


def get_dest(self):
    """Clears the current entry box, then replaces it with
    the selected file path.
    """
    self.text_dest.delete(0, 60)
    self.custom_dest = filedialog.askdirectory()
    self.text_dest.insert(0, self.custom_dest)


def move_files(self, source, destination):
    """Accepts two file path parameters as a source and a destination.
    Searches through source parameter, finds all files that end in '.txt',
    compares their last modified timestamp (mtime) with 24 hours ago from
    application run time, and if the .txt file was modified in the last 24 hours,
    it will be moved to the destination parameter. It will pop up a message box
    saying that it was completed successfully, then enters a unix timestamp into
    the database 'file_xfer.db'.
    """
    # declare variables for current run time and 24 hours ago
    now = datetime.datetime.now()
    ago = now - datetime.timedelta(hours=24)
    print('The following .txt files were modified in the last 24 hours: \n')

    # loop through files in the source parameter
    for files in os.listdir(source):
        # if the files end with '.txt', create variables with a path and stats
        if files.endswith('.txt'):
            path = os.path.join(source, files)
            st = os.stat(path)
            # create a variable with the file's timestamp from its stats
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            # compare the file's modified time with 24 hours ago
            if mtime > ago:
                # print the file and when it was last modified
                print('{} ~ last modified {}'.format(path, mtime))
                # use os.path.join to create an absolute path
                file_source = os.path.join(source, files)
                file_destination = os.path.join(destination, files)
                # move the files using the absolute path
                shutil.move(file_source, file_destination)
                # print what was moved successfully and to where
                print("\tMoved {} to {}.\n".format(files, destination))

    # enter current time into database on click event
    current_time = time.time()
    conn = sqlite3.connect('file_xfer.db')
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO timestamps VALUES({})".format(current_time))
        conn.commit()
        c.close()
    conn.close()

    # pop up a tkinter messagebox
    messagebox.showinfo("File Transfer", "Files moved successfully!")

    def read_db(self):
        """Reads the max unix value from the timestamps table, and
        populates the tkinter label widget.
        """
        conn = sqlite3.connect('file_xfer.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT MAX(unix) FROM timestamps")
            most_recent = c.fetchone()[0]
            most_recent = time.ctime(most_recent)
            c.close()
        conn.close()

        # create and populate the label_print widget with the new time
        self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
        self.label_print.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

    read_db(self)

