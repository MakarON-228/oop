import tkinter as tk
root = tk.Tk()

class Dot():
    def __init__(self, canvas, x, y, radius = 5, color = "#000000"):
        self.x = x
        self.y = y
        self.rad = radius
        self.color = color
        self._canvas = canvas
        self._draw()

    def connect_with_line(self, dot, color = "#000000", width = 1):
        if self._canvas != dot._canvas:
            raise Exception(f"Точки принадлежат разным Canvas")

        self._canvas.create_line(self.x, self.y, dot.x, dot.y, fill = color, width = width)

    def _draw(self):
        hrad = self.rad / 2
        self._canvas.create_oval(self.x - hrad, self.y - hrad, self.x + hrad, self.y + hrad, fill=self.color)

    def __str__(self):
        return f"Dot(X={self.x}, Y={self.y})"

    def __repr__(self):
        return str(self)


class Line():
    def __init__(self, canvas, x1, y1, x2, y2, color = "#000000", width = 1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width
        self._canvas = canvas
        self._draw()


    def _draw(self):
        self._canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=self.width)

    def __str__(self):
        return f"Line(X1={self.x1}, Y1={self.y1}; X2={self.x2}, Y2={self.y2})"

    def __repr__(self):
        return str(self)


class Rectangle():
    def __init__(self, canvas, x1, y1, x2, y2, color = "#000000"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self._canvas = canvas
        self._draw()

    def _draw(self):
        self._canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)

    def __str__(self):
        return f"Rectangle(X1={self.x1}, Y1={self.y1}; X2={self.x2}, Y2={self.y2})"

    def __repr__(self):
        return str(self)


class Oval(Rectangle):
    def _draw(self):
        self._canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.color)

    def __str__(self):
        return f"Oval(X1={self.x1}, Y1={self.y1}; X2={self.x2}, Y2={self.y2})"


canv = tk.Canvas(root, width=400, height=400)

A = Dot(canvas=canv, x=50, y=50, color="red")
B = Dot(canvas=canv, x=100, y=100, color="blue", radius=10)
C = Dot(canvas=canv, x=150, y=45, color="green", radius=7)
print(str(A))

A.connect_with_line(dot=B)
B.connect_with_line(dot=C, color="#555555")
C.connect_with_line(A)

median = Line(canvas=canv, x1 = A.x, y1 = A.y, x2 = (B.x + C.x) / 2, y2 = (B.y + C.y) / 2, color="purple", width=2)
print(str(median))

rect1 = Rectangle(canv, 200, 200, 350, 250, color="red")
oval1 = Oval(canv, 100, 300, 200, 370, color="yellow")
print(rect1, oval1, sep='\n')

canv.pack(fill="both", expand=True)

root.mainloop()