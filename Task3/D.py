class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calculate_area(self):
        length = abs(self.point1.x - self.point2.x)
        width = abs(self.point1.y - self.point2.y)
        return length * width

def compare_areas(rectangle1, rectangle2):
    area1 = rectangle1.calculate_area()
    area2 = rectangle2.calculate_area()
    if area1 == area2:
        return "Площади равны"
    elif area1 > area2:
        return "Первая фигура больше по площади"
    else:
        return "Вторая фигура больше по площади"

def check_intersection(rectangle1, rectangle2):
    x_overlap = not (rectangle1.point2.x < rectangle2.point1.x or rectangle2.point2.x < rectangle1.point1.x)
    y_overlap = not (rectangle1.point2.y < rectangle2.point1.y or rectangle2.point2.y < rectangle1.point1.y)
    return x_overlap and y_overlap

class Square(Rectangle):
    def __init__(self, point1, point2):
        super().__init__(point1, point2)
        self.check_square()

    def check_square(self):
        if abs(self.point1.x - self.point2.x) != abs(self.point1.y - self.point2.y):
            raise ValueError("Одна из фигур должна быть квадратом")

# Пример использования:

try:
    point_a = Point(0, 0)
    point_b = Point(3, 3)
    point_c = Point(2, 2)
    point_d = Point(5, 5)

    square1 = Square(point_a, point_b)  # Используем квадрат вместо прямоугольника
    rectangle2 = Rectangle(point_c, point_d)

    intersection_result = check_intersection(square1, rectangle2)
    areas_comparison = compare_areas(square1, rectangle2)

    print("Пересекаются" if intersection_result else "Не пересекаются")
    print(areas_comparison)

except ValueError as ve:
    print(f"Ошибка: {ve}")
except Exception as e:
    print(f"Ошибка: {e}")
