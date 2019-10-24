'''
===============================================================================
ENGR 133 Program Description 
	This function takes an image file and converts it into a 3D array. It then returns the array.
Assignment Information
	Assignment:     Python Group Project
	Author:         Marcus Lannie, mlannie@purdue.edu
                    Christos Levy, levy30@purdue.edu
                    Blake Lowe, lowe77@purdue.edu
                    Thomas Weese, tweese@purdue.edu
	Team ID:        002-10
	
===============================================================================
'''

import matplotlib.image as mpimg
import numpy as np

## Takes a file path and returns the array form of the image
def importImage(path): ## Where path is the file path as a string
    image = mpimg.imread(path) 
    return image

