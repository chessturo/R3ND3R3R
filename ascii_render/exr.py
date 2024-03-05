import skimage as ski
from numpy import ndarray

def openImage(filePath: str):
    img: ndarray = ski.io.imread(filePath)[0]  # Need the weird zero here for some reason?
    image_grey = ski.color.rgb2gray(img)
    return image_grey

def writeImage(filePath: str, image: ndarray):
    ski.io.imsave(filePath, image)

