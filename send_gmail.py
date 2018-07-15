#!/usr/bin/env python36

####
#name: lior
#date: 14/7/18
#	   this script will send an email with gmail accounts.
#	   to send an email with this script, you may need to create an
#	   app-specific password for less secure apps in your gmail account.
####


import smtplib
import getpass
import time

#ask for username and password for gmail
user_mail = input('please enter your gmail: ')
user_pass = getpass.getpass('enter your password: ')

#ask for addressee, subject, and body
addressee_mail = input('please enter addressee: ') 
subject = input('please enter a subject: ')

#get a long string content
print('plese enter your content, to stop hit ctrl + d')
body = []

while True:
	try:
		line = input()
	except EOFError:
		break
	body.append(line)
body = '\n'.join(body)
		 
the_mail = 'Subject: {}\n\n {}'''.format(subject, body)

try:
	server_mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server_mail.ehlo()
	server_mail.login(user_mail, user_pass)
	server_mail.sendmail(user_mail, addressee_mail, the_mail)
	server_mail.close()
	print('mail send')
	time.sleep(2)
	
except:
	print('something went worng')
