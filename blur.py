
import math
def getKernel(size, stdev):#odd integer size of square kernel, spread in both directions
    kernel = []

    center = (int(size)/2)
    for j in range(0, size):
        for i in range(0, size):
            row = []
            row.append(#todo)

    return kernel

def gaussian2D(x, y, stddev):
    A = 1/(2*math.pi*stddev*stddev)
    return A*math.exp(-(x*x+y*y)/(2*stddev*stddev))

print(gaussian2D(0, 0, 1))
