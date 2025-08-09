import math

class Shape:
    """Base class for all shapes."""
    def __init__(self):
        pass

    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    """Rectangle representing a circle."""
    def __init__(self, length, width):
        """Initialize the rectangle with width and height."""
        self.length = length
        self.width = width
 
    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Circle representing a circle."""
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius
 
    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
