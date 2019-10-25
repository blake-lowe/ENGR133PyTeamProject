'''
===============================================================================
ENGR 133 Program Description 
	Main Script to run all functions

Assignment Information
	Assignment:     Python Group Project

	Author:         Marcus Lannie, mlannie@purdue.edu
                    Christos Levy, levy30@purdue.edu
                    Blake Lowe, lowe77@purdue.edu
                    Thomas Weese, tweese@purdue.edu

	Team ID:        002-10
	
    Copyright Da Boys ENGR 133 2019
    All rights Reserved
===============================================================================
'''

## IMPORT FUNCTIONS
import numpy as np
import import_file_to_array as ifta
import image_mirroring as im
import arraytoimage as ati
import rotate_picture as rp
import grayscale as gs
import blur as bl
import os

## Asks for name of the file
while True:
    isKilled = False
    while True:
        infName = input("Enter name of file to process with extention (.png only): ")
        if(infName.lower() == "quit"):
            isKilled = True
            break
       
        filepath = os.getcwd()+ "/" + infName
    
        ## Converts image to an array after successful import
        try:
            inImage = ifta.importImage(filepath)
            print("Image successfully imported!")
            break

        ## Repeats if the file isn't found
        except:
            print("File not found. Try again. (Type 'quit' to kill program)")
            continue
    if isKilled == True:
        print("\n\n\n")
        break 



    if isKilled == False:
        ## Asks user for desired function
        while True:
            print("Functions: blur, grayscale, rotate, mirror")
            processName = input("Enter name of function: ").lower()
            if(processName == "quit"):
                isKilled = True
                print("Killing program...\n\n\n")
                break
        
            ## Runs Blur Function and assures input values are (str, float, int)
            elif(processName == "blur"):
                print("You have chosen blur.")
                blurValue = 0
                size = 0
                ## Checks if the values are correct data type and valid
                while True:
                    blurValue = input("Enter blur value: ")
                    try:
                        blurValue = float(blurValue)
                        break
                    except:
                        print("Error: Blur value must be an float")
                        continue
                while True:
                    size = input("Enter size value as an odd integer greater than or equal to 3: ")
                    try:
                        size = int(size)
                    except:
                        print("Error: Size value must be an integer")
                        continue
                    
                    if size%2 == 0 or size < 3:
                        print("Error: Size value must be odd and greater than or equal to 3.")
                        continue
                    else:
                        break
                ## Creates blurred image
                outImage = bl.process(inImage,blurValue,size)
                break

            ## Runs Grayscale Function
            elif(processName == "grayscale"):
                print("You have chosen grayscale.")
                outImage = gs.makeGray(inImage)
                print("Image processing complete.")
                break

            ## Runs Rotate Function
            elif(processName == "rotate"):
                print("You have chosen rotate.")
                degrees = 0
                while True:
                    degrees = input("Enter number of degrees to rotate (must be divisible by 90): ")

                    ## Checks to see if input is a number
                    try:
                        degrees = int(degrees)
                    except:
                        print("Error: Input must be numeric")
                        continue

                    ## Checks if the number is a factor of 90
                    if degrees%90 != 0:
                        print("Error: degrees must be divisible by 90")
                        continue
                    else:
                        break
                outImage = rp.rotate(inImage, degrees)
                print("Image processing complete.")
                break

            ## Runs mirror function
            elif(processName == "mirror"):
                print("You have chosen mirror.")
                outImage = im.flipIt(inImage)
                break

            ## Prints an error if a function is not found
            else:
                print("Error: Input not recognized, please enter then name of a function. (Type 'quit' to kill program)")
        if isKilled == True:
            break    

    ## Creates and outputs the file to the directory
    if isKilled == False:
        fileName = input("Enter name for output file without extension: ")
        ati.outimage(fileName,outImage)

        ## Asks if user wishes to run again
        runDecision = input("Run Again? (Y/N): ").lower()
        if runDecision == "n":
            print("Thank you for using the Python Deluxe Photo Editor!\n\n\n")
            isKilled = True
            break
        else:
            continue

