import numpy as np
import matplotlib as mp

def mirror(path):
    image = mp.image.imread(path)
    flipped = np.fliplr(image)
    return flipped
    