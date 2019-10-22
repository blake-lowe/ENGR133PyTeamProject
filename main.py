import import_file_to_array as ifta
import image_mirroring as im
import arraytoimage as ati
import rotate_picture as rp
import grayscale as gs
import blur as bl
import os

name = input('Input output file name: ')

## IMPORT TEST FILE TO ARRAY
filepath = os.getcwd()+ "/boys.png"
meNDaBoyz = ifta.importImage(filepath)


## MIRROR IMAGE
#mirrored = im.flipIt(meNDaBoyz)

## BLUR IMAGE
blurred = bl.process(meNDaBoyz)

## ROTATE IMAGE
rotated = rp.rotate(meNDaBoyz, 180)

## GRAYSCALE
gray = gs.makeGray(meNDaBoyz)

## OUTPUT FILE
ati.outimage(name, blurred)