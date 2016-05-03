# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals

#----------module import---------

import os
import time
import codecs
import csv

#----------module import----------


#----------function definition----------

def createFile(presentDay,presentTime,categoryName,parameters,pageNum=1):
    'Create file and its name for a certain page'
    
    # check or create a daily dictionary
    dictionaryName = u'TmallData_' + presentDay
    try:
        os.makedirs(dictionaryName)
    except OSError, e:
        if e.errno != 17:
            raise(e)
        
    # create a file and its name for a certain page
    if parameters:
        fileName = ''.join([dictionaryName,'/','tmallPrice','_',presentDay,'_',presentTime,'_',categoryName,'_',parameters,'_',str(pageNum)])
    else:
        fileName = ''.join([dictionaryName,'/','tmallPrice','_',presentDay,'_',presentTime,'_',categoryName,'_',str(pageNum)])
    
    # write the first line
    with codecs.open(fileName,'wb',) as f:
        writer = csv.writer(f)
        writer.writerow(('goodsID','goodsURL','goodsName','shopURL','shopName','price','price_ave','monthly_sales','comments'))
  
    return fileName
#----------function definition----------
        

#----------unit test----------
        
if __name__ == '__main__':
    begin = time.time()
    
    presentDay = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    categoryName = u'酱油'
    parameters = u'&cat=54986001'
    pageNum = 1
    fileName = createFile(presentDay,categoryName, parameters, pageNum)
    print(fileName)
    end = time.time()
    print('time:',end-begin)
    
#----------unit test----------

