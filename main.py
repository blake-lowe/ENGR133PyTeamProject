import import_file_to_array as ifta
import image_mirroring as im
import os


## TEST IMPORT FILE TO ARRAY
filepath = os.getcwd()+ "/boys.png"
meNDaBoyz = ifta.importImage(filepath)
print(meNDaBoyz)

##MIRROR IMAGE
mirrored = im.mirror(filepath)
print(mirrored)