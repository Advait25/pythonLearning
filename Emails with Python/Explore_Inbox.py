print('WORKING WITH EMAILS')

import email
import imaplib
import getpass

#connect to gamil imap server
M = imaplib.IMAP4_SSL('imap.gmail.com')

#login
email_id = getpass.getpass('Email:')
password = getpass.getpass('password: ')
M.login(email_id, password)  #o/p ('OK', [b'advaitgokhale25@gmail.com authenticated (Success)'])

#differet option of folder in your rmail
#print(M.list())

#go to inbox
M.select('inbox')
#x= M.select('inbox')
#print(f'\n{x}')

#filter data for particualr subject line
typ, data = M.search(None, 'SUBJECT "test mail from python script"')
#print(f'\n{typ}   {data}')

#fetch actual data
result, email_data = M.fetch(data[0], "RFC822")  #The Internet RFC 822 specification defines an electronic message format consisting of header fields and an optional message body. 
#print(f'\n{result}   {email_data}')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

#use inbuilt email library to parse the raw string to text
email_message = email.message_from_string(raw_email_string)
#print(f'\n{email_message}')

#to get actual body we have to iterate through iterater object email_message
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':   #we can use text/html in case any links are in the email
        body = part.get_payload(decode=True)
        print(body)





