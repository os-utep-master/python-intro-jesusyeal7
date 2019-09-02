"""
Jesus Ramos
Intro to Python Lab
Prof. Daniel Cervantes

"""
import sys        
import re         
import os         
import subprocess 
import string

# This is if statement will set the input and output files 
if len(sys.argv) is not 3:
    print("Invalid Input") # This message will appear if the input is Invalid 
    exit()

#Input File
inputFile = sys.argv[1]
#Output File
fileOutput = sys.argv[2]

# Counts words in an input file
def countCharacters(inputIn, txtFile):

# This for loop is printing the characters with an if statement inside 
    for characters in input_File.read().split(): # .read() and .split() Reads and splits the characters/words 
        characters = characters.lower() # Makes sure all letters are lower case
        characters = characters.translate(None, string.punctuation)
        #print(Characters)

        if characters not in txtFile:
            txtFile[characters] = 1
            
        else:
            txtFile[characters]+= 1
           


def dictionaryChar(fileOutput, txtFile):
    fileOutput = open(fileOutput,"w+")
    for i in sorted(txtFile):
        fileOutput.write("%s %d \n" % (i, txtFile[i]))
    print("Completed") # Print out message when task is done

# This are methods that are being called
txtFile = {}
input_File = open(inputFile, "r")
countCharacters(input_File, txtFile)
dictionaryChar(fileOutput, txtFile)