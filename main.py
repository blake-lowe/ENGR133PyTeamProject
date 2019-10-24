import import_file_to_array as ifta
import image_mirroring as im
import arraytoimage as ati
import rotate_picture as rp
import grayscale as gs
import blur as bl
import os

isKilled = False
while True:
    infName = input("Enter name of file to process with extention (.png only): ")
    if(infName.lower() == "quit"):
        isKilled = True
        break
    filepath = os.getcwd()+ "/" + infName
    try:
        inImage = ifta.importImage(filepath)
        print("Image successfully imported!")
        break
    except:
        print("File not found. Try again. (Type 'quit' to kill program)")

outImage = [][][]
if !isKilled:
    while True:
        print("Functions: blur, grayscale, rotate, mirror")
        processName = input("Enter name of function: ").lower()
        if(processName == "quit"):
            isKilled = True
            print("Killing program...")
            break
        elif(processName == "blur"):#todo
            print("You have chosen blur.")
            break
        elif(processName == "grayscale"):#done
            print("You have chosen grayscale.")
            outImage = gs.makeGray(inImage)
            print("Image processing complete.")
            break
        elif(processName == "rotate"):#done
            print("You have chosen rotate.")
            degrees = 0
            while True:
                degrees = input("Enter number of degrees to rotate (must be divisible by 90)")
                try:
                    degrees = int(degrees)
                except:
                    print("Error: Input must be numeric")
                    continue
                if degrees%90 != 0:
                    print("Error: degrees must be divisible by 90")
                    continue
                else:
                    break
            outImage = rp.rotate(inImage, degrees)
            print("Image processing complete.")
            break
        elif(processName == "mirror"):#done
            print("You have chosen mirror.")
            im.flipIt(inImage)
            break
        else:#done
            print("Error: Input not recognized, please enter then name of a function. (Type 'quit' to kill program)")

if !isKilled:
    outfName = input("Enter name for output file without extension: ")
