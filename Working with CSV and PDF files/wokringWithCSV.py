print('WORKING WITH CSVs')

#import csv module
import csv

#import os to change current wokring directory
import os
os.chdir('C:/Users/Advait/Documents/Learning/pythonLearning/Working with CSV and PDF files/')

#open exampl.csv
#tip ->  whenever opening a csv file do not forget to include the unicode parameter to let python know what kind of data it will be reading
#otherwise it will throw error like this -> UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 1835: character maps to <undefined>
#google for appropriate unicode and add while opening the file
#in this case encoding ='utf-8' for english
data = open('example.csv',encoding = 'utf-8')

#get csv data
csv_data = csv.reader(data)

#convert to list of lists
data_lines = list(csv_data)

#print(data_lines)

print('\nget column names')
print(data_lines[0])

print('\nnumber of rows')
print(len(data_lines))

print('\nfirst 5 rows')
for dl in data_lines[:5]:
    print(dl)

print('\nparticular numbered row, 15th and then print only its email')
print(data_lines[14])
print(data_lines[14][3])

print('\nget all emails for row 110 to 130') 
all_emails = []
for data in data_lines[110:130]:   #start from one as 0th is column names
    all_emails.append(data[3])

print(all_emails)


print('\nGet full names for rows 40 to 70')

full_names = []
for data in data_lines[40:70]:
    full_names.append(data[1]+' '+data[2])

print(full_names)

print('\n create and save a csv file and also append data to it')

fileCsv = open('new_csv.csv', mode='w', newline='')
csv_writer = csv.writer(fileCsv,delimiter=',')
csv_writer.writerow([1,2,4])  #to write single row
csv_writer.writerows([['a','b','c'],[5,6,7]]) #to write multiple rows
fileCsv.close()

new_fileCsv = open('new_csv.csv',mode='a',newline='')
new_csv_writer = csv.writer(new_fileCsv,delimiter=',')
new_csv_writer.writerow([7,3,8])
new_fileCsv.close()