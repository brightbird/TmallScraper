# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-17'

__moduleVersion__ = '3.0'

__doc__ = '''
This is a tmall multithreading scarper,
in order to get scraping time,url,name,price,average price,monthly sales,and comments 
of the goods in the categories list.
'''

#----------module document----------


#----------module import----------

import Queue
from threading import Thread
import time

from tmallCategoryScraper import tmallCategoryScraper
from categories import CATEGORIES_NAME
from catPara import catPara

#----------module import----------


#----------class definition----------

class ScraperManager(object):
    'The Manager of the Scraper'
    
    def __init__(self,categories,threadNum=100):
        self.workQueue = Queue.Queue()
        self.threads = []
        self.jobNum = len(categories)
        self.__initWorkQueue(self.jobNum)
        self.__initThreadPool(threadNum)
        
    def __initThreadPool(self,threadNum):
        for i in range(threadNum):
            self.threads.append(ScraperWorker(self.workQueue))

    def __initWorkQueue(self,jobNum):
        for i in range(jobNum):
            self.addJob(scraperFunc,categories[i])
            
    def addJob(self,func,args):
        self.workQueue.put((func,args))
        
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
                do,args = self.workQueue.get(block=False)
                do(args)
                self.workQueue.task_done()
            except Exception,e:
                print(e)
                break
        
#----------class definition----------
        
        
#----------function definition----------

def scraperFunc(category):
    categoryName,urlPara = catPara(category)
    tmallCategoryScraper(categoryName,**urlPara)

    
def tmallScraper(categories,n=100):
    threadNum = len(categories)
    if threadNum > n:
        threadNum = n
    workManager = ScraperManager(categories,threadNum)
    workManager.waitAllComplete()
    
#----------function definition---------- 


#----------main function----------

if __name__ == '__main__':
    start = time.time()
    categories = CATEGORIES_NAME
    tmallScraper(categories)
    end = time.time()
    print('time:',end-start)
    print('Web scraping is over')
#----------main function----------

    
