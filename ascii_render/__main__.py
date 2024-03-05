import sys
from .exr import openImage
from .fontToMap import create_arrays

image = openImage(sys.argv[1])
font = create_arrays(sys.argv[2])