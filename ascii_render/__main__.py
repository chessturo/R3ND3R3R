import sys

import monobit
from monobit.streams import Stream
from monobit.formats.text.yaff import load_yaff

from .exr import openImage, writeImage
from .fontToMap import FontMap
from .imageProcessing import apply_approximation

debug = True

image = openImage(sys.argv[1])
# font = FontMap(sys.argv[2])
# font = load_yaff(Stream(open(sys.argv[2], 'r'), 'r'))
font = monobit.load(sys.argv[2]).get()
lines = apply_approximation(image, font)
if debug:
    import functools
    text = functools.reduce(lambda x, y: x + y, lines)
    f = open('test/output.txt', 'wb')
    f.write(text.encode())
writeImage(sys.argv[3], image)
