import import_file_to_array as ifta
import matplotlib as mpl

## Takes an input name and the array of the filter and outputs an image in the directory
def outimage(name, array):
    mpl.image.imsave(name + '.png', array)
    return
