# -*- coding:utf-8 -*-

import requests, json, csv, urllib, sys, time, datetime
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf8')


class LianJiaSpider(object):
    def __init__(self):
        self.base_url = 'https://hz.lianjia.com/zufang/pg%d'
        self.headers = {

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'select_city=330100; all-lj=3d0b35ab17a07d475f1852d271de56f8; lianjia_uuid=9f4a138b-9482-4e5a-9d5a-85400f05edcd; UM_distinctid=163f7c6a1a33df-05a9a8e77e67e7-3e70055f-1b2180-163f7c6a1a4bb3; _jzqy=1.1528870380.1528870380.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; _jzqckmp=1; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1528870380; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1528870391; _smt_uid=5b20b5eb.36a62577; CNZZDATA1253492436=779546538-1528868258-https%253A%252F%252Fwww.baidu.com%252F%7C1528868258; CNZZDATA1254525948=1604095059-1528867599-https%253A%252F%252Fwww.baidu.com%252F%7C1528867599; CNZZDATA1255633284=1992649578-1528866475-https%253A%252F%252Fwww.baidu.com%252F%7C1528866475; CNZZDATA1255604082=144980995-1528869703-https%253A%252F%252Fwww.baidu.com%252F%7C1528869703; _qzja=1.1188379151.1528870380123.1528870380123.1528870380123.1528870380123.1528870391499.0.0.0.2.1; _qzjb=1.1528870380123.2.0.0.0; _qzjc=1; _qzjto=2.1.0; _jzqa=1.933721594748306.1528870380.1528870380.1528870380.1; _jzqc=1; _jzqb=1.2.10.1528870380.1; _ga=GA1.2.1566435740.1528870382; _gid=GA1.2.1396306159.1528870382; lianjia_ssid=f89e3f8e-5d66-4081-85a6-0b328105fc92',
            'Host': 'hz.lianjia.com',
            'Referer': 'https://hz.lianjia.com/zufang/',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        }
        self.page_num = 100
        self.page = 1

    def send_request(self, url, referer):
        self.headers['Referer'] = referer
        try:
            response = requests.get(url, headers=self.headers)
            return response

        except Exception as e:
            print e

    def link(self, content):
        html = etree.HTML(content)
        return html.xpath('//ul[@id="house-lst"]/li/div[2]/h2/a/@href')

    def write(self, response):
        html = etree.HTML(response.content)
        city = "杭州"
        try:
            district = html.xpath('//div[@class="zf-room"]/p[7]/a[1]/text()')[0]
        except:
            district = '暂无数据'
        # block = html.xpath('')[0]
        try:
            cell_name = html.xpath('//div[@class="zf-room"]/p[6]/a[1]/text()')[0]
        except:
            cell_name = '暂无数据'
        # cell_address = html.xpath('')[0]
        try:
            house_type = html.xpath('//div[@class="zf-room"]/p[2]/text()')[0].split('  ')[0]
        except:
            house_type = '暂无数据'
        try:
            area = html.xpath('//div[@class="zf-room"]/p[1]/text()')[0]
        except:
            area = '暂无数据'
        try:
            decoration = html.xpath('//span[@class="tips decoration"]/text()')[0]
        except:
            decoration = '暂无数据'
        try:
            face = html.xpath('//div[@class="zf-room"]/p[4]/text()')[0]
        except:
            face = '暂无数据'
        try:
            price = html.xpath('//span[@class="total"]/text()')[0]
        except:
            price = '暂无数据'
        try:
            pay_way = html.xpath('//div[@class="content"]/ul/li[2]/text()')[1].strip()
        except:
            pay_way = '暂无数据'
        try:
            jjr_name = html.xpath('//a[@class="name LOGCLICK"]/text()')[0]
            jjr_phone = html.xpath('//div[@class="brokerInfoText"]/div[@class="phone"]/text()')[0].strip() + "转" + \
                        html.xpath('//div[@class="brokerInfoText"]/div[@class="phone"]/text()')[1].strip()
        except:
            jjr_name = '暂无数据'
            jjr_phone = '暂无数据'
        try:
            floor = html.xpath('//div[@class="zf-room"]/p[3]/text()')[0]
            rental_method = html.xpath('//div[@class="zf-room"]/p[2]/text()')[0].split('  ')[1]
        except:
            floor = '暂无数据'
            rental_method = '暂无数据'
        from_web = "链家"
        from_url = response.url
        try:
            house_id = html.xpath('//span[@class="houseNum"]/text()')[0]
        except:
            house_id = '暂无数据'
        try:
            release_time = html.xpath('//div[@class="zf-room"]/p[8]/text()')[0]
        except:
            release_time = '暂无数据'
        try:
            image = html.xpath('//div[@class="imgContainer"]/img/@src')[0]
        except:
            image = '暂无数据'
        try:
            introduce = html.xpath('//div[@class="title"]/div[@class="sub"]/text()')[0]
        except:
            introduce = '暂无数据'
        try:
            title = html.xpath('//h1[@class="main"]/text()')[0]
        except:
            title = '暂无数据'
        try:
            is_sell = html.xpath('//div[@class="base"]/div[@class="content"]/ul/li[3]/text()')[0]
        except:
            is_sell = '暂无数据'
        crawl_time = datetime.datetime.utcnow()
        lis = [city,
               district,
               # block,
               cell_name,
               house_type,
               area,
               decoration,
               face,
               price,
               pay_way,
               jjr_name,
               jjr_phone,
               floor,
               rental_method,
               from_web,
               from_url,
               house_id,
               release_time,
               image,
               introduce,
               title,
               is_sell,
               crawl_time]
        csvwrite = csv.writer(self.file, dialect='excel')
        csvwrite.writerow(lis)

    def manage(self):
        self.file = open('res.csv', 'w')
        for i in range(self.page_num):
            for link in self.link(self.send_request(self.base_url % self.page, self.base_url % (
                    self.page - 1) if self.page > 1 else 'https://hz.lianjia.com/zufang/').content):
                self.write(self.send_request(link, self.base_url % self.page))
            self.page += 1
        self.file.close()


if __name__ == '__main__':
    a = LianJiaSpider()
    a.manage()
