print('Zipping and Unzipping the files')

import zipfile
import os
import pdb

#change working directory here at the top
#this will fix the bug ->  the zip file creation was gettnig created with the whole path structure, resulting in similar structure while extracting
os.chdir('/home/ag/Documents/python/pythonLearning/AdvancePythonModules/zipit/')

path = os.getcwd()

#creating files
f =  open('file_one.txt','w+')
f.write('File ONE')
f.close()

f =  open('file_two.txt','w+')
f.write('File TWO')
f.close()

#create compress file object
comp_file = zipfile.ZipFile('comp_file.zip','w')

#add the files  ,that need to be compressed, to comp_file object 
#refer os module for below code ->  shutil_and OS.py

for folder,subfolder,files in os.walk(path):
    for f in files:
        if '.txt' in f:
            comp_file.write(f,compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()
#extract the zipped file
extract_obj = zipfile.ZipFile('comp_file.zip','r')
#extract_obj.extract('file_one.txt')    -> to extract individual file
extract_obj.extractall('extracted')    #to extract all

