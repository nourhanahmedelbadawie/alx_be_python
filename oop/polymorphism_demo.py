import math

class Shape:
    def __init__(self):
        self.area = 0  # Initialize area to 0

    def calculate_area(self):
        """Method to be overridden by derived classes to calculate area."""
        pass  # Placeholder for derived classes to implement


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  # Initialize the base class
        self.length = length
        self.width = width
        self.area = self.calculate_area()  # Calculate area when initialized

    def calculate_area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width  # Return area directly


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()  # Initialize the base class
        self.radius = radius
        self.area = self.calculate_area()  # Calculate area when initialized

    def calculate_area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2) 