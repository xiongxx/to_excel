# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:52:40 2016

@author: Asual
"""

import re
from openpyxl import Workbook


txtName = r"raw.txt"
workBook = Workbook(encoding = 'ascii')
workSheet = workBook.active

fp=open(txtName, 'r+b')

row=0
for linea in fp.readlines():
    #print(linea)      
    
    str_linea = linea.decode('gb2312', 'ignore').replace('"',"").replace('#',"")
    str_linea = str_linea[:-2]  #str  string
    #print(type(str_linea))
    
    array_str = re.split('\,', str_linea) #component = str_linea.split(',')
    
    #print(array_str)     
      
    workSheet.append(array_str)
        
    row +=1
    print("sum =",row)

workBook.save('raw.xls')
fp.close()
