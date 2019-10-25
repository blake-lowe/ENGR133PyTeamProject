
import import_file_to_array as ifta
import image_mirroring as im
import arraytoimage as ati
import rotate_picture as rp
import grayscale as gs
import blur as bl
import fastblur as fbl
import os

import import_file_to_array as ifta
import image_mirroring as im
import arraytoimage as ati
import rotate_picture as rp
import grayscale as gs
import blur as bl
import os

name = input('Input output file name: ')

# ## IMPORT TEST FILE TO ARRAY
filepath = os.getcwd()+ "/purdue.png"
meNDaBoyz = ifta.importImage(filepath)


# ## MIRROR IMAGE
# #mirrored = im.flipIt(meNDaBoyz)

## BLUR IMAGE
#blurred = bl.process(meNDaBoyz, 20, 9)

## FAST BLUR IMAGE'
blurred2 = fbl.process(meNDaBoyz, 100, 5)
# ## BLUR IMAGE
# #blurred = bl.process(meNDaBoyz, 20, 5)

# ## ROTATE IMAGE
# #rotated90 = rp.rotate(meNDaBoyz,90)
# #rotated180 = rp.rotate(meNDaBoyz,180)
# #rotated270 = rp.rotate(meNDaBoyz,270)

# ## GRAYSCALE
# #gray = gs.makeGray(meNDaBoyz)

# ## OUTPUT FILE
# #ati.outimage(name, rotated270)

## OUTPUT FILE
ati.outimage(name, blurred2)

