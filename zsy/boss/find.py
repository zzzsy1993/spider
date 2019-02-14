# -*- coding:utf-8 -*-
from selenium import webdriver
from lxml import etree
import requests
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
import  re
with open('result.html','rb') as fil:
    response=fil.read()
    html = etree.HTML(response)
    title = html.xpath("//div[@class='job-title']/text()")
    price = html.xpath("//span[@class='red']/text()")
    info=html.xpath('//div[@class="info-primary"]/p/text()')
    company=html.xpath('//div[@class="info-company"]/div/h3/a/text()')
    print company[0]
    # adress = html.xpath("//table[@class='tbimg']/tr/td/font/text()")
    # print len(adress)
    # # style = html.xpath("//table[@class='tbimg']/tr/td/text()")
    # style=re.findall(r'(\d室*?\d厅*?.*?\d卫*?.*?)\s',response)
    # print len(style)
    # floor = re.findall(r'\d+?/\d+?F', response)
    # print len(floor)

    # print len(price)
    # area = html.xpath("//p[@class='blue1']/text()")
    # print len(area)
    # for i in style:
    #     print i
