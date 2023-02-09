print('SHUTIL AND OS MODULE')

print('open a file in write mode')
f =  open('C:/Users/Advait/Documents/Learning/pythonLearning/AdvancePythonModules/practise.txt','w+')
f.write('this is a test string for a test file')
f.close()

#importing OS module
#it has commands which can work across all systems

import os

print(f'1. get current working directory: \n {os.getcwd()}')

print(f'2. list item in current directory: \n {os.listdir()}')

print(f'3. list item in any directory on computer: \n {os.listdir("C:/Users")}')

#importing shell utility  module
#this helps to move file in diff location
import shutil

#shutil.move('C:/Users/Advait/Documents/Learning/pythonLearning/AdvancePythonModules/practise.txt','C:/Users/Advait/Documents/Learning/')
#print(os.listdir('C:/Users/Advait/Documents/Learning/'))

#os.unlink(path) -> to delete the file in the provided path
#os.rmdir(path) ->  deleting the folder in the provided path(folder has to be emoppty)
#shutil.rmtree(path) -> to remove all files and folder in the path -> alternate more safe module =  send2trash, command -> pip install send2trash


#OS.Walk ->  directory tree generator
print('get file/folder tree at a path using OS.Walk method')

for folder, subfolders, files in os.walk('C:/Users/Advait/Documents/Learning/pythonLearning/AdvancePythonModules/example/'):
    print(f"current directory is : {folder}")
    print("\n")

    print("the subfolders here are : ")
    for sub_folder in subfolders:
        print(f"\t subfolder : {sub_folder}")
        print("\n")

    print("here are the files: ")
    for f in files :
        print(f"\t file : {f}")
        print("\n")







