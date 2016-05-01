# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import----------

import time

from tmallScraper import *
from tmallCategoryScraper import *
from categories import CATEGORIES_NAME #categories --> your list
from catPara import catPara

#----------module import----------


#----------function definition----------

def unit_test():
    'complete test'
    tmallScraper(CATEGORIES_NAME)


def unit_test_1():
    'test one page of a category with one thread'
    for category in CATEGORIES_NAME:
        categoryName = category[0]
        urlPara = category[1]
        tmallPageScraper(categoryName,**urlPara)
        
        
def unit_test_para():
    'test the paramater groups'
    for category in CATEGORIES_NAME:
        categoryName,urlPara = catPara(category)
        test_scraper = ScraperProducer(categoryName,**urlPara)
        
#----------function definition----------


#----------main function----------

if __name__=='__main__':
    #unit_test()
    #unit_test_1()
    unit_test_para()
    input('finish')
    
#----------main function----------
