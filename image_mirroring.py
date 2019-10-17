import numpy as np
import matplotlib.image as mpimg

def mirrorH(path):
    image = mpimg.imread(path)
    x=0
    for i in image:
        for j in range(len(image[0])+1,-1):
            image[i][j] = image[i][x]
            x+=1
            if x > len(image[i]):
                x=0
    return image

