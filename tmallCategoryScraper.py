# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals



#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-19'

__moduleVersion__ = '6.3'

__doc__ = '''
This is a tmall category scarper,
in order to get scraping time,url,name,price,average price,monthly sales,and comments 
of the goods in a certain category.
'''

#----------module document----------


#----------module import----------

# import system module
import os
import codecs
import time
import csv
import random 

# import third-party module
import requests
from bs4 import BeautifulSoup

# import my own module
from scraperHeaders import USER_AGENT_LIST,PROXIES
from re_match import deal_sales
from getParameter import getParameter
from createFile import createFile
from unparseURL import unparseURL
from getPageHTML import getPageHTML 
from getTotalPageNumber import getTotalPageNumber  

#----------module import----------


#----------class definition----------

class PageScraper(object):
    'a page scraper for the Tmall scraper'
    
    def __init__(self,categoryName,pageNum = 1,**urlParameter):
        'Define attributes for ScraperProducer'
        
        self.presentDay = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.presentTime = str(time.strftime('%H-%M-%S',time.localtime(time.time())))
        self.logTime = '[{} {}]'.format(self.presentDay,str(time.strftime('%H:%M:%S',time.localtime(time.time()))))

        self.categoryName = categoryName
        self.pageNum = pageNum
        self.parameters = getParameter(**urlParameter)
        self.pageURL = unparseURL(categoryName,self.parameters,(pageNum-1)*60)
        self.html = getPageHTML(self.pageURL)
        
    def getTotalPageNumber(self):
        'Get total page number for a certain category'
        
        if self.html == None:
            return None
        
        try:
            soup = BeautifulSoup(self.html,'html.parser')
            div_page = soup.body.find('div',attrs={'class','page'})
            div_content = div_page.find('div',attrs={'id':'content'})
            div_filter = div_content.find('div',attrs={'class':'filter clearfix'})
            p_ui = div_filter.find('p',attrs={'class':'ui-page-s'})
            pageNumber = p_ui.find('b',attrs={'class':'ui-page-s-len'}).getText().split('/')[1]
            return int(pageNumber)                                  
        except Exception:
            print(self.logTime,',fail to get page number:',(self.pageURL).encode('utf-8'))
            return None
    
    def parsePageHTML(self):
        'Parse the HTML'
        
        if self.html == None:
            return None
        
        fileName = createFile(self.presentDay,self.presentTime,self.categoryName,self.parameters,self.pageNum)
    
        # parse the HTML
        try:
            soup = BeautifulSoup(self.html,'html.parser')
            div_content = soup.body.find('div',attrs={'class':'page'}).find('div',attrs={'class':'content'})
            products = soup.find_all('div',attrs={'class':'product-iWrap'})
            if products == None:
                print(self.logTime,',parse error:',(fileName).encode('utf-8'))
                return None
        except Exception:
            print(self.logTime,',parse error:',(fileName).encode('utf-8'))
        
        # parse the data
        __i__ = 1
        for product in products:
            
            try:
                goodsID = product.find('p',attrs = {'class':'productStatus'}).find_all('span')[-1]['data-item']
            except:
                goodsID = None
           
            try:
                goodsURL = product.find('div',attrs={'class':'productImg-wrap'}).find('a')['href']
                goodsURL =''.join(['http:',goodsURL])
            except:
                goodsURL = None
                
            try:
                goodsName = product.find('p',attrs={'class':'productTitle'}).find('a')['title'].encode('utf-8')
            except AttributeError:
                try:
                    goodsNameList = []
                    a = product.find('div',attrs={'class':'productTitle productTitle-spu'}).find_all('a')
                    for text in a:
                        text = text.getText()
                        text = ''.join(text.split('\n')).split('\r')
                        text = ''.join(text).split(' ')[0]
                        goodsNameList.append(text)
                    goodsName = '_'.join(goodsNameList).encode('utf-8')
                except Exception:
                    goodsName = None
            except Exception:
                goodsName = None
                
            try:
                shopURL = product.find('div',attrs={'class':'productShop'}).find('a')['href']
                shopURL = ''.join(['http:',shopURL]).encode('utf-8')
           
            except:
                shopURL = None
                
            try:
                shopName = product.find('div',attrs={'class':'productShop'}).find('a').getText()
                shopName = ''.join(shopName.split('\r')).split('\n')[1].encode('utf-8')
            except:
                shopName = None
 
            try:
                price = product.find('p',attrs={'class':'productPrice'}).em['title']
            except:
                price = None
                
            try:
                price_ave = product.find('span',attrs={'class':'productPrice-ave'}).getText().encode('utf-8')
            except:
                price_ave = None
                
            try:
                monthly_sales = product.find('p',attrs={'class':'productStatus'}).em.getText().encode('utf-8')
                monthly_sales = deal_sales(monthly_sales)
            except:
                monthly_sales = None
                
            try:
                comments = product.find('p',attrs={'class':'productStatus'}).a.getText().encode('utf-8')
                comments = deal_sales(comments)
            except:
                comments = None

            # write the data
            try:
                with codecs.open(fileName,'ab') as f:
                    writer = csv.writer(f)
                    writer.writerow((goodsID,goodsURL,goodsName,shopURL,shopName,price,price_ave,monthly_sales,comments))
            except:
                __i__ = 0
        
        # print write error
        if __i__ == 0:        
            print(self.logTime,',write error:',(fileName).encode('utf-8'))

#----------class definition----------


#----------function definition----------

def tmallPageScraper(categoryName,page=1,**urlParameter):
    'A scraper for a certain page of a certain category'
    
    # produce the html
    scraper = PageScraper(categoryName,page,**urlParameter)
    # consume the html
    scraper.parsePageHTML()
    
    return scraper.totalPages


def tmallCategoryScraper(categoryName,**urlParameter):
    'A scraper for a certain category'
    
    scraper = PageScraper(categoryName,**urlParameter)
    scraper.parsePageHTML()
    number = scraper.getTotalPageNumber()
    if number:
        #print('%s: page 1'%(categoryName))
        number += 1
        for i in xrange(2,number):
            scraper = PageScraper(categoryName,i,**urlParameter)
            scraper.parsePageHTML()
            #print('%s: page %d'%(categoryName,i))
            
#----------function definition----------


#----------main function----------

if  __name__ == '__main__':
    print('-'*40)
    begin = time.time()
    categoryName = u'笔记本电脑'
    urlParameter = {'cat':'50024399'}
    #categoryName = u'酱油' #u'%BD%B4%D3%CD'
    #urlParameter = {'cat':u'50099300'}
    #tmallPageScraper(categoryName,**urlParameter)
    tmallCategoryScraper(categoryName,**urlParameter)
    print('finish:',categoryName.encode('utf-8'))
    end = time.time()
    print('time:',(end-begin))
    print('-'*40)
    
#----------main function----------



