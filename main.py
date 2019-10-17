import import_file_to_array as ifta
import os


## TEST IMPORT FILE TO ARRAY
filepath = os.getcwd()+ "/boys.png"
meNDaBoyz = ifta.importImage(filepath)
print(meNDaBoyz)