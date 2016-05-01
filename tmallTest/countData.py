# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-26'

__moduleVersion__ = '2.1'

__doc__ = '''
This is a count data module,
in order to summaize CPPdata. 
'''

#----------module document----------

#----------module import----------

# import system modules
import os
import time

#----------module import----------

#----------class definition----------

class CountData(object):
    def __init__(self,data):
        self.data = data
    
    def dictSummary(self,printout=True):
        
        dicts = os.listdir(os.getcwd())
        for dict in dicts:
            if (self.data in dict) and ('.rar' not in dict):
                summarySet = self.fileNameSummary(dict)
                paraDict = self.paraSummary(summarySet)
                categoryDict = self.categorySummary(summarySet)
                if printout:
                    print('-'*40)
                    print(dict)
                    print('file number:',len(summarySet))
                    print('parameter number:',len(paraDict))
                    print('category number',len(categoryDict))
                    print('-'*40)
                else:
                    self.writeParaSummary(dict,paraDict)
                    self.writeCateSummary(dict,categoryDict)
            
    def fileNameSummary(self,dict):
        dataDict = os.listdir(dict)
        summaryList = []
        for file in dataDict:
            fileListImproved = []
            fileList = file.split('_')
            del fileList[0]
            for i in fileList:
                if '-' not in i:
                    fileListImproved.append(i)
            para = fileListImproved[1:-1]
            del fileListImproved[1:-1]
            fileListImproved.insert(1,''.join(para))
            fileTuple = tuple(fileListImproved)
            summaryList.append(fileTuple)
        summarySet = set(summaryList)
        return summarySet
            
    def paraSummary(self,summarySet):
        paraDict = {}
        for item in summarySet:
            key = item[0:2]
            if key in paraDict.keys():
                paraDict[key] += 1
            else:
                paraDict[key] = 1
        return paraDict     
    
    def categorySummary(self,summarySet):
        categoryDict = {}
        for item in summarySet:
            key = item[0]
            if key in categoryDict.keys():
                categoryDict[key] += 1
            else:
                categoryDict[key] = 1
        return categoryDict 
    
    def writeParaSummary(self,dict,paraSet):
        
        # create dictionary 
        dictionaryName = 'stat'
        try:
            os.makedirs(dictionaryName)
        except OSError, e:
            if e.errno != 17:
                raise(e)
            
        # create file
        fileName = 'stat/'+dict + '_parameter' 
        if fileName in os.listdir(os.getcwd()):
            return None
        else:
            with open(fileName,'wb') as f:
                f.write('categoryName,paraName,number,\n')
                
            for item in paraSet.items():
                with open(fileName,'ab') as f:
                    f.write(item[0][0])
                    f.write(',')
                    f.write(item[0][1])
                    f.write(',')
                    f.write(str(item[1]))
                    f.write(',')
                    f.write('\n')
                    
    def writeCateSummary(self,dict,paraSet):
        
        # create dictionary 
        dictionaryName = 'stat'
        try:
            os.makedirs(dictionaryName)
        except OSError, e:
            if e.errno != 17:
                raise(e)
            
        # create file
        fileName = 'stat/'+dict + '_category' 
        if fileName in os.listdir(os.getcwd()):
            return None
        else:
            with open(fileName,'wb') as f:
                f.write('categoryName,number,\n')
                
            for item in paraSet.items():
                with open(fileName,'ab') as f:
                    f.write(item[0])
                    f.write(',')
                    f.write(str(item[1]))
                    f.write(',')
                    f.write('\n')
                              

#----------class definition----------


#----------function definition----------

def countData(*datas):
    for data in datas:
        summary = CountData(data)
        summary.dictSummary(printout=False)

#----------function definition----------


#----------main function----------

if __name__=='__main__':
    begin = time.time()
    
    # datas = ('TmallData',)
    datas = ('TmallData','JDData')
    countData(*datas)
    
    end = time.time()
    print('time:',end-begin)
    input('finish')
    
#----------main function----------


