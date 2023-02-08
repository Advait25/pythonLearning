print('Zipping and Unzipping the files')

import zipfile
import os
import pdb

path = '/home/ag/Documents/python/pythonLearning/AdvancePythonModules/zipit/'


#creating files
f =  open(path+'file_one.txt','w+')
f.write('File ONE')
f.close()

f =  open(path+'file_two.txt','w+')
f.write('File TWO')
f.close()

#create compress file object
comp_file = zipfile.ZipFile(path+'comp_file.zip','w')

#add the files  ,that need to be compressed, to comp_file object 
#refer os module for below code ->  shutil_and OS.py

for folder,subfolder,files in os.walk(path):
    for f in files:
        full_filename = path + f
        comp_file.write(full_filename,compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()
#extract the zipped file
extract_obj = zipfile.ZipFile(path+'comp_file.zip','r')
#extract_obj.extract('file_one.txt')    -> to extract individual file

extract_obj.extractall('extracted_content')    #to extract all

