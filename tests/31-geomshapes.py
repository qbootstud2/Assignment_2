import math


class Point:
    """
    >>> p1 = Point()
    >>> p2 = Point(3, 4)
    >>> p3 = Point(-12.2, 101)
    >>> p1
    Point(0, 0)
    >>> p2
    Point(3, 4)
    >>> p3
    Point(-12.2, 101)
    >>> li = [p3, Point(3)]
    >>> li
    [Point(-12.2, 101), Point(3, 0)]
    >>> p4 = p1.move_x(10)
    >>> p5 = p1.move_y(-10)
    >>> p4
    Point(10, 0)
    >>> p5
    Point(0, -10)
    >>> p1
    Point(0, 0)
    >>> p4 = p1.move(5, -5)
    >>> p4
    Point(5, -5)
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def move_x(self, d):
        return Point(self.x + d, self.y)

    def move_y(self, d):
        return Point(self.x, self.y + d)

    def move(self, d_x, d_y):
        return Point(self.x + d_x, self.y + d_y)


class Circle:
    """
    >>> p1 = Point()
    >>> c1 = Circle(p1, 10)
    >>> c1
    Circle(Point(0, 0), 10)
    >>> c2 = c1.move(-3.14, +12.2)
    >>> c1
    Circle(Point(0, 0), 10)
    >>> c2
    Circle(Point(-3.14, 12.2), 10)
    >>> c1.perimeter()
    62.83185307179586
    >>> c1.area()
    314.1592653589793
    >>> c2.perimeter()
    62.83185307179586
    >>> c2.area()
    314.1592653589793
    """
    def __init__(self, c, r):
        self.c = c
        self.r = r

    def __repr__(self):
        return "Circle(%r, %r)" % (self.c, self.r)

    def move(self, d_x, d_y):
        return Circle(Point(self.c.x + d_x,
            self.c.y + d_y), self.r)

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * (self.r ** 2)
