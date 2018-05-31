# Q4.

class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
        print(self.length * self.breadth)

class Rectangle(Shape):
    pass


class Square(Shape):
    pass


print("Area of rectangle:",end=' ')
rect=Rectangle(4,8)
rect.Area()
print("Area of Square:",end=' ')
sq=Square(20,20)
sq.Area()

'''
OUTPUT:
Area of rectangle: 32
Area of Square: 400
'''