from .shape import Shape
# from shape import Shape

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        if width > 0 and height > 0:
            self._width = width
            self._height = height
        else:
            raise ValueError("Dimensions must be positive")
    def get_area(self):
        return self._width * self._height
    def get_perimeter(self):
        return 2 * (self._width + self._height)
    def __str__(self):
        return f'Rectangle ({self._color}) | {self._width} x {self._height}'

# rect = Rectangle("green", 10.0, 5.0)
# print(rect)
# print(f"Area: {rect.get_area():.2f}")
# print(f"Perimeter: {rect.get_perimeter():.2f}")