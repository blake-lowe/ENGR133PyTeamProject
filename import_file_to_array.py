import matplotlib.image as mpimg
import numpy as np

def importImage(path):
    image = mpimg.imread(path) #Where path is the file path as a string
    return image

