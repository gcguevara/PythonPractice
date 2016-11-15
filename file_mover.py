"""Python Workplace Simulation
Author: Garrett Guevara
Written/Tested in Python 3.5.2

Task: Your employer wants you to create a program that can
move .txt files from Folder A to Folder B at the click of
a button. Write a program that moves four .txt files from
one folder to another on your desktop.
"""


import shutil
import os


def file_mover():
    """ Loops through Folder-A, finds files that ends with '.txt',
    moves them to Folder-B, then prints what was moved successfully.
    """
    # declare variables for the source folder and destination folder as strings
    source = 'C://Users//Gary//Desktop//Folder-A'
    destination = 'C://Users//Gary//Desktop//Folder-B'

    # loop through the source folder
    for files in os.listdir(source):
        # if the files end with .txt, move them and print that it occurred
        if files.endswith('.txt'):
            # use os.path.join to create an absolute path
            file_source = os.path.join(source, files)
            file_destination = os.path.join(destination, files)
            # move the files using the absolute path
            shutil.move(file_source, file_destination)
            # print what was moved successfully
            print("Moved {} to Folder-B.".format(files))

file_mover()

