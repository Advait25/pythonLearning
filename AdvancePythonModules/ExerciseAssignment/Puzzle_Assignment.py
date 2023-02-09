#import modules
import os
import zipfile
import re
import pdb

#change working directory to current folder
os.chdir('/home/ag/Documents/python/pythonLearning/AdvancePythonModules/ExerciseAssignment/')

#create extract object and extract the file
extr_obj = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
extr_obj.extractall()

#open instructions.txt file
with open('extracted_content/Instructions.txt','r') as i:
    print(i.read())

#regex for telephone number
pattern = r"\d{3}-\d{3}-\d{4}"


#search function
def search_phone(filename):
    
    #open file and search for phone number using regex
        with open(filename,'r') as f_obj:
            phone_number = re.search(pattern, f_obj.read())

            #if phone number found print it
            if phone_number:
                print(f'file ->{f}<- has phone number --> {phone_number.group()}')



#os.walk to traverse through the files
for folder,subfolder,files in os.walk('extracted_content',topdown=False):
    
    #iterate through files
    for f in files:

        #creating full file name i.e. file name with path to read it 
        #And search it
        filename = os.path.join(folder,f)
        search_phone(filename)

