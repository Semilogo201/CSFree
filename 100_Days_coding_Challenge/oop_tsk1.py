"""A code that uses oop to calculate the perimeter and area of a rectangle"""
class Rectangle:

    def __init__(self, len, bre):
        self.length = len 
        self.bredth = bre
    def get_area(self):
        area = self.length * self.bredth
        return area
    def get_perimeter(self):
        peri = int(2 * (self.length + self.bredth))
        return peri
    
        
        
rectangle_1 = Rectangle(5, 5)
print(f'The area of the rectangle 1 is: {rectangle_1.get_area()}')
print(f"The perimeter of rectangle 1 is: {rectangle_1.get_perimeter()}")

rectangle_2 = Rectangle(8, 20)
print(f'The area of the rectangle 1 is: {rectangle_2.get_area()}')
print(f"The perimeter of rectangle 1 is: {rectangle_2.get_perimeter()}")























































































































