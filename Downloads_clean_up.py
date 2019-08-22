# Short script to organize files in The downloads folder
# By: Parrot023
# github.com/parrot023

#Imports
import os
import shutil
import time

#variables
path = 'C:\\Users\\Andre\\Downloads'
files = []
files_bf = []
iterations = 0

while True:

    #Sleeps for a second
    time.sleep(1)

    #Updates files_bf (files before)
    files_bf = files

    files = []

    #Adds all files in dir to list files
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
    
    if iterations > 0:
        for f in files:
            if not f in files_bf:
                print("new file ", f)

                #Opens file: Log.txt
                file = open("Log.txt", "a+") 
                #Initial string
                string = "Moved file: " + f + " to: " + path

                #Moves files based on file type
                if ".txt" in f:
                    #Moves file
                    shutil.move("C:\\Users\\Andre\\Downloads\\" + f, "C:\\Users\\Andre\\Downloads\\Text_files")
                    #Adds folder name to string
                    string += "\\Text_files"
                if ".docx" in f or ".doc" in f:
                    shutil.move("C:\\Users\\Andre\\Downloads\\" + f, "C:\\Users\\Andre\\Downloads\\Docx_files")
                    string += "\\Docx_files"

                if ".jpeg" in f or ".png" in f or ".jpg" in f:
                    shutil.move("C:\\Users\\Andre\\Downloads\\" + f, "C:\\Users\\Andre\\Downloads\\Images")
                    string += "\\Images" 

                if ".exe" in f:
                    shutil.move("C:\\Users\\Andre\\Downloads\\" + f, "C:\\Users\\Andre\\Downloads\\Executable_files")
                    string += "\\Executable_files"

                #Writes string to file
                file.write(string + "\r\n")
                #Closes file
                file.close() 
    
    iterations += 1



        



        