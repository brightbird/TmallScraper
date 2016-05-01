# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import----------

import time

from categories import CATEGORIES_NAME
from tmallCategoryScraper import *
from scraperThreadPool import scraper

#----------module import----------


#----------function definition----------

def testPara(categoryName,**urlPara):
    scraper=PageScraper(categoryName,**urlPara)
    scraper.getTotalPageNumber()
    
    
def testList():
    function = testPara
    categories = CATEGORIES_NAME
    scraper(function,categories)
    
    
#----------function definition---------


#----------main function----------

if __name__ == '__main__':
    testList()

#----------main function----------

