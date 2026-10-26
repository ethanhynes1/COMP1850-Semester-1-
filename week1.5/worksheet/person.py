# Worksheet 1.5: Person class

from datetime import date
from datetime import datetime

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):


        if type(name) != str:
            raise TypeError

        elif name == "":
            raise ValueError

        elif birth != datetime.strptime(birth, "%Y-%m-%d"):
            print("yes")
            raise ValueError

        

        self.name = name
        self.birth = birth

    def initials(self):

        initials = "".join(word.name[0].upper for word in self.name.split())
        return initials 

    def is_birthday(self):

        if self.birth.strftime("%m-%d") == date.today().strftime("%m-%d"):
            return True



    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

p = Person("Ethan", "2007-11-09")
