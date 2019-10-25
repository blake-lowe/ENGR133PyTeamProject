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
    kernel = getKernel(size, blur)
    outimage = np.empty([len(imageData), len(imageData[0]), channelCount])#create empty image with same dimensions as original
    #vertical blur only
    for i in range(0, len(imageData)):#for each row
        for j in range(0, len(imageData[0])):#for each column
            weightedAvg = np.zeros(channelCount)

            for h in range(0, len(kernel)):
                dy = -len(kernel)//2 + h#relative change in pixel y
                
                if j+dy >= 0 and j+dy < len(imageData[0]):
                    pixelY = j+dy
                elif j+dy < 0:
                    pixelY = 0
                elif j+dy > len(imageData[0]):
                    pixelY = -1
            pixelX = i
            pixel = imageData[pixelX][pixelY]#get pixel data for target pixel

            for c in range(0, len(weightedAvg)):#sum the corresponding ARGB or RGB numbers
                weightedAvg[c] += kernel[h]*pixel[c]

            outimage[i][j] = weightedAvg

    imageData = outimage

    #horizontal blur only
    for i in range(0, len(imageData)):#for each row
        for j in range(0, len(imageData[0])):#for each column
            weightedAvg = np.zeros(channelCount)

            for k in range(0, len(kernel)):
                dx = -len(kernel)//2 + k#relative change in pixel y
                
                if i+dx >=0 and i+dx < len(imageData):#if pixel is out of bounds, extend the image
                    pixelX = i+dx
                elif i+dx < 0:
                    pixelX = 0
                elif i+dx >= len(imageData):
                    pixelX = -1
            pixelY = j
            pixel = imageData[pixelX][pixelY]#get pixel data for target pixel

            for c in range(0, len(weightedAvg)):#sum the corresponding ARGB or RGB numbers
                weightedAvg[c] += kernel[h]*pixel[c]

            outimage[i][j] = weightedAvg

    
            
    return outimage

def getKernel(size, stddev):
    kernel = []
    center = (int(size))//2
    for i in range(0, size):
        x = i-center
        kernel.append(gaussian(x, stddev))
    kernel = normalizeArray(kernel)
    print(sum(kernel))
    return kernel

def gaussian(x, stddev):
    A = 1/(math.sqrt(2*math.pi)*stddev)
    return A*math.exp(-(x*x)/(2*stddev*stddev))

def normalizeArray(array):#1D array input
    total = 0
    for i in range(len(array)):
        total += array[i]
    for i in range(len(array)):
        array[i] /= total
    
    return(array)
