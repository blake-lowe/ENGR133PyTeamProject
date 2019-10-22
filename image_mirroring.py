import numpy as np


 
def mirrorH(image):
    outimage = np.empty([len(image),len(image[0]),4])
    for i in range(len(image)):
      for j in range(len(image[i])):
          outimage[i][j] = image[i][-j-1]  
    return outimage

