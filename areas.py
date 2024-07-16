class Shape():
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width **2
def print_area(shape):
    print(f'The area of {type(shape).__name__} is {shape.area()}')

circle=Circle(1)
rectangle=Rectangle(2,3)
square=Square(4)

print_area(circle)
print_area(rectangle)
print_area(square)
