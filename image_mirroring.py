import numpy as np


 
def flipIt(image): #FLIPS THE IMAGE ACROSS VERTICAL AXIS
    outimage = np.empty([len(image),len(image[0]),4])
    for i in range(len(image)):
      for j in range(len(image[i])):
          outimage[i][j] = image[i][-j-1]  
    return outimage

def flipH(image): #FLIPS IMAGE ACROSS HORIZONTAL AXIS
    outimage = np.empty([len(image),len(image[0]),4])
    for i in range(len(image)):
      for j in range(len(image[i])):
          outimage[i][j] = image[-i-1][j]  
    return outimage

def mirrorH(image): # "MIRRORS" IMAGE ACROSS HORIZONTAL AXIS
    for i in range(len(image)):
      for j in range(len(image[i])):
          image[i][j] = image[-i-1][j]  
    return image

def mirrorV(image): # "MIRRORS" IMAGE ACROSS VERTICAL AXIS
    for i in range(len(image)):
      for j in range(len(image[i])):
          image[i][j] = image[i][-j-1]  
    return image