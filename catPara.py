# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


def catPara(category):
    if type(category)== list:
            categoryName = category[0]
            try:
                if type(category[1]==dict):
                    urlParameters = category[1]
                else:
                    urlParameters = {}
            except IndexError:
                urlParameters = {}
    elif (type(category)== unicode or type(category)==str):
        categoryName = category
        urlParameters = {}
    else:
        print('Error: wrong categories list!!'.encode('utf-8'))
        categoryName = ''
        urlParameters = {}
    return categoryName,urlParameters


if __name__ == '__main__':
    category = [u'电视机',{'cat':'50928001'}]
    categoryName, urlParameters = catPara(category)
    print(categoryName,urlParameters)