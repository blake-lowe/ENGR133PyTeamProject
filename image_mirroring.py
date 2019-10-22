import numpy as np
import matplotlib.image as mpimg


def mirrorH(path):
    image = mpimg.imread(path)
    for i in range(0,len(image)):
        for j in range(0,len(image[i])):
            image[i][j],image[i][-j-1] = image[i][-j-1],image[i][j]

    return image     
 