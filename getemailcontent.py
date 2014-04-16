#library: gmail,xlwt.
#source: gmail library is from https://github.com/charlierguo/gmail need download and install this library.
#excel library: python has built-in library write and read csv file, xls file can be read and write use xlwt library. 
#xlwt can be download from https://pypi.python.org/pypi/xlwt
#details about gmail library in https://github.com/charlierguo/gmail
#author:xiaohu
# import getemailcontent.py
import sys
sys.path.append('D:/python_stufff/algorithm')
import gmail
from gmail import Gmail
import datetime
import xlwt 	#excel python library
import xlrd    #write excel
import re      #regular expression
import types 
import numpy as np
g = Gmail()
username='xiaohu.zhang@alciouncapital.com'
password='zxh19891119'
g.login(username, password)
g.inbox().mail(unread=True, sender="tony@alciouncapital.com")#sender
data=g.inbox().mail(on=datetime.date(2014, 3, 26))       #date
#print len(data) #number of emails

for i in range(len(data)-1):
    data[i].fetch() #get email
   # print data[i].body #testing and printing email

#-----------------------------------------------------------------------------------------------------------------------#
#each email including contents like attachement is not attached, find all attachments than erase everything before that
maillist=(len(data)-1,2)
indexlist=np.zeros(maillist)

for i in range(5):
    indexlist[i,:]=np.asarray(re.search('Attached',data[i].body).span())

for i in range(len(indexlist)):
    if indexlist[i,0] ==0:
        indexlist=np.delete(indexlist,i,axis=0)
        data[i].body.lstrip(data[i].body[0:indexlist[i,0]])
    #problem with index, index can not be integer
#=================write to excel========================================
'''
wb = xlwt.Workbook()
newsheet= wb.add_sheet('trading_information')
newsheet.write(1,1,tRet)
wb.save('email.xls')
'''

g.logout