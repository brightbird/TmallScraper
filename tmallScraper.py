# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-26'

__moduleVersion__ = '4.0'

__doc__ = '''
This is a tmall scarper,
in order to get scraping time,url,name,price,average price,monthly sales,and comments 
of the goods in the categories list.
'''

#----------module document----------


#----------module import----------

import time

from tmallCategoryScraper import tmallCategoryScraper
from categories import CATEGORIES_NAME
from scraperThreadPool import scraper

#----------module import----------


#----------function rename----------

scraperFunction = tmallCategoryScraper

#----------function rename----------


#----------function definition----------

def tmallScraper():
    begin = time.time()

    categories = CATEGORIES_NAME
    scraper(scraperFunction, categories)
    
    end = time.time()
    print('time:',end-begin)
    print('Web scraping is over')

#----------function definition----------


#----------main function----------

if __name__ == '__main__':
    tmallScraper()

#----------main function----------



