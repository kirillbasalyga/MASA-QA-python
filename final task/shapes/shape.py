import math

class Shape:
    def __init__(self, color:str):
        self._color = color
    def get_area(self):
        return 0.0
    def get_perimeter(self):
        return 0.0
    def __str__(self):
        return str(f'Shape (Color: {self._color})')
