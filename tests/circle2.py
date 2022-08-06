#!/usr/bin/env python
import math

class Circle:
    """Circle class"""
    # count no of objects instantiated from this class
    __obj_count: int = 0   # class variable

    def __init__(self, circ: tuple, color: tuple) -> None:
        """ private instance variables"""
        self.__c = circ
        self.__cx = circ[0]
        self.__cy = circ[1]
        self.__radius = circ[2]
        self.__color = color
        self.__area = self.__radius * self.__radius * math.pi
        self.__circum = self.__radius * 2 * math.pi
        Circle.__obj_count += 1

    @classmethod
    def get_obj_count(cls) -> int:
        """class method"""
        return cls.__obj_count

    def get_center(self) -> tuple:
        return (self.__cx, self.__cy)

    def get_radius(self) -> float:
        return self.__radius

    def get_color(self) -> tuple:
        return self.__color

    def set_center(self, center: tuple) -> None:
        self.__cx = center[0]
        self.__cy = center[1]

    def set_radius(self, radius: float) -> None:
        self.__radius = radius

    def set_color(self, color: tuple) -> None:
        self.__color = color

    def __str__(self) -> str:
        s1: str = f"Circle: cx = {self.__cx}, cy = {self.__cy}"
        s2: str = f"radius = {self.__radius}, color = {self.__color}"
        return s1 + s2

    def draw_circle(self) -> None:
        print("drawing circle")

    def area_circle(self) -> float:
        return self.__area

    def circumference_circle(self) -> float:
        return self.__circum

if __name__ == "__main__":
    c1: Circle = Circle((10,10,7.3), (255,0,0))
    print(Circle.get_obj_count())
    print(c1)
    c1.draw_circle()
    area: float = c1.area_circle()
    circum: float = c1.circumference_circle()
    # create 5 Circle objects
    cl: list = []
    for k in range(5):
        c: Circle = Circle((20,20, 5.3), (255,0,255))
        cl.append(c)
    print(f"No of Circle objects instantiated: {Circle.get_obj_count()}")
    print(f"area   = {area:5.2f}")
    print(f"circum = {circum:5.2f}")
    print(f"center = {c1.get_center()}")
    print(f"radius = {c1.get_radius()}")
    print(f"color  = {c1.get_color()}")
    print(f"{cl}")
    c1.set_center((22,22))
    c1.set_radius(88)
    c1.set_color((0,255, 255))
    print(c1)
    print(f"Objects created  = {Circle.get_obj_count()}")