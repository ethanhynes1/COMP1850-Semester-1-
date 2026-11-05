# Worksheet 1.5: Person class

from datetime import date
from datetime import datetime

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):

        """
        Initialises the person class
        """
        if type(name) != str:
            raise TypeError

        elif name == "":
            raise ValueError

        if not isinstance (birth, date):
            raise TypeError("Birth date must be in the format YYYY-MM-DD.")


        

        self.name = name
        self.birth = birth


    def initials(self):
        """
        Returns initials
        """

        initials = "".join(word[0].upper() for word in self.name.split())
        return initials 

    def is_birthday(self):
        """
        Returns true if it is their birthday
        """
        if self.birth.strftime("%m-%d") == date.today().strftime("%m-%d"):
            return True

        else:
            return False



    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

