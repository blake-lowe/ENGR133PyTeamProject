'''
===============================================================================
ENGR 133 Program Description 
	This function takes an image array, a size number and a blur value and returns an array that contains a blurred image

Assignment Information
	Assignment:     Python Group Project
	Author:         Marcus Lannie, mlannie@purdue.edu
                    Christos Levy, levy30@purdue.edu
                    Blake Lowe, lowe77@purdue.edu
                    Thomas Weese, tweese@purdue.edu
	Team ID:        002-10
	
===============================================================================
'''

import math
import numpy as np


def process(imageData, blur, size):
    if(size%2 == 0):
        size += 1
    kernel = getKernel(size, blur)
    outimage = np.empty([len(imageData), len(imageData[0]), 4])#create empty image with same dimensions as original
    for i in range(0, len(imageData)):
        print(f"pixel done ({i},{0})")
        for j in range(0, len(imageData[0])):#for each pixel in image
            weightedAvg = [0, 0, 0, 0]
            
            for h in range(0, len(kernel)):
                for k in range(0, len(kernel[0])):#for each number in kernel
                    dx = -len(kernel)//2 + h#relative change in pixel x
                    dy = -len(kernel)//2 + k#relative change in pixel y
                    if((i+dx>=0 and i+dx<len(imageData)) and (j+dy >= 0 and j+dy<len(imageData[0]))):#if within original image
                        pixel = imageData[i+dx][j+dy]
                    elif((i+dx < 0 or i+dx>=len(imageData)) and (j+dy >= 0 and j+dy<len(imageData[0]))):#if only horizontally out of original
                        if(i+dx < 0):
                            pixel = imageData[0][j+dy]
                        elif(i+dx >= len(imageData)):
                            pixel = imageData[-1][j+dy]
                    elif((i+dx>=0 and i+dx<len(imageData)) and (j+dy < 0 or j+dy >len(imageData[0]))):#if vertically out of original
                        if(j+dy < 0):
                            pixel = imageData[i+dx][0]
                        elif(j+dy >= len(imageData)):
                            pixel = imageData[i+dx][-1]
                    else:#if corner out of original
                        if(i+dx < 0 and j+dy < 0):#top left
                            pixel = imageData[0][0]
                        elif(i+dx < 0 and j+dy > len(imageData[0])):#bottom left
                            pixel = imageData[0][-1]
                        elif(i+dx > len(imageData) and j+dy < 0):#top right
                            pixel = imageData[-1][0]
                        elif(i+dx > len(imageData) and j+dy > len(imageData[0])):#bottom right
                            pixel = imageData[-1][-1]

                    for c in range(0, len(weightedAvg)):
                            weightedAvg[c] += kernel[h][k]*pixel[c]

            outimage[i][j] = weightedAvg

    return outimage

def getKernel(size, stddev):#odd integer size of square kernel, spread in both directions
    kernel = []

    center = (int(size))
    for j in range(0, size):
        row = []
        for i in range(0, size):
            x = i-center
            y = j-center
            row.append(gaussian2D(x, y, stddev))
        kernel.append(row)
    kernel = normalizeArray(kernel)
    return kernel

def gaussian2D(x, y, stddev):#return the gaussian2D function evaluated at x and y
    A = 1/(2*math.pi*stddev*stddev)
    return A*math.exp(-(x*x+y*y)/(2*stddev*stddev))

def normalizeArray(array):#2D array input
    total = 0
    for i in range(len(array[0])):
        for j in range(len(array)):
            total += array[i][j]
    #print(sum(sum(array,[])))
    for i in range(len(array[0])):
        for j in range(len(array)):
            array[i][j] /= total
    
    #print(sum(sum(array,[])))
    return(array)
