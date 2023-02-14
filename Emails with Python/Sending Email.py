print('WORKING WITH EMAILS')

import smtplib
import getpass    #it is very good for saving values in encrypted format

#creating smtp email server object
smtp_0bj = smtplib.SMTP('smtp.gmail.com',587)

#establishing connection
smtp_0bj.ehlo() #o/p (250, b'smtp.gmail.com at your service, [2402:e280:3e09:2e:e966:539d:c122:67dc]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')


#port 587 means we are using TLS encryption
smtp_0bj.starttls() #o/p (220, b'2.0.0 Ready to start TLS')

#setting up email and pwd
email = getpass.getpass('Email:')
password = getpass.getpass('password: ')

#login
smtp_0bj.login(email, password)

#create and send email
from_address = email
to_address =  email
subject = 'test mail from python script'
message = 'hello from python script'
msg = 'Subject:'+subject+'\n'+message

#send email
smtp_0bj.sendmail(from_address, to_address, msg)

#quit the object
smtp_0bj.quit()