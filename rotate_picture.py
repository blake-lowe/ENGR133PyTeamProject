import numpy as np
def rotate(image): #ROTATES IMAGE 90 DEGREES COUNTERCLOCKWISE
    h,w,c = image.shape #INTIALIZES VARIABLES FOR THE HEIGHT, WIDTH, AND COLORS OF THE SHAPE

    empty_image = np.zeros([w,h,c]) #CREATES A NEW 0 MATRIX WITH WIDTH AND HEIGHT OPPOSITE TO THE ORIGINAL IMAGE

    for i in range(h):
        for j in range(w):
            empty_image[j, i] = image[i, j-1] #ROTATES EACH PIXEL 90 DEGREES COUNTERCLOCKWISE
    
    return(empty_image)