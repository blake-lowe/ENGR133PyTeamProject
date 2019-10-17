import numpy as np
import matplotlib.image as mpimg


def mirrorH(path):
    image = mpimg.imread(path)
    outimage = image
    for i in range(0,len(image)):
        for j in range(0,len(image[i])//2):
            outimage[i][j] = image[i][-j]
        for j in range():
            outimage[i][-j] = image[i][j]
    return outimage