'''
#Every Python File -->Module -->import keyword -->__name__
import SEPT_10
print(dir(SEPT_10))#dir-->directory will return all available methods,attributes
print(type(SEPT_10.employees))
print(type(SEPT_10.details))
SEPT_10.employees("Durga",designation="Co-founder",location="vizag")
#print(SEPT_10.details.keys())
print(SEPT_10.details['organization'])
SEPT_10.details.update({'batches':['PFS','JFS','DA','AAA','DS'],'employees':240})
print(SEPT_10.details)

#from keyword
from SEPT_10 import employees,details
details.update({'batches':['PFS','JFS','DA','AAA','DS'],'employees':240})
print(details)
print(SEPT_10.__doc__)#returns Doc string from the given module.

'''
#Built-in modules-->math,random,os,time,datetime
#We download modules -->pypi(python packages index
#Build a QRCode Scanner using Python-->Linkedin URL
#pyqrcode,png
#pip install pyqrcode
#pip install png
import pyqrcode
import png
#create a QRcode by giving a link
link="https://ibb.co/PzwrDJXN"
qr=pyqrcode.create(link)
#print(qr)
qr.png("throwback.png",scale=10)
