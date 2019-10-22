import numpy as np

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