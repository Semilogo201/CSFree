class Circle:
    pi = 3.142  # Class Object Attribute

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.pi * self.radius * self.radius

    def get_circumference(self):
        return 2 * self.pi * self.radius


circle_1 = Circle(4)
print(f"The circumference of circle 1 is: {circle_1.get_circumference()}")   
print(f"The area of circle 1 is: {circle_1.get_area()}")
circle_2 = Circle(14)
print(f"The circumference of circle 2 is: {circle_2.get_circumference()}") 
print(f"The area of circle 2 is: {circle_2.get_area()}") 
