import import_file_to_array as ifta
import image_mirroring as im
import arraytoimage as ati
import rotate_picture as rp
import grayscale as gs
import os

name = input('Input output file name: ')

## IMPORT TEST FILE TO ARRAY
filepath = os.getcwd()+ "/boys.png"
meNDaBoyz = ifta.importImage(filepath)


## MIRROR IMAGE
#mirrored = im.flipV(meNDaBoyz)


## ROTATE IMAGE
#rotated = rp.rotate(meNDaBoyz)

## GRAYSCALE
gray = gs.makeGray(meNDaBoyz)

## OUTPUT FILE
ati.outimage(name, gray)