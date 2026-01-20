import math
from .shape import Shape

class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        elif (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Invalid triangle! Sum of two sides must be > third.")
        self._a = a
        self._b = b
        self._c = c
    def get_perimeter(self):
        return self._a + self._b + self._c
    def get_area(self):
        s = self.get_perimeter() / 2
        S = math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))
        return S
    def __str__(self):
        return f'Triangle ({self._color}) | Sides: {self._a} {self._b} {self._c}'

# triangle = Triangle("yellow", 3, 4, 5)
# print(triangle)
# print(f"Area: {triangle.get_area():.2f}")
# print(f"Perimeter: {triangle.get_perimeter():.2f}")
# triangle = Triangle("blue", 5, 5, 5)
# print(triangle)
# print(f"Area: {triangle.get_area():.2f}")
# print(f"Perimeter: {triangle.get_perimeter():.2f}")
# try:
#     triangle = Triangle("red", 2, 3, 5)  # 2+3=5, НЕ больше 5!
# except ValueError as e:
#     print(e)
#
# try:
#     triangle = Triangle("red", 1, 2, 10)
# except ValueError as e:
#     print(e)
