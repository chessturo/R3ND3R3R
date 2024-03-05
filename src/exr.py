import skimage as ski
from numpy import ndarray


def openImage(filePath: str):
    image: ndarray = ski.io.imread(filePath)[0]  # Need the weird zero here for some reason?
    image_grey = ski.color.rgb2gray(image)
    return image_grey


openImage('../test/Lightmap-0_comp_light.exr')
