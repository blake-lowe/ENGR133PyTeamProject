import numpy as np
def rotate(image):
    h,w,c = image.shape

    empty_image = np.zeros([w,h,c]) #,dtype=np.uint8

    for i in range(h):
        for j in range(w):
            empty_image[j, i] = image[i, j-1]
    
    return(empty_image)


    ''' int m = input[0].length();
    int [][] output = new int [m][n];

    for (i=0; i<n; i++)
	    for (int j=0;j<m; j++)
		    output [j][n-1-i] = input[i][j];
    
    return output; '''