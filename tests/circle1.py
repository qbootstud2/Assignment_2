#!/usr/bin/env python
"""Exploring Circle class"""
import math

class Circle:
    """Circle class"""
    def __init__(self, circ: tuple, color: tuple):
        self.__c = circ
        self.__cx = circ[0]
        self.__cy = circ[1]
        self.__radius = circ[2]
        self.__color = color

    def __str__(self) -> str:
        s1: str = f"Circle: cx = {self.__cx}, cy = {self.__cy}"
        s2: str = f"radius = {self.__radius}, color = {self.__color}"
        return s1 + s2

    def draw(self) -> None:
        print("Drawing: center, radius, color")  # draw SVG in Assignment

    def area(self) -> float:
        return self.__radius * self.__radius * math.pi

    def circumference(self) -> float:
        return 2.0 * self.__radius * math.pi


def main() -> None:
    c1: Circle = Circle((10,10, 7.3), (255,0,0))
    print(f"Object: {c1.__str__()}")
    c1.draw()
    print(f"Area = {c1.area():.2f}")
    print(f"Circumference = {c1.circumference():.2f}")

main()