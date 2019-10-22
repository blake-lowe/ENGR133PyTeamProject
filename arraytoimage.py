import import_file_to_array as ifta
import os
import matplotlib as mpl

filepath = os.getcwd()+ "/boys.png"
meNDaBoyz = ifta.importImage(filepath)

def outimage(name, array):
    mpl.image.imsave(name + '.png', array)
    return
