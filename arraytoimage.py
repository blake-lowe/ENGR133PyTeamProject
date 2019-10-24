'''
===============================================================================
ENGR 133 Program Description 
	This function takes an array and converts it to an image and saves it in the file directory.

Assignment Information
	Assignment:     Python Group Project
	Author:         Marcus Lannie, mlannie@purdue.edu
                    Christos Levy, levy30@purdue.edu
                    Blake Lowe, lowe77@purdue.edu
                    Thomas Weese, tweese@purdue.edu
	Team ID:        002-10
	
===============================================================================
'''


import import_file_to_array as ifta
import matplotlib as mpl

## Takes an input name and the array of the filter and outputs an image in the directory
def outimage(name, array):
    mpl.image.imsave(name + '.png', array)
    return
