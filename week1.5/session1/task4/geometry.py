# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

    # Add distance() method here

    def distance(self):

        return math.hypot(self.x, self.y)


    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def distance_to(self, new_x, new_y):

        dis = math.sqrt(((self.x-new_x)**2) + ((self.y-new_y)**2))

        return dis 

# Add a definition for a Circle class here, giving it

class Circle: 

    def __init__(self, centre, radius): 

        self.centre = centre
        self.radius = radius 

#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

    def area(self):

        return(3.14 * ((self.radius)**2))

    def perimeter(self): 

        return(3.14 * self.radius * 2)

# Don't add any testing code to this file!
