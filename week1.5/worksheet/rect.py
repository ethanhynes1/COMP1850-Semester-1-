# Worksheet 1.5: Rectangle Class





class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if type(width) != int or type(height) != int:
             raise TypeError

        elif width <= 0 or height <= 0:
            raise ValueError

        self.width = width
        self.height = height

    def is_square(self):
        """
        Decides if rectangle if a square 
        """
        if self.width == self.height:
            return True

        else:
            return False 

    def area(self):
        """
        return area of square 
        """

        return (self.width * self.height)

    def perimeter(self):
        """
        returns perimeter of square  
        """

        return (self.width*2 + self.height*2)
 
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
