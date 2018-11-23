#This file collects the metadata from all fits files in the selected directory and
#prints them to a text file, ready to import into a database
#Written by Matt Thomas for TheShoeFits: https://github.com/matthomas15/TheShoeFits/tree/master/FitsModule
#This code reads FITS files from the directory Datafiles/spectra in the repository and prints the properties 
# of the Info class (from fits_module_class.py)

#import required
from astropy.io import fits
from os import listdir
import re
#Import packages from our repository
from fits_module_class import *

file_directory = "Datafiles/spectra" #set file path/folder containing the FITS files
output_file_directory = "Documents/FILE_Metadata.txt"  #Add desired file path for output file


output_file = open(output_file_directory, mode = "w") #create blank output file for writing, overwriting last output file

fits_files = listdir(file_directory) #Generate list of all files in directory -

#Write heading names to the output file
#output_file.write("telecope_name|right_ascention|declination|plate_id")
a = list()
header_counter = 0
for file in fits_files:
    #First check that the line we are reading contains a .fits file
    line = re.search("([a-zA-Z-0-9]+.fits)", file)
    if line is None: #Ignores lines which do not have the .fits file extension
        print(f"File is not a .fits file: {file}")
        continue
    else:
        current_file=Info(f"{file_directory}/{file}")
        variable_dictionary = vars(current_file)
        #Dynamically set the column headers based on the attributes of Info class.
        if header_counter == 0:
            for value in range(len(list(variable_dictionary.values()))):
                output_file.write(f"{list(variable_dictionary.keys())[value]}|")
            header_counter = 1
            output_file.write("\n")
        else:
            for value in range(len(list(variable_dictionary.values()))):
                output_file.write(f"{list(variable_dictionary.values())[value]}|")
            output_file.write("\n")

        #output_file.write(f"\n{current_file.telescope}|{current_file.ra }|{current_file.dec}|{current_file.plate_id}")


output_file.close()
