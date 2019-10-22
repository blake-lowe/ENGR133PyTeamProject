
import math


def process(imageData):
    return

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

def gaussian2D(x, y, stddev):
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



print(getKernel(3, 5.5))
print(gaussian2D(0, 0, 1))
