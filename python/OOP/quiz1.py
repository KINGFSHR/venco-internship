import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius*2

    def calculate_area(self):
        return round(math.pi * self.radius**2)
    
    def calculate_perimeter(self):
        return round(math.pi * self.diameter)

radius = float(input("Enter circle's radius: "))
circle = Circle(radius)

print("Area: ", circle.calculate_area(), "\n" "Perimeter: ", circle.calculate_perimeter())
