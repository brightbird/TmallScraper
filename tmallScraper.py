# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-17'

__moduleVersion__ = '2.0'

__doc__ = '''
This is a tmall multithreading scarper,
in order to get scraping time,url,name,price,average price,monthly sales,and comments 
of the goods in the categories list.
'''

#----------module document----------


#----------module import----------

from threading import Thread
import time

from tmallCategoryScraper import tmallCategoryScraper
from categories import CATEGORIES_NAME

#----------module import----------


#----------class definition----------

class ScraperThread(Thread):
    
    def __init__(self,categoryName,**urlParameters):
        self.categoryName = categoryName
        self.urlParameters = urlParameters
        super(ScraperThread,self).__init__()
        
    def run(self):
        tmallCategoryScraper(self.categoryName,**self.urlParameters)
        
#----------class definition----------
        
        
#----------function definition----------  
      
def tmallScraper(categories):
    
    threads =[]
    
    for category in categories:
        
        # parameters
        if type(category)== list:
            categoryName = category[0]
            try:
                if type(category[1]==dict):
                    urlParameters = category[1]
                else:
                    urlParameter = {}
            except IndexError:
                urlParameters = {}
        elif (type(category)== unicode or type(category)==str):
            categoryName = category
            urlParameters = {}
        else:
            print('Error: wrong categories list!!'.encode('utf-8'))
            
        t = ScraperThread(categoryName,**urlParameters)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        

#----------function definition---------- 

#----------main function----------

if __name__ == '__main__':
    start = time.time()
    categories = CATEGORIES_NAME
    tmallScraper(categories)
    end = time.time()
    print('time:',end-start)
#----------main function----------

    