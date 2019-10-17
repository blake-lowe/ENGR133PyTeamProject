import numpy as np
import matplotlib.image as mpimg


def mirrorH(path):
    image = mpimg.imread(path)
    outimage = image
    for i in range(len(image)):
        for j in range(len(image[i])):
            outimage[i][j] = image[i][-j]
            outimage[i][-j] = image[i][j]
    
    return outimage

