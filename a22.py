#!/usr/bin/env python

import os
from src.shape_generator import ArtConfig
from src.random_generator import GenRandom
from src.utils import build_header


def main() -> None:

    # Define path to data directory
    data_path = os.path.join(os.path.dirname(__file__), 'data/')

    # Define some parameters
    n_shapes = 10                   # number of objects do draw
    canvas_w, canvas_h = 500, 300   # canvas size

    # Generate table of parameters
    params = ['CNT', 'SHA', 'X', 'Y', 'RAD', 'RX', 'RY', 'W', 'H', 'R', 'G', 'B', 'OP']

    # Build table header
    header = build_header(params, space=5)

    # Generate table of random numbers
    with open(f"{data_path}/a22.txt", 'w') as writer:

        # Write header
        writer.write(header)

        for i in range(n_shapes):
            cnt = i + 1
            shape = GenRandom.gen_int_in_range(0, 2)
            x = GenRandom.gen_int_in_range(0, canvas_w)
            y = GenRandom.gen_int_in_range(0, canvas_h)
            rad = GenRandom.gen_int_in_range(ArtConfig.rad_min, ArtConfig.rad_max)
            rx = GenRandom.gen_int_in_range(ArtConfig.rx_min, ArtConfig.rx_max)
            ry = GenRandom.gen_int_in_range(ArtConfig.ry_min, ArtConfig.ry_max)
            w = GenRandom.gen_int_in_range(ArtConfig.w_min, ArtConfig.w_max)
            h = GenRandom.gen_int_in_range(ArtConfig.h_min, ArtConfig.h_max)
            red = GenRandom.gen_int_in_range(ArtConfig.red_min, ArtConfig.red_max)
            green = GenRandom.gen_int_in_range(ArtConfig.green_min, ArtConfig.green_max)
            blue = GenRandom.gen_int_in_range(ArtConfig.blue_min, ArtConfig.blue_max)
            op = GenRandom.gen_float_in_range(ArtConfig.o_min, ArtConfig.o_max)

            line = f"{cnt : >5}{shape : >5}{x : >5}{y : >5}{rad : >5}{rx : >5}{ry : >5}" + \
                   f"{w : >5}{h : >5}{red : >5}{green : >5}{blue : >5}{op : >5}\n"

            writer.write(line)


if __name__ == "__main__":
    print(__doc__)
    main()
