from tkinter import *
import tkinter as tk

import file_xfer_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define max and min size of frame
        self.master = master
        self.master.minsize(500, 170)
        self.master.maxsize(500, 170)
        # give the master frame a name
        self.master.title("Daily File Transfer")
        # give it a background color
        self.master.configure(bg="#F0F0F0")

        file_xfer_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
