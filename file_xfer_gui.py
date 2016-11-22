from tkinter import *
import tkinter as tk

import file_xfer_func


def load_gui(self):
    """ Populate the master Frame with the correct buttons
    and Tkinter widgets placed with grid geometry.
    """
    
    # create an entry text box for source button
    self.custom_source = StringVar()
    # set text box to a default string
    self.custom_source.set('Select a source directory')
    # set the width to 60 characters
    self.text_source = tk.Entry(self.master, width=60, textvariable=self.custom_source)
    self.text_source.grid(row=0, column=0, rowspan=1, columnspan=2, padx=(5, 0),
                          pady=(10, 20))

    # create an entry text box for destination button
    self.custom_dest = StringVar()
    # set text box to a default string
    self.custom_dest.set('Select a destination directory')
    # set the width to 60 characters
    self.text_dest = tk.Entry(self.master, width=60, textvariable=self.custom_dest)
    self.text_dest.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

    # create and place a source button
    self.button_source = tk.Button(self.master, width=12, height=1, text="Source",
                                   command=lambda: file_xfer_func.get_source(self))
    self.button_source.grid(row=0, column=2, padx=(10, 0), pady=(10, 20))

    # create and place a destination button
    self.button_dest = tk.Button(self.master, width=12, height=1, text="Destination",
                                 command=lambda: file_xfer_func.get_dest(self))
    self.button_dest.grid(row=1, column=2, padx=(10, 0), pady=(10, 20))
    
    # create and place a transfer button
    self.button_transfer = tk.Button(self.master, width=16, height=2, text="Transfer Files",
                                command=lambda: file_xfer_func.move_files(self, self.custom_source, self.custom_dest))
                                
    self.button_transfer.grid(row=2, column=0, padx=(0, 0), pady=(10, 10))

    # create and place a done button
    self.button_done = tk.Button(self.master, width=16, height=2, text="Done",
                                 command=lambda: file_xfer_func.close(self))
    self.button_done.grid(row=2, column=1, padx=(0, 0), pady=(10, 10))

    # connec to the database and create the table if it doesn't exist
    file_xfer_func.create_db(self)
