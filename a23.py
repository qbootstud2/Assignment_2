#!/usr/bin/env python

import os
from src.html_generator import HtmlDoc
from src.svg_generator import SvgCanvas
from src.shape_generator import Circle, Rectangle, Ellipse, ArtConfig
from src.random_generator import GenRandom


def main() -> None:

    # Define path to data directory
    data_path = os.path.join(os.path.dirname(__file__), 'data/')

    # Define some parameters
    n_shapes = 400                  # number of objects to draw
    canvas_w, canvas_h = 600, 300   # canvas size

    # Instantiate HtmlDoc and SvgCanvas classes
    hd: HtmlDoc = HtmlDoc(f"{data_path}/a2-33.html", "Merry Christmas")
    svg: SvgCanvas = SvgCanvas(w=canvas_w, h=canvas_h)

    # Open html file
    hd.open_html_file()

    # Generate html template with an svg canvas
    hd.write_html_head()
    svg.write_svg_head(hd)

    # Generate random shapes
    for i in range(n_shapes):
        shape = GenRandom.gen_int_in_range(0, 2)
        x = GenRandom.gen_int_in_range(0, canvas_w)
        y = GenRandom.gen_int_in_range(0, canvas_h)
        red = GenRandom.gen_int_in_range(ArtConfig.red_min, ArtConfig.red_max)
        green = GenRandom.gen_int_in_range(ArtConfig.green_min, ArtConfig.green_max)
        blue = GenRandom.gen_int_in_range(ArtConfig.blue_min, ArtConfig.blue_max)
        op = GenRandom.gen_float_in_range(ArtConfig.o_min, ArtConfig.o_max)

        if shape == 0:
            # Generate specific parameters of circle
            rad = GenRandom.gen_int_in_range(ArtConfig.rad_min, ArtConfig.rad_max)

            # Draw circle
            Circle(cx=x, cy=y, rad=rad, red=red, green=green, blue=blue, op=op).draw_circle_line(hd, 2)
        elif shape == 1:
            # Generate specific parameters of rectangle
            w = GenRandom.gen_int_in_range(ArtConfig.w_min, ArtConfig.w_max)
            h = GenRandom.gen_int_in_range(ArtConfig.h_min, ArtConfig.h_max)

            # Draw rectangle
            Rectangle(x=x, y=y, width=w, height=h, red=red, green=green, blue=blue, op=op).draw_rect_line(hd, 2)
        elif shape == 2:
            # Generate specific parameters of ellipse
            rx = GenRandom.gen_int_in_range(ArtConfig.rx_min, ArtConfig.rx_max)
            ry = GenRandom.gen_int_in_range(ArtConfig.ry_min, ArtConfig.ry_max)

            # Draw ellipse
            Ellipse(cx=x, cy=y, rx=rx, ry=ry, red=red, green=green, blue=blue, op=op).draw_ellipse_line(hd, 2)
        else:
            raise ValueError('A shape must be specified')

    svg.write_svg_tail(hd)
    hd.write_html_tail()

    # Close html file
    hd.close_html_file()


if __name__ == "__main__":
    print(__doc__)
    main()
