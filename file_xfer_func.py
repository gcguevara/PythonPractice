from tkinter import messagebox
from tkinter import filedialog


import datetime
import os
import shutil


def close(self):
    """Asks user if they would like to quit the application,
    and if so, kills the program.
    """
    if messagebox.askokcancel("Exit Program",
                              "Are you sure you want to close the application?"):
        self.master.destroy()
        os._exit(0)


def get_source(self):
    """Clears the current entry box, then replaces it with
    the selected file path.
    """
    self.text_source.delete(0, 60)
    self.custom_source = filedialog.askdirectory()
    self.text_source.insert(0, self.custom_source)


def get_dest(self):
    """Clears the current entry box, then replaces it with
    the selected file path
    """
    self.text_dest.delete(0, 60)
    self.custom_dest = filedialog.askdirectory()
    self.text_dest.insert(0, self.custom_dest)


def move_files(self, source, destination):
    """Accepts two file path parameters as a source and a destination.
    Searches through source parameter, finds all files that end in '.txt',
    compares their last modified timestamp (mtime) with 24 hours ago from
    application run time, and if the .txt file was modified in the last 24 hours,
    it will be moved to the destination parameter.
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

    # pop up a tkinter messagebox
    messagebox.showinfo("File Transfer", "Files moved successfully!")

