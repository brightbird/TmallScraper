#!/usr/bin/env python
# encoding=utf-8


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-17'

__moduleVersion__ = '2.0'

__doc__ = '''
This is a IP checker,
in order to check IP proxies.
'''

#----------module document----------


#----------module import----------

# import system module
import codecs
import time

# import third-party module
import requests
from bs4 import BeautifulSoup

#----------module import----------

#----------global variables----------

url = 'https://www.tmall.com/'
#url = 'http://www.jd.com/allSort.aspx'

#----------global variables----------


#----------function definition----------

def requestsCheck(ip_proxy):
    r = requests.get(url,ip_proxy,timeout=0.05)
    if r.status_code==200:
        return True
    else:
        return False


def ipChecker():
    with codecs.open('proxiesList','rb') as f:
        ip_list = f.readlines()
        
    with codecs.open('ipProxiesList','ab') as ff:
        for ip_proxy in ip_list:
            try:
                if requestsCheck(ip_proxy):
                    print 'Success:',ip_proxy
                    ff.write(ip_proxy)
            except:
                print "Fail:",ip_proxy
                continue
            
#----------function definition----------   
                
#----------main function----------     
          
if __name__ == '__main__':
    start = time.time()
    ipChecker()
    end = time.time()
    print 'time:',(start-end)
    
#----------main function----------
        