import sys
from .exr import openImage, writeImage
from .fontToMap import create_arrays
from .imageProcessing import applyApproximation

image = openImage(sys.argv[1])
font = create_arrays(sys.argv[2])
applyApproximation(image, font)
writeImage(sys.argv[3], image)