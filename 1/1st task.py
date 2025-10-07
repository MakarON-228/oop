class Shape:
    def __init__(self, list_of_sides, is_oval = False):
        self.list_of_sides = list_of_sides
        self.is_oval = is_oval

    def get_perimeter(self):
        return sum(self.list_of_sides)



class Triangle(Shape):
    def __init__(self, list_of_sides, is_oval):
        super().__init__(list_of_sides, is_oval)
        self.validate_sides()
        self.a = self.list_of_sides[0]
        self.b = self.list_of_sides[1]
        self.c = self.list_of_sides[2]
        self.perimeter = self.get_perimeter()
        half_p = self.perimeter
        self.area = (half_p*(half_p-self.a)*(half_p-self.b)*(half_p-self.c))**0.5


    def validate_sides(self):
        if self.is_oval:
            raise ValueError("Вы делаете круг")
        if len(self.list_of_sides) != 3:
            raise ValueError("Нужно 3 стороны списком")
        a = self.list_of_sides[0]
        b = self.list_of_sides[1]
        c = self.list_of_sides[2]
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Некорректно заданы стороны")


class Rect(Shape):
    def __init__(self, list_of_sides, is_oval):
        super().__init__(list_of_sides, is_oval)
        self.validate_sides()
        self.W = self.list_of_sides[0]
        self.H = self.list_of_sides[1]
        self.perimeter = (self.H + self.W) * 2
        self.area = self.W * self.H

    def validate_sides(self):
        if self.is_oval:
            raise ValueError("Вы делаете круг")
        if len(self.list_of_sides) != 2:
            raise ValueError("Нужно 2 стороны списком")

class Square(Shape):
    def __init__(self, list_of_sides, is_oval):
        super().__init__(list_of_sides, is_oval)
        self.validate_sides()
        self.side = self.list_of_sides[0]
        self.perimeter = self.side * 4
        self.area = self.side ** 2

    def validate_sides(self):
        if self.is_oval:
            raise ValueError("Вы делаете круг")
        if len(self.list_of_sides) != 1:
            raise ValueError("Нужно 1 сторона списком")

class Circle(Shape):
    def __init__(self, list_of_sides, is_oval):
        super().__init__(list_of_sides, is_oval)
        self.validate_circle()
        radius = self.list_of_sides[0]
        self.perimeter = 2 * 3.14 * radius
        self.area = 3.14 * radius**2

    def validate_circle(self):
        if self.is_oval == False or len(self.list_of_sides) != 1:
            raise ValueError("Данные некорректны для круга")

shape = Shape([1, 2, 3, 4, 5])
print("shape perimeter", shape.get_perimeter())

triangle = Triangle([3, 4, 5])
print("triangle perimeter and area", triangle.perimeter, triangle.area)


circle = Circle([5], True)
print("circle perimeter and area", circle.perimeter, circle.area)



