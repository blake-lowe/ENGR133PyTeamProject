'''
===============================================================================
ENGR 133 Program Description 
	This function rotates an image 90 degrees counterclockwise

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

def rotate1(image): #ROTATES IMAGE 90 DEGREES COUNTERCLOCKWISE
    h,w,c = image.shape #INTIALIZES VARIABLES FOR THE HEIGHT, WIDTH, AND COLORS OF THE SHAPE

    empty_image = np.zeros([w,h,c]) #CREATES A NEW 0 MATRIX WITH WIDTH AND HEIGHT OPPOSITE TO THE ORIGINAL IMAGE

    for i in range(h):
        for j in range(w):
            empty_image[j, i] = image[i,j-1] #ROTATES EACH PIXEL 90 DEGREES COUNTERCLOCKWISE
    
    return(empty_image)

def rotate(image, n):
  for i in range(0, n//90):
      image = rotate1(image)

  return(image)