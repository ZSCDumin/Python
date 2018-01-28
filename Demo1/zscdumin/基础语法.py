#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-25 16:41:09
# @Author  : 杜敏 (2712220318@qq.com)
# @Link    : https://github.com/ZSCDumin
# @Version : $Id$

import os
import re
import requests
from bs4 import BeautifulSoup
from base64 import *
from math import sqrt
import tushare as ts
# k = int(input("enter a number:"))
# if k == 0:
#     print(0)
# elif k == 1:
#     print(1)
# else:
#     print(2)
# list = range(5, 10, 1)  # 前闭后开，最后一个参数表示步长
# list1 = range(5, 5)  # 无输出
# for c in list1:
#     print(c)
# k = sqrt(4)
# def fun(k=True):
#     if k:
#         print("True")
#     else:
#         print("False")
# fun(k=False)
# s='dumin'
# print(s.encode('utf-8'))
# lf = [('AXP', 'American Express Company', '86.40'),('BA', 'The Boeing Company', '122.64')]
# print(lf)
# aDict = {}
# for data in lf:
#     aDict[data[0]] = data[2]
# print(aDict)

# ts.get_h_data('600848',start='2017-03-01',end='2017-03-08')
# r=requests.get("https://www.baidu.com")
# r.encoding='utf-8'
# print(r.text)

# url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
# try:
# 	kv={'user-agent':'Mozilla/5.0'}
# 	r=requests.get(url,headers=kv)
# 	r.raise_for_status()
# 	r.encoding=r.apparent_encoding
# 	print(r.text[1:1000])
# except:
# 	print("爬虫失败")

# kv={'wd':'Python'}
# r=requests.get("https://www.baidu.com/s",params=kv)
# print(r.status_code)
# print(r.request.url)
# soup=BeautifulSoup('<p>Data</p>','html.parser')
# print(soup.prettify())
