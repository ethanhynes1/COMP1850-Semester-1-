# Week 1.5, Session 1: Task 3

import math 

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



# Finally, add code here to demonstrate use of Point

p = Point(1,1)
print(p.distance())
print(p.distance_to(1,1))