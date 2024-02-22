class Rectangle:
    def __init__(self, identifier, width, height):
        self.identifier = identifier
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square:
    def __init__(self, identifier, side_length):
        self.identifier = identifier
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

def is_intersect(t1, t2):
    if (
        (t1.width >= t2.side_length and t1.height >= t2.side_length) or
        (t2.side_length >= t1.width and t2.side_length >= t1.height)
    ):
        return True
    else:
        return False

def compare(t1, t2):
    area_t1 = t1.area()
    area_t2 = t2.area()

    if area_t1 < area_t2:
        return -1
    elif area_t1 == area_t2:
        return 0
    else:
        return 1

x_rectangle = int(input("Введите ширину прямоугольника: "))
y_rectangle = int(input("Введите высоту прямоугольника: "))
a_square = int(input("Введите длину стороны квадрота: "))

rectangle = Rectangle("Прямоугольник", x_rectangle, y_rectangle)
square = Square("Квадрат", a_square)

if is_intersect(rectangle, square):
    print(f"{rectangle.identifier} и {square.identifier} пересекаются.")
else:
    print(f"{rectangle.identifier} и {square.identifier} не пересекаются.")

result = compare(rectangle, square)
if result < 0:
    print(f"{rectangle.identifier} меньше по площади чем {square.identifier}.")
elif result == 0:
    print(f"{rectangle.identifier} и {square.identifier} имеют равную площадь.")
else:
    print(f"{rectangle.identifier} больше по площади чем {square.identifier}.")
