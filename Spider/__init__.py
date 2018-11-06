#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WU Xiaotong time:2018/11/6
import logging

from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen


try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())
except HTTPError:
    print("Error")

bsObj = BeautifulSoup(html.read(), features="html.parser")
print(bsObj.h1)
print(bsObj.head)

