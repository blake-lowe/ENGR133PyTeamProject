import numpy as np
def rotate(image):
    h,w,c = image.shape

    empty_image = np.zeros([h,w,c], dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            empty_image[i, j] = image[j-1, i-1]
    
    return(empty_image)