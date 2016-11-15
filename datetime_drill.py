""" Python Workplace Simulation

Author: Garrett Guevara
Written/Tested in Python Version 3.5.2

Task: Your company is headquartered in Portland, OR.
They've opened two new branches in NYC and London. They
ask that you create a program that tells if the branches
are open or closed based on the current time at HQ.
All branches are open 9:00AM-9:00PM
"""


import datetime


class Branch(object):
    """ A branch object for the hypothetical company. Each branch
    has the following attributes:

    name: A string with the branch name by location, i.e. "Portland"
    timezone: An integer that is the correct hour difference from UTC
    """
    # declare local opening and closing hour for branch, 9 AM to 9 PM
    opening_hour = 9  # 9 AM
    closing_hour = opening_hour + 12  # 9 PM

    def __init__(self, name, timezone=0):
        self.name = name
        self.timezone = timezone

    def __str__(self):
        return "The " + self.name + " branch is " + self.is_open() + "."

    def is_open(self):
        """ Compares if the current time adjusted for timezone is between
        the variables opening_hour and closing_hour. Returns "open" or "closed".
        """
        # find the current time in UTC
        now = datetime.datetime.utcnow()
        # add the now variable to the timezone argument
        hour_in_timezone = now.hour + self.timezone

        # if that hour is between 9 AM or 9 PM, return "open", else "closed"
        if self.opening_hour <= hour_in_timezone < self.closing_hour:
            return "open"
        else:
            return "closed"

# tell the person the current time based on the server they are using
currtime = datetime.datetime.now()
print("Hello, your current time is " + currtime.strftime('%H:%M:%S') + ".\n")

# declare array of three branches with correct timezone argument
branches = [
    Branch('Portland', -8),
    Branch('New York', -5),
    Branch('London', 0)
]

# loop through list and print a string telling if it's open or closed
for branch in branches:
    print(branch)





