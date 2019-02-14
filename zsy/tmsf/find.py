# -*- coding:utf-8 -*-
from selenium import webdriver
from lxml import etree
import requests
import sys
import time
reload(sys)
# asdfasdf??
sys.setdefaultencoding('utf8')
import  re
with open('res.html','rb') as fil:
    response=fil.read()
    html = etree.HTML(response)
    title = html.xpath("//table[@class='tbimg']/tr/td/a/@title")
    print len(title)
    adress = html.xpath("//table[@class='tbimg']/tr/td/font/text()")
    print len(adress)
    # style = html.xpath("//table[@class='tbimg']/tr/td/text()")
    style=re.findall(r'(\d室*?\d厅*?.*?\d卫*?.*?)\s',response)
    print len(style)
    floor = re.findall(r'\d+?/\d+?F', response)
    print len(floor)
    price = html.xpath("//span[@class='f20 orange1']/text()")
    print len(price)
    area = html.xpath("//p[@class='blue1']/text()")
    print len(area)
    for i in style:
        print i
