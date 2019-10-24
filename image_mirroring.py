'''
===============================================================================
ENGR 133 Program Description 
	This function takes an image array an mirrors the photo across the vertical axis. It then returns the image array of the mirrored image
Assignment Information
	Assignment:     Python Group Project
	Author:         Marcus Lannie, mlannie@purdue.edu
                    Christos Levy, levy30@purdue.edu
                    Blake Lowe, lowe77@purdue.edu
                    Thomas Weese, tweese@purdue.edu
	Team ID:        002-10
	
===============================================================================
'''

import numpy as np


 
def flipIt(image): #FLIPS THE IMAGE ACROSS VERTICAL AXIS
    outimage = np.empty([len(image),len(image[0]),len(image[0][0])])
    for i in range(len(image)):
      for j in range(len(image[i])):
          outimage[i][j] = image[i][-j-1]  
    return outimage


## THESE METHODS ARE UNIMPLEMENTED IN THE MAIN


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