#!/usr/bin/env python3


import os
import sys

file = os.path.expanduser( sys.argv[1] )


import src.png_reader as pr

with pr.PngReader(file) as reader:
    for len, tp, data, crc in reader:
        print(f"{len:07}, {tp}, {crc}")
