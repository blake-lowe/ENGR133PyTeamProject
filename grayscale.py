'''
===============================================================================
ENGR 133 Program Description 
	This function takes an image array and converts the color values to grey. Then it returns the image array

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

##Takes the image array and returns it as a gray image by using the weighted average RBG formula
def makeGray(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            ## Finds value of RGB nums
            r = image[i][j][0]
            g = image[i][j][1]
            b = image[i][j][2]

            ## Calculates grayscale by using the weighted average formula
            Avg = 0.2989*r+0.5780*g+0.1140*b
            ## Reassigns colors to the average
            image[i][j][0], image[i][j][1], image[i][j][2] = Avg,Avg,Avg

    return image