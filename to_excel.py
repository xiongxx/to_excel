# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:52:40 2016

@author: Asual
"""

import xlrd, xlwt, re

txtName = r"raw.txt"
workBook = xlwt.Workbook(encoding = 'ascii')
workSheet = workBook.add_sheet('sheet1')

fp=open(txtName, 'r+b')

row=0
for linea in fp.readlines():
    #print(linea)
    print("00000000")   
    
    str_linea = linea.decode('gb2312', 'ignore').replace('"',"").replace('#',"")
    str_linea = str_linea[:-2]  #str  string
    #print(type(str_linea))
    
    array_str = re.split('\,', str_linea) #component = str_linea.split(',')
    
    print(array_str)
    print(type(array_str))
    
    col=0
    for arr in array_str:
        print(arr)        
        workSheet.write(row, col, arr)
        col += 1
    row +=1
    print("sum =",row)
    if(row == 65536):
       break;
#workSheet.write(2, 0, 1) 

workBook.save('raw.xls')
fp.close()
