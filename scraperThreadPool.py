# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-17'

__moduleVersion__ = '1.0'

__doc__ = '''
This is a multithreading scarper pool.
'''

#----------module document----------


#----------module import----------

# import system modules
import Queue
from threading import Thread
import time

# import my own modules
from tmallCategoryScraper import tmallCategoryScraper
from categories import CATEGORIES_NAME
from catPara import catPara

#----------module import----------


#----------class definition----------

class ScraperManager(object):
    'The Manager of the Scraper'
    
    def __init__(self,function,categories,threadNum=100):
        self.workQueue = Queue.Queue()
        self.threads = []
        self.jobNum = len(categories)
        self.__initWorkQueue(function,categories,self.jobNum)
        self.__initThreadPool(threadNum)
        
    def __initThreadPool(self,threadNum):
        for i in range(threadNum):
            self.threads.append(ScraperWorker(self.workQueue))

    def __initWorkQueue(self,function,categories,jobNum):
        for i in range(jobNum):
            self.addJob(scraperFunc,function,categories[i])
            
    def addJob(self,func,args1,arg2):
        self.workQueue.put((func,args1,arg2))
        
    def checkQueue(self):
        return self.workQueue.qsize()
    
    def waitAllComplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()


class ScraperWorker(Thread):
    'The Worker of the Scraper'
    
    def __init__(self,workQueue):
        Thread.__init__(self)
        self.workQueue = workQueue
        self.start()
        
    def run(self):
        while True:
            try:
                do,args1,arg2 = self.workQueue.get(block=False)
                do(args1,arg2)
                self.workQueue.task_done()
            except Exception,e:
                print(e)
                break
        
#----------class definition----------
        
        
#----------function definition----------

def scraperFunc(function,category):
    categoryName,urlPara = catPara(category)
    function(categoryName,**urlPara)

    
def scraper(function,categories,n=100):
    threadNum = len(categories)
    if threadNum > n:
        threadNum = n
    workManager = ScraperManager(function,categories,threadNum)
    workManager.waitAllComplete()
    
#----------function definition---------- 


#----------main function----------

if __name__ == '__main__':
    start = time.time()
    function = tmallCategoryScraper
    categories = CATEGORIES_NAME
    scraper(function,categories)
    end = time.time()
    print('time:',end-start)
    print('Web scraping is over')
#----------main function----------