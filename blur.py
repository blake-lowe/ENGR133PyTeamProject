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
    channelCount = len(imageData[0][0])#determine if RGB or RGBA
    rowCount = len(imageData)#for progress display
    if(size%2 == 0):
        size += 1
    kernel = getKernel(size, blur)
    outimage = np.empty([len(imageData), len(imageData[0]), channelCount])#create empty image with same dimensions as original
    for i in range(0, len(imageData)):
        print(f"Row {i}/{rowCount}")
        for j in range(0, len(imageData[0])):#for each pixel in image
            weightedAvg = np.zeros(channelCount)
            
            for h in range(0, len(kernel)):
                for k in range(0, len(kernel[0])):#for each number in kernel
                    dx = -len(kernel)//2 + h#relative change in pixel x
                    dy = -len(kernel)//2 + k#relative change in pixel y

                    if i+dx >=0 and i+dx < len(imageData):#if pixel is out of bounds, extend the image
                        pixelX = i+dx
                    elif i+dx < 0:
                        pixelX = 0
                    elif i+dx >= len(imageData):
                        pixelX = -1

                    if j+dy >= 0 and j+dy < len(imageData[0]):
                        pixelY = j+dy
                    elif j+dy < 0:
                        pixelY = 0
                    elif j+dy > len(imageData):
                        pixelY = -1

                    pixel = imageData[pixelX][pixelY]#get pixel data for target pixel

                    for c in range(0, len(weightedAvg)):#sum the corresponding ARGB or RGB numbers
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
