# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import----------

import time

#----------module import----------


#----------function definition----------

def unparseURL(categoryName,parameters,s=0):
    'Create the page URL'
    
    try:
        urlFirst = u'http://list.tmall.com/search_product.htm?'
        query = ''.join([u'&s=',str(s),u'&q=',categoryName,u'&sort=d']) 
        pageURL = ''.join([urlFirst,query,parameters])
        return pageURL
    except Exception:
        print('unparsing URL error:',(categoryName).encode('utf-8'),(parameters).encode('utf-8'))
        return None
    
#----------function definition----------


#----------unit test----------
    
if __name__ =='__main__':
    
    begin = time.time()
    
    categoryName = u'酱油'
    parameters = u'&cat=54986001'
    pageURL = unparseURL(categoryName, parameters)
    print(pageURL)
    
    end = time.time()
    print('time:',end-begin)
    
#----------unit test---------