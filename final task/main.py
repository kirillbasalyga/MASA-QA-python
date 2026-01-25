from shapes import Circle, Rectangle, Triangle
from utils import get_valid_float, get_valid_index
# import json
import pickle

def menu():
   print('1.Add new shape')
   print('2.List all shapes')
   print('3.Show shape details')
   print('4.Remove shape')
   print('5.Show sum of all areas')
   print('6.Show sum of all perimeters')
   print('7.Exit')
   print('8.Save to file')
   print('9. Load from file')
   print('10. ADD preset figures')

shapes_db = []

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-10): ")
        try:
            choice = int(choice)
        except ValueError:
            print('Invalid choice')
            continue
        if choice < 1 or choice > 10:
            print('Invalid choice')
            continue
        try:
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
                                radius = get_valid_float('Enter radius: ')
                                circle = Circle(color, radius)
                                shapes_db.append(circle)
                                print('Success: Shape added!')
                            case 2:
                                width, height = map(int, input('Enter width and height: ').split())
                                try:
                                    width, height = int(width), int(height)
                                except ValueError:
                                    print('Invalid parameter')
                                    continue
                                rectangle = Rectangle(color, width, height)
                                shapes_db.append(rectangle)
                                print('Success: Shape added!')
                            case 3:
                                a, b, c = map(int, input('Enter sides a, b, c: ').split())
                                try:
                                    a, b, c = int(a), int(b), int(c)
                                except ValueError:
                                    print('Invalid parameter')
                                    continue
                                triangle = Triangle(color, a, b, c)
                                shapes_db.append(triangle)
                                print('Success: Shape added!')

                case 2:
                    if not shapes_db:
                        print( f"\nList is empty\n")
                    else:
                        print(f'\n---------- ALL SHAPES ----------\n')
                        for index, shape in enumerate(shapes_db, start=1):
                            print (f'{index}. {shape}')
                        print(f'\n--------------------------------\n')
                case 3:
                    if not shapes_db:
                        print(f"\nList is empty\n")
                    else:
                        print(f'---------- SHAPE DETAILS ----------')
                        a = len(shapes_db)
                        idx = get_valid_index('Enter shape number: ', a)
                        shape = shapes_db[idx]
                        print(f'------------------------------')
                        print(f'Info: {shape}')
                        print(f'Area: {shape.get_area():.2f}')
                        print(f'Perimeter: {shape.get_perimeter():.2f}')
                        print(f'------------------------------')
                case 4:
                     if not shapes_db:
                        print(f"\nList is empty\n")
                     else:
                         print(f'---------- REMOVE SHAPE ----------')
                         idx = get_valid_index(input('Enter shape number: '), len(shapes_db))
                         removed = shapes_db.pop(idx)
                         print(f'Success: Removed {removed}')
                case 5:
                    if not shapes_db:
                        print(f"\nList is empty\n")
                    else:
                        total = sum(s.get_area() for s in shapes_db)
                        print(f'\nTotal areas of {len(shapes_db)} shapes: {total}\n')
                case 6:
                    if not shapes_db:
                        print(f"\nList is empty\n")
                    else:
                        total = sum(s.get_perimeter() for s in shapes_db)
                        print(f'\nTotal Perimeter of {len(shapes_db)} shapes: {total}\n')
                case 7:
                    print('Goodbye!')
                    break
                case 8:
                    with open('shape.pickle', 'wb') as f:
                        pickle.dump(shapes_db, f)
                case 9:
                    with open('shape.pickle', 'rb') as f:
                        shapes_db1 = pickle.load(f)
                        for shape in shapes_db1:
                            print(f'{shape}')

                case 10:
                    circle = Circle("blue", 5.0)
                    rect = Rectangle("green", 10.0, 5.0)
                    triangle = Triangle("yellow", 3, 4, 5)
                    shapes_db.append(circle)
                    shapes_db.append(rect)
                    shapes_db.append(triangle)
        except ValueError as e:
            print(f'{e}')
            continue

if __name__ == "__main__":
    main()




