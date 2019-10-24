'''
===============================================================================
ENGR 133 Program Description 
	This function rotates an image 90 degrees counterclockwise

Assignment Information
	Assignment:     Python Group Project
	Author:         Marcus Lannie, mlannie@purdue.edu
	Team ID:        002-10
	
Contributor:    None, name@purdue.edu [repeat for each]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''

import numpy as np
def rotate1(image): #ROTATES IMAGE 90 DEGREES COUNTERCLOCKWISE
    h,w,c = image.shape #INTIALIZES VARIABLES FOR THE HEIGHT, WIDTH, AND COLORS OF THE SHAPE

    empty_image = np.zeros([w,h,c]) #CREATES A NEW 0 MATRIX WITH WIDTH AND HEIGHT OPPOSITE TO THE ORIGINAL IMAGE

    for i in range(h):
        for j in range(w):
            empty_image[j, i] = image[i, j-1] #ROTATES EACH PIXEL 90 DEGREES COUNTERCLOCKWISE
    
    return(empty_image)

def rotate(image, n):
  for i in range(0, n//90):
      image = rotate1(image)

  return(image)