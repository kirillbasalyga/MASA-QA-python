class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    def __str__(self) -> str:
        return f"Rectangle {self.__width}x{self.__height}"

    def __add__(self, other: 'Rectangle'):
        return self.__width * self.__height + other.__width * other.__height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if value <= 0:
            print(f'Can not be less than or equal to 0')

    @height.setter
    def height(self, value):
        if value <= 0:
            print(f'Can not be less than or equal to 0')

rect1 = Rectangle(5, 4)
rect2 = Rectangle(10, 2)
print(rect1)
print(rect1 + rect2)
rect1.width = -5

