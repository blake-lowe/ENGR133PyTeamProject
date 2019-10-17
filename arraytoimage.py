import import_file_to_array as ifta
import os
from matplotlib import pyplot as plt


filepath = os.getcwd()+ "/boys.png"
meNDaBoyz = ifta.importImage(filepath)
img = plt.imshow(meNDaBoyz)
