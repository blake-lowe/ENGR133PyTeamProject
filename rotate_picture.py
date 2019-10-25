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
## Rotates image based on specified degrees

def rotate(image,degrees): 

    ## Will rotate image 90 degrees counterclockwise
    if degrees == 90: 
        h,w,c = image.shape 
        empty_image = np.zeros([w,h,c]) ## Creates a new image that has opposite dimensions as original 
        for i in range(h):
            for j in range(w):
                empty_image[-j-1,i] = image[i,j] 
        return(empty_image)
    ## Rotates image 180 degrees or mirrors over horizontal axis
    elif degrees == 180: 
        empty_image = np.empty([len(image),len(image[0]),len(image[0][0])]) ## Creates a new image that has same dimensions as original 
        for i in range(len(image)):
            for j in range(len(image[i])):
                empty_image[i][j] = image[-i-1][-j-1]  
        return empty_image

    ## Rotates image 270 degrees counterclockwise
    elif degrees == 270: 
        h,w,c = image.shape 
        empty_image = np.zeros([w,h,c]) ## Creates a new image that has opposite dimensions as original 
        for i in range(h):
            for j in range(w):
                empty_image[j,-i-1] = image[i,j] 
        return(empty_image)
        
    
        

