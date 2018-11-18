#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: WU Xiaotong time:2018/11/6

from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen

from common import constants
from config import spider_log
from public_spider import PublicSpider

LOG = spider_log.spider_logger()


class ZhihuSpider(PublicSpider):
    def __init__(self):
        pass


try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bsObj = BeautifulSoup(html.read(), features="html.parser")
    # print(bsObj.h1)
    # print(bsObj.head)
    # print(bsObj.body)
except HTTPError:
    print("Error")

try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bsObj = BeautifulSoup(html, features="html.parser")
    # findAll(tagName, tagAttributes)
    nameList = bsObj.findAll("span", {"class": "green"})
    for name in nameList:
        print(name.get_text())
except HTTPError:
    print("error")

    # book #34
