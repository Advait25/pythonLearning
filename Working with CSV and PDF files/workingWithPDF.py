print('WORKING WITH PDFs')

#import csv module
import PyPDF2

#import os to change current wokring directory
import os
os.chdir('C:/Users/Advait/Documents/Learning/pythonLearning/Working with CSV and PDF files/')

f_pdf = open('Working_Business_Proposal.pdf', mode='rb')

f_pdf_reader = PyPDF2.PdfReader(f_pdf)

print('\nGet number of pages')
print(len(f_pdf_reader.pages))

print('\nget page 1 and its text')
f_pdf_text_0 = f_pdf_reader.pages[0].extract_text()
print(f_pdf_text_0)

#f_pdf.close()

print('\nadd pages to pdf')
#pdfs are designed not to be editted, so what we can do is create a new writer object and add page/s to it and save it as a pdf
#the pages that will be added has tp be a specialized PageObject

second_page = f_pdf_reader.pages[1]

new_f_pdf = open('new_pdf.pdf',mode='wb')

new_f_pdf_writer = PyPDF2.PdfWriter(new_f_pdf)

new_f_pdf_writer.add_page(second_page)

new_f_pdf_writer.write(new_f_pdf)

print('page added')

#f_pdf.close()
new_f_pdf.close()

print('\nget text from all pages of pdf')

all_text = []

for page_num in range(len(f_pdf_reader.pages)):
    page_text = f_pdf_reader.pages[page_num].extract_text()
    all_text.append(page_text)

#print(all_text[0])
#print(all_text[1])
#print(all_text[2])
print(all_text[3])
#print(all_text[4])

f_pdf.close()
