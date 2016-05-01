# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#---------module import---------

import random
import time
import codecs

import requests

from scraperHeaders import USER_AGENT_LIST,PROXIES

#----------module import----------


#----------function definition----------

def getPageHTML(pageURL):
    'Request for the HTML of a certain page'
    
    # request head
    userAgent = random.choice(USER_AGENT_LIST)
    proxies = random.choice(PROXIES)
    headers = {
':host':'list.tmall.com',
':method':'GET',
':path':pageURL,
':scheme':'https',
':version':'HTTP/1.1',
'accept':'text/html',
'accept-encoding':'gzip,deflate',
'accept-language':'zh-CN,zh;q=0.8',
'cache-control':'max-age=0',
#'cookie':cookie,
'referer':'https://list.tmall.com',
'user-agent':userAgent,
'http':proxies,
}
    
    # request for the HTML
    try:
        r = requests.get(pageURL,headers)
    except (requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
        print('connect error:',(pageURL).encode('utf-8'))
        return None
    return r.content
    
#-----------function definition----------


#----------unit test----------

if __name__ == '__main__':
    
    begin = time.time()
    
    pageURL = u'http://list.tmall.com/search_product.htm?&s=0&q=酱油&sort=d&cat=54986001'
    html = getPageHTML(pageURL) 
   
    with codecs.open('unitTest_html','wb') as f:
        f.write(html)    
    
    end = time.time()
    print('time:',end-begin)
    
#----------unit test----------