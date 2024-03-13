import skimage as ski
import simpleimageio as sio
from numpy import ndarray

def openImage(filePath: str):
    img: ndarray = ski.io.imread(filePath)
    if img.ndim == 4:
        img = img[0]  # Need the weird zero here for some reason with exr files
    image_grey = ski.color.rgb2gray(img)
    return image_grey

def writeImage(filePath: str, image: ndarray):
    # ski.io.imsave(filePath, image.astype('float32'), plugin='imageio', extension='.exr')
    ski.io.imshow(image)
    ski.io.show()
    sio.write(filePath, image)

