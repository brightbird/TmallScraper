#!/usr/bin/env python
# encoding=utf-8


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-17'

__moduleVersion__ = '2.0'

__doc__ = '''
This is a xici IP scarper,
in order to get IP proxies from http://www.xicidaili.com/nn/
'''

#----------module document----------


#----------module import----------

# import system module
import re
import codecs
import time

# import third-party module
import requests
from bs4 import BeautifulSoup

#----------module import----------


#----------global variables----------

URL = 'http://www.xicidaili.com/nn/'
headers = {
           'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
           'http':'http://110.76.38.173:6666'
           }
IP = r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))'
PORT = r'^([0-9]{1,4}|[1-5][0-9]{4}|6[0-5]{2}[0-3][0-5])$'

#----------global variables----------


#----------function definition----------

def get_ip_html(url):
    try:
        r = requests.get(url,headers=headers)
        #print 'Connect' #r.status_code
        html = r.content
        return html
    except:
        print 'connected error'
        return None


def parse_ip_html(html):
    if html == None:
        return None
    ip_list = []
    soup = BeautifulSoup(html,'lxml')
    ip_table = soup.find('table')
    td_list = list(ip_table.children)
    for td1 in td_list:
        try:
            for td2 in td1.find_all('td'):
                td_text = td2.get_text()
                try:
                    if re.match(IP,td_text):
                        ip = td_text

                    elif re.match(PORT,td_text):
                        port = td_text

                    ip_proxy = 'http://'+ ip + ':' + port
                    if not ip_proxy in ip_list:
                        ip_list.append(ip_proxy)
                except:
                    continue
                
        except:
            continue

    next_page = soup.find('div',attrs={'class':'pagination'}).find('a',attrs={"rel":'next'})
    if next_page:
        return ip_list,'http://www.xicidaili.com/'+next_page['href']
    return ip_list,None


def write_ip(ip_list):
    with codecs.open('proxiesList','ab') as f:
        for ip in ip_list:
            f.write(ip)
            f.write('\n')
        #print 'Finished'


def getIP():
    print '-'*34 + 'IP Scraping' + '-'*34
    url = URL
    while url:
        html = get_ip_html(url)
        ip_list,url = parse_ip_html(html)
        write_ip(ip_list)
    print '-'*34 + 'IP Scraping' + '-'*34
    
#----------function definition----------


#----------main function----------

if __name__ =='__main__':
    begin = time.time()
    getIP()
    end = time.time()
    print 'time:',end-begin

#----------main function----------