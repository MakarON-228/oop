"""Shape"""
class Shape:
    def __init__(self, list_of_sides):
        self.list_of_sides = list_of_sides
        self.validate_input()
        self.validate_figure()
        self.perimeter = self.get_perimeter()

    def validate_figure(self):
        if len(self.list_of_sides) < 3:
            raise Exception("Требуется определить фигуру")

    def validate_input(self):
        for i in self.list_of_sides:
            if i <= 0:
                raise ValueError("Данные не имеют смысла")

    def get_perimeter(self):
        return sum(self.list_of_sides)

    def get_area(self):
        raise Exception("Нет сведений о фигуре")

    def __str__(self):
        return f"Shape(P={self.perimeter})"

    def __repr__(self):
        return str(self)

shape = Shape([1, 2, 3, 4, 5])
print(shape.perimeter, str(shape))

# wrong_shape = Shape([1, 2])
# print(shape.get_area())


"""Triangle"""

class Triangle(Shape):
    def __init__(self, list_of_sides):
        super().__init__(list_of_sides)
        self.a = self.list_of_sides[0]
        self.b = self.list_of_sides[1]
        self.c = self.list_of_sides[2]
        self.area = self.get_area()

    def validate_figure(self):
        if len(self.list_of_sides) != 3:
            raise ValueError("Нужно 3 стороны списком")
        a = self.list_of_sides[0]
        b = self.list_of_sides[1]
        c = self.list_of_sides[2]
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Такого треугольника не существует")


    def get_area(self):
        hp = self.perimeter / 2
        return (hp * (hp - self.a) * (hp - self.b) * (hp - self.c)) ** 0.5

    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c}, P={self.perimeter}, Ar={self.area})"

triangle = Triangle([3, 4, 5])
print(str(triangle))

# wrong_triangle = Triangle([-3, 4, 5])


"""Rectangle"""

class Rect(Shape):
    def __init__(self, list_of_sides):
        super().__init__(list_of_sides)
        self.W = self.list_of_sides[0]
        self.H = self.list_of_sides[1]
        self.area = self.get_area()

    def validate_figure(self):
        if len(self.list_of_sides) != 2:
            raise ValueError("Нужно 2 стороны списком")

    def get_perimeter(self):
        return sum(self.list_of_sides) * 2

    def get_area(self):
        return self.W * self.H

    def __str__(self):
        return f"Rectangle(Height={self.H}, Weighth={self.W}, P={self.perimeter}, Ar={self.area})"

rect = Rect([3, 5])
print(str(rect))

# wrong_rect = Rect([3, 6, 4])


"""Square"""

class Square(Shape):
    def __init__(self, list_of_sides):
        super().__init__(list_of_sides)
        self.side = self.list_of_sides[0]
        self.area = self.get_area()
        self.diameter = (self.side ** 2 * 2) ** 0.5


    def validate_figure(self):
        if len(self.list_of_sides) != 1:
            raise ValueError("Нужна 1 сторона списком")

    def get_perimeter(self):
        return self.list_of_sides[0] * 4

    def get_area(self):
        return self.list_of_sides[0] ** 2

    def __str__(self):
        return f"Square(side={self.side}, P={self.perimeter}, Ar={self.area}, diameter={self.diameter})"

square = Square([5])
print(str(square))

# wrong_square = Square([5, 5])


"""Circle"""

class Circle(Shape):
    def __init__(self, list_of_sides):
        super().__init__(list_of_sides)
        self.radius = self.list_of_sides[0]
        self.area = self.get_area()


    def validate_figure(self):
        if len(self.list_of_sides) != 1:
            raise ValueError("Нужен только радиус в списке")

    def get_perimeter(self):
        return 2 * 3.1415 * self.list_of_sides[0]

    def get_area(self):
        return 3.141 * (self.list_of_sides[0]) ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, P={self.perimeter}, Ar={self.area})"

circle = Circle([6])
print(str(circle))

# wrong_circle = Circle([0])




