# -*- coding:utf-8 -*-
from selenium import webdriver
from lxml import etree
import requests
import sys
import re,csv

reload(sys)
sys.setdefaultencoding('utf8')

base_url = 'http://www.tmsf.com/esf/search_cz.htm?'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

class Bu:
    def findChinese(self, text):
        if isinstance(text, unicode):
            return ''
        text = text.decode('utf8')
        res = re.findall(u"[\u4e00-\u9fa5\u3001\u3002]", text)
        return res


    def myAlign(self, un_align_str, lenh=0, lenf=0, addh=' ', addf='　'):
        assert isinstance(lenh, int)
        assert isinstance(lenf, int)
        if (lenh + lenf * 2) <= len(un_align_str):
            return un_align_str
        strlen = len(un_align_str)
        chn = self.findChinese(un_align_str)
        numchn = len(chn)
        numsph = strlen - numchn * 3
        str = addh * (lenh - numsph) + addf * (lenf - numchn)
        return str

end = int(raw_input('几页'))
bu=Bu()
for i in range(end):
    data = {
        'page': i + 1
    }
    response = requests.get(base_url, params=data, headers=user_agent)
    html=etree.HTML(response.content)
    title = html.xpath("//table[@class='tbimg']/tr/td/a/@title")
    adress = html.xpath("//table[@class='tbimg']/tr/td/font/text()")
    # style = html.xpath("//table[@class='tbimg']/tr/td/text()")
    style = re.findall(r'(\d室*?\d厅*?.*?\d卫*?.*?)\s', response.content)
    floor = re.findall(r'\d+?/\d+?F', response.content)
    price = html.xpath("//span[@class='f20 orange1']/text()")
    area = html.xpath("//p[@class='blue1']/text()")
    out = open('res.csv', 'a')
    csv_write = csv.writer(out, dialect='excel')
    for i in range(len(title)):
        lis=[title[i].strip(),adress[i].strip(),style[i],floor[i],price[i],re.search('\d+',area[i]).group()]
        csv_write.writerow(lis)