from .shape import Shape
# import math
class Circle(Shape):
    def __init__(self, color, radius) -> None:
        super().__init__(color)
        if radius <= 0:
            raise ValueError('radius must be positive')
        self._radius = radius
    def get_area(self):
        return math.pi * self._radius**2
    def get_perimeter(self):
        return 2 * math.pi * self._radius
    def __str__(self):
        return f'Circle ({self._color}) | R: { self._radius}'

# circle = Circle("blue", 4)
# print(circle)
# print(f"Area: {circle.get_area():.2f}")
# print(f"Perimeter: {circle.get_perimeter():.2f}")
#
# try:
#     circle = Circle("red", -3)
# except ValueError as e:
#     print(e)