import import_file_to_array as ifta
import image_mirroring as im
import arraytoimage as ati
import rotate_picture as rp
import os
name = input('Input output file name: ')

## TEST IMPORT FILE TO ARRAY
filepath = os.getcwd()+ "/boys.png"
meNDaBoyz = ifta.importImage(filepath)
#print(meNDaBoyz)

## MIRROR IMAGE
mirrored = im.flipV(meNDaBoyz)
#print(mirrored)

## ROTATE IMAGE
#rotated = rp.rotate(meNDaBoyz)

## OUTPUT FILE
ati.outimage(name, mirrored)