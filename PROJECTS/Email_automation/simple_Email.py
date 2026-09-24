'''
Python -->Automation -->email Automation -->Google Mail
Simple Mail automation
Mail OTP
Mail with subject&attachments
Bulk Mail

#anht pqyt shch erde
#Simple Mail Automation
#SMTP
import smtplib
#first lets make server connection
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("gurubillidurga@gmail.com","anht pqyt shch erde")
msg="Hello dear.how are you "
server.sendmail("gurubillidurga@gmail.com","anupojumeghana07@gmail.com",msg)
#close the connection
server.quit()
print("sent mail")

#now let's send an otp to mail and validate the scrip
import math
import random
import smtplib
otp=random.randint(1000,9999)
print(otp)
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("gurubillidurga@gmail.com","anht pqyt shch erde")
msg=f'your OTP is {otp}'
server.sendmail("gurubillidurga@gmail.com","gurubillidurga26@gmail.com",msg)
server.quit()
print("sent mail")
validate=int(input('enter the otp:'))
if otp == validate:
    print("sucessfully validate  the otp")
else:
    print("invalid otp")

#now let's send an otp to mail and validate the scrip
import math
import random
import smtplib
digits='1234567890'
otp=''
for i in range(6):
    otp+=digits[math.floor(random.random()*10)]
    #print(otp)
#first lets make server connection
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("gurubillidurga@gmail.com","anht pqyt shch erde")
msg=f'your OTP is {otp}'
print(msg)
server.sendmail("gurubillidurga@gmail.com","anupojumeghana07@gmail.com",msg)
a=input("enter the OTP received")
if a==otp:
    print("Access Granted")
else:
    print("Access Denied")
#close the connection
server.quit()
print("sent mail")

In This case we need to add subject and to addresss for mail
we will use email package
'''
import email
import smtplib
#MIME ->MultiPurpose Interner Mail Extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Now we will provides the details
From="gurubillidurga@gmail.com"
To="gurubillidurga26@gmail.com"
Subject="Python Full Stach Training"
#now we will check all the details and throw it to Multipart
msg=MIMEMultipart()
#print(msg)
#print(type(msg))
msg['From']=From
msg['To']=To
msg['Subject']=Subject
msg['body']="Hey guys ,what are your plan for this week"
msg.attach(MIMEText(msg['body'],'plain'))
text=msg.as_string()
#first lets make server connection
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("gurubillidurga@gmail.com","anht pqyt shch erde")
server.sendmail(From,To,text)
server.quit()
print('sent mail')





















