# -*- coding:utf-8 -*-
from selenium import webdriver
from lxml import etree
import requests
import sys
import re,csv
reload(sys)
sys.setdefaultencoding('utf8')
base_url = 'https://www.zhipin.com/c101210100-p100901/b_%E8%A5%BF%E6%B9%96%E5%8C%BA-h_101210100/?'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

end = int(raw_input('几页'))
for i in range(end):
    data = {
        'query': 'python',
        'page': i + 1
    }
    response = requests.get(base_url, params=data, headers=user_agent)
    html=etree.HTML(response.content)
    # with open('result.html','wb+') as fil:
    #     fil.write(response.content)
    # title = html.xpath("//table[@class='tbimg']/tr/td/a/@title")
    title = html.xpath("//div[@class='job-title']/text()")
    price = html.xpath("//span[@class='red']/text()")
    info = html.xpath('//div[@class="info-primary"]/p/text()')
    company = html.xpath('//div[@class="info-company"]/div/h3/a/text()')
    out = open('res.csv', 'a')
    csv_write = csv.writer(out, dialect='excel')
    for i in range(len(title)):
        lis=[title[i].strip(),price[i].strip(),info[3*i],info[3*i+1],info[3*i+2],company[i]]
        csv_write.writerow(lis)