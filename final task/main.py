from shapes import Circle, Rectangle, Triangle
from utils import get_valid_float, get_valid_index

def menu():
   print('1.Add new shape')
   print('2.List all shapes')
   print('3.Show shape details')
   print('4.Remove shape')
   print('5.Show sum of all areas')
   print('6.Show sum of all perimeters')
   print('7.Exit')

shapes_db = []

while True:
    menu()
    choice = input("Enter your choice (1-7): ")
    try:
        choice = int(choice)
    except ValueError:
        print('Invalid choice')
        continue
    if choice < 1 or choice > 7:
        print('Invalid choice')
        continue
    match choice:
        case 1:
            print('1.Circle 2.Rectangle 3.Triangle')
            figur = input('Enter your choice (1-3): ')
            try:
                figur = int(figur)
            except ValueError:
                print('Invalid choice')
                continue
            if figur < 1 or figur > 3:
                print('Invalid choice')
                continue
            color = input('Enter color: ')
            match figur:
                case 1:
                    radius = get_valid_float(input('Enter radius: '))
                    circle = Circle(color, radius)
                    shapes_db.append(circle)
                    print('Success: Shape added!')
                case 2:
                    width, height = map(int, input('Enter width: ').split())
                    try:
                        width, height = int(width), int(height)
                    except ValueError:
                        print('Invalid parameter')
                        continue
                    rectangle = Rectangle(color, width, height)
                    shapes_db.append(rectangle)
                    print('Success: Shape added!')
                case 3:
                    a, b, c = map(int, input('Enter side a: ').split())
                    try:
                        a, b, c = int(a), int(b), int(c)
                    except ValueError:
                        print('Invalid parameter')
                        continue
                    triangle = Triangle(color, a, b, c)
                    shapes_db.append(triangle)
                    print('Success: Shape added!')


