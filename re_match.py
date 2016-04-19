# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def deal_sales(sales):
    pattern_ten_th = re.compile('万')
    pattern_num = re.compile('^\d+\.?\d*')
    match = re.search(pattern_ten_th, sales)
    if match:
        match_num = re.search(pattern_num, sales)
        num = int(float(match_num.group(0)) * 10000)
        return num
    else:
        match_num = re.search(pattern_num,sales)
        num = int(match_num.group(0))
        return num


