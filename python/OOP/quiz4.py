import math

class Shape:
    def calculate_area(self):
        pass


    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius*2

    def calculate_area(self):
        return round(math.pi * self.radius**2)
    
    def calculate_perimeter(self):
        return round(math.pi * self.diameter)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        return self.length * self.length
    
    def calculate_perimeter(self):
        return 2 * self.length
    
class Triangle(Shape):
    def __init__(self, base, side2, side3, height):
        self.base = base
        self.side2 = side2
        self.side3 = side3
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def calculate_perimeter(self):
        return self.base + self.side2 + self.side3