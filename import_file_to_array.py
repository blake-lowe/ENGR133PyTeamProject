import matplotlib.image as mpimg
import numpy as np

## Takes a file path and returns the array form of the image
def importImage(path): ## Where path is the file path as a string
    image = mpimg.imread(path) 
    return image

