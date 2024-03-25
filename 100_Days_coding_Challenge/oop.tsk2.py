"""calculating the area and perimeter of a square"""
class Square:
    def __init__(self, length):
        self.len = length
    def area (self):
        area = self.len * self.len
        return area
    def perimeter(self):
        peri = 4 * self.len
        return peri
    
square_1 = Square(10)
print(f'The area of the square 1 is: {square_1.area()}')
print(f"The perimeter of square 1 is: {square_1.perimeter()}")

square_2 = Square(25)
print(f'The area of the square 2 is: {square_2.area()}')
print(f"The perimeter of rectangle 1 is: {square_2.perimeter()}")


