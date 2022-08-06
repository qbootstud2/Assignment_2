from src.html_generator import HtmlDoc


class Circle:
    """ This class holds the characteristic values of a circle and it provides methods to generate and draw
    an SVG line """

    def __init__(self, cx: int, cy: int, rad: int, red: int, green: int, blue: int, op: float) -> None:
        """shorten parameter list with namedtuples"""
        self.__cx: int = cx
        self.__cy: int = cy
        self.__rad: int = rad
        self.__red: int = red
        self.__green: int = green
        self.__blue: int = blue
        self.__op: float = op

    def draw_circle_line(self, hd: HtmlDoc, t: int) -> None:
        """draw_circle_line method"""
        line1: str = f'<circle cx="{self.__cx}" cy="{self.__cy}" r="{self.__rad}" '
        line2: str = f'fill="rgb({self.__red}, {self.__green}, {self.__blue})" '
        line3: str = f'fill-opacity="{self.__op}"></circle>'
        hd.write_html_line(t, line1 + line2 + line3)


class Rectangle:
    """ This class holds the characteristic values of a rectangle and it provides methods to generate and draw
    an SVG line """

    def __init__(self, x: int, y: int, width: int, height: int, red: int, green: int, blue: int, op: float) -> None:
        """shorten parameter list with namedtuples"""
        self.__x: int = x
        self.__y: int = y
        self.__width: int = width
        self.__height: int = height
        self.__red: int = red
        self.__green: int = green
        self.__blue: int = blue
        self.__op: float = op

    def draw_rect_line(self, hd: HtmlDoc, t: int) -> None:
        """draw_rect_line method"""
        line1: str = f'<rect x="{self.__x}" y="{self.__y}" '
        line2: str = f'width="{self.__width}" height="{self.__height}" '
        line3: str = f'fill="rgb({self.__red}, {self.__green}, {self.__blue})" '
        line4: str = f'fill-opacity="{self.__op}"></rect>'
        hd.write_html_line(t, line1 + line2 + line3 + line4)


class Ellipse:
    """ This class holds the characteristic values of a ellipse and it provides methods to generate and draw
    an SVG line """

    def __init__(self, cx: int, cy: int, rx: int, ry: int, red: int, green: int, blue: int, op: float) -> None:
        """shorten parameter list with namedtuples"""
        self.__cx: int = cx
        self.__cy: int = cy
        self.__rx: int = rx
        self.__ry: int = ry
        self.__red: int = red
        self.__green: int = green
        self.__blue: int = blue
        self.__op: float = op

    def draw_ellipse_line(self, hd: HtmlDoc, t: int) -> None:
        """draw_ellipse_line method"""
        line1: str = f'<ellipse cx="{self.__cx}" cy="{self.__cy}" rx="{self.__rx}" ry="{self.__ry}" '
        line2: str = f'fill="rgb({self.__red}, {self.__green}, {self.__blue})" '
        line3: str = f'fill-opacity="{self.__op}"></ellipse>'
        hd.write_html_line(t, line1 + line2 + line3)


class ArtConfig:
    """ This class defines ranges for an art style (e.g. big and small shapes, constrained colors, shapes,
    pointillistic style, fall style, ... """

    # Define counter
    counter = 0

    # Define default ranges for the shape's parameters
    rad_min, rad_max = 0, 100
    rx_min, rx_max = 10, 30
    ry_min, ry_max = 10, 30
    w_min, w_max = 10, 100
    h_min, h_max = 10, 100
    red_min, red_max = 0, 255
    green_min, green_max = 0, 255
    blue_min, blue_max = 0, 255
    o_min, o_max = 0.0, 1.0

    def __init__(self,
                 shape: bool,
                 x: int,
                 y: int,
                 rad: int = 20,
                 rx: int = 20,
                 ry: int = 20,
                 w: int = 40,
                 h: int = 20,
                 red: int = 255,
                 green: int = 0,
                 blue: int = 0,
                 op: float = 0.8
                 ) -> None:
        ArtConfig.counter += 1
        self.__shape: int = shape
        self.__x: int = x
        self.__y: int = y
        self.__rad: int = rad
        self.__rx: int = rx
        self.__ry: int = ry
        self.__w: int = w
        self.__h: int = h
        self.__red: int = red
        self.__green: int = green
        self.__blue: int = blue
        self.__op: float = op
