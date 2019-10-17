import numpy as np
import matplotlib.image as mpimg

def mirrorH(path):
    image = mpimg.imread(path)
    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = image[i][len(image[i]-j)]
    return image

