#!/usr/bin/env python

import os
from src.html_generator import HtmlDoc
from src.svg_generator import SvgCanvas
from src.shape_generator import Circle, Rectangle, Ellipse


def main() -> None:

    # Define path to data directory
    data_path = os.path.join(os.path.dirname(__file__), 'data/')

    # Define canvas size
    canvas_w, canvas_h = 500, 300

    # Instantiate HtmlDoc and SvgCanvas classes
    hd: HtmlDoc = HtmlDoc(f"{data_path}/a21.html", "MyPart1")
    svg: SvgCanvas = SvgCanvas(w=canvas_w, h=canvas_h)
    circ: Circle = Circle(cx=100, cy=100, rad=50, red=0, green=0, blue=255, op=1)
    rect: Rectangle = Rectangle(x=0, y=0, width=100, height=50, red=0, green=255, blue=0, op=1)
    elli: Ellipse = Ellipse(cx=200, cy=200, rx=50, ry=100, red=255, green=0, blue=0, op=1)

    # Open html file
    hd.open_html_file()

    # Generate html template with an svg canvas
    hd.write_html_head()
    svg.write_svg_head(hd)

    circ.draw_circle_line(hd, 2)
    rect.draw_rect_line(hd, 2)
    elli.draw_ellipse_line(hd, 2)

    svg.write_svg_tail(hd)
    hd.write_html_tail()

    # Close html file
    hd.close_html_file()


if __name__ == "__main__":
    print(__doc__)
    main()
