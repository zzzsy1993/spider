# -*- coding:utf-8 -*-

import requests, json, csv, urllib, sys, time, datetime, re
from lxml import etree
from threading import Thread

reload(sys)
sys.setdefaultencoding('utf8')


class ZiroomSpider(object):
    def __init__(self):
        self.base_url = 'http://hz.ziroom.com/z/nl/z3.html?p=%d'
        self.headers = {

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'CURRENT_CITY_CODE=330100; gr_user_id=4f32b5d1-0fc8-44ac-aab8-14b8d2e290bb; Hm_lvt_038002b56790c097b74c818a80e3a68e=1528945675; mapType=%20; PHPSESSID=1adhkfqsingqr2ukmovfl3mv03; CURRENT_CITY_NAME=%E6%9D%AD%E5%B7%9E; gr_session_id_8da2730aaedd7628=b3b9be3b-4f19-4bc0-b244-e6c375098cce_true; HZ_nlist=%7B%2261342192%22%3A%7B%22id%22%3A%2261342192%22%2C%22sell_price%22%3A1830%2C%22title%22%3A%22%5Cu4f59%5Cu676d%5Cu4e54%5Cu53f81%5Cu53f7%5Cu7ebf%5Cu7fc1%5Cu6885%5Cu91d1%5Cu5730%5Cu827a%5Cu58835%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528956489%2C%22usage_area%22%3A15.3%2C%22floor%22%3A%2212%22%2C%22floor_total%22%3A%2217%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F01%5C%2F73%5C%2FChAFfVsasmKAQoVJAAJIRaLeMrI591.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2261318412%22%3A%7B%22id%22%3A%2261318412%22%2C%22sell_price%22%3A2130%2C%22title%22%3A%22%5Cu6c5f%5Cu5e72%5Cu706b%5Cu8f66%5Cu4e1c%5Cu7ad94%5Cu53f7%5Cu7ebf%5Cu666f%5Cu82b3%5Cu666f%5Cu82b3%5Cu4e00%5Cu533a4%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528955565%2C%22usage_area%22%3A11.9%2C%22floor%22%3A%224%22%2C%22floor_total%22%3A%227%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F04%5C%2FB5%5C%2FChAFD1scoxyAXGhrAAJ_WzbqONo776.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2261284128%22%3A%7B%22id%22%3A%2261284128%22%2C%22sell_price%22%3A5190%2C%22title%22%3A%22%5Cu4e0b%5Cu6c99%5Cu9ad8%5Cu6559%5Cu56ed%5Cu533a%5Cu897f1%5Cu53f7%5Cu7ebf%5Cu6587%5Cu6cfd%5Cu8def%5Cu548c%5Cu8fbe%5Cu57ce2%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528949063%2C%22usage_area%22%3A11.9%2C%22floor%22%3A%223%22%2C%22floor_total%22%3A%2233%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2FD9%5C%2F95%5C%2FChAFD1sEwP6AGvT5ABAKTNEFij4096.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2260783029%22%3A%7B%22id%22%3A%2260783029%22%2C%22sell_price%22%3A1830%2C%22title%22%3A%22%5Cu897f%5Cu6e56%5Cu7533%5Cu82b12%5Cu53f7%5Cu7ebf%5Cu4e09%5Cu58a9%5Cu9996%5Cu5f00%5Cu56fd%5Cu98ce%5Cu7f8e%5Cu57df5%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528946584%2C%22usage_area%22%3A12.4%2C%22floor%22%3A%2227%22%2C%22floor_total%22%3A%2231%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2FF4%5C%2F75%5C%2FChAFD1sTuTqAKeEfABWAq795LQA043.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%7D; Hm_lpvt_038002b56790c097b74c818a80e3a68e=1528956488',
            'Host': 'hz.ziroom.com',
            'Referer': '',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

        }
        self.page_num = 50
        self.page = 45

    def send_request(self, url, referer):
        self.headers['Referer'] = referer
        try:
            response = requests.get(url, headers=self.headers)
            return response

        except Exception as e:
            return e

    def jjr_request(self, url, referer, data):
        header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': ' CURRENT_CITY_CODE=330100; gr_user_id=4f32b5d1-0fc8-44ac-aab8-14b8d2e290bb; Hm_lvt_038002b56790c097b74c818a80e3a68e=1528945675; mapType=%20; PHPSESSID=1adhkfqsingqr2ukmovfl3mv03; CURRENT_CITY_NAME=%E6%9D%AD%E5%B7%9E; gr_session_id_8da2730aaedd7628=b3b9be3b-4f19-4bc0-b244-e6c375098cce_true; HZ_nlist=%7B%2261318695%22%3A%7B%22id%22%3A%2261318695%22%2C%22sell_price%22%3A2190%2C%22title%22%3A%22%5Cu897f%5Cu6e56%5Cu4e09%5Cu58a92%5Cu53f7%5Cu7ebf%5Cu58a9%5Cu7965%5Cu8857%5Cu7d2b%5Cu91d1%5Cu6e2f%5Cu6e7e4%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528962291%2C%22usage_area%22%3A16.2%2C%22floor%22%3A%223%22%2C%22floor_total%22%3A%2217%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F04%5C%2FA8%5C%2FChAFfVscnzOAfoTTAAu7-Ig51LU439.jpg%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2261254834%22%3A%7B%22id%22%3A%2261254834%22%2C%22sell_price%22%3A1930%2C%22title%22%3A%22%5Cu8427%5Cu5c71%5Cu94b1%5Cu6c5f%5Cu4e16%5Cu7eaa%5Cu57ce2%5Cu53f7%5Cu7ebf%5Cu98de%5Cu8679%5Cu8def%5Cu987a%5Cu53d1%5Cu6c5f%5Cu5357%5Cu4e3d%5Cu95265%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528959123%2C%22usage_area%22%3A12.4%2C%22floor%22%3A%2211%22%2C%22floor_total%22%3A%2233%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2FF9%5C%2F4A%5C%2FChAFfVsWbV6AeW95ABRRAxw_jvc277.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2261205037%22%3A%7B%22id%22%3A%2261205037%22%2C%22sell_price%22%3A1930%2C%22title%22%3A%22%5Cu6c5f%5Cu5e72%5Cu4e5d%5Cu58211%5Cu53f7%5Cu7ebf%5Cu5ba2%5Cu8fd0%5Cu4e2d%5Cu5fc3%5Cu7ea2%5Cu82f9%5Cu679c%5Cu5bb6%5Cu56ed4%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528958098%2C%22usage_area%22%3A13.5%2C%22floor%22%3A%224%22%2C%22floor_total%22%3A%2215%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2FA1%5C%2F0A%5C%2FChAFfVrh_wKAN8JwAAPbRZv2_n8394.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2261341163%22%3A%7B%22id%22%3A%2261341163%22%2C%22sell_price%22%3A2290%2C%22title%22%3A%22%5Cu6c5f%5Cu5e72%5Cu4e5d%5Cu58211%5Cu53f7%5Cu7ebf%5Cu4e5d%5Cu548c%5Cu8def%5Cu9633%5Cu5149%5Cu57ce%5Cu666e%5Cu53474%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528958095%2C%22usage_area%22%3A10.1%2C%22floor%22%3A%2215%22%2C%22floor_total%22%3A%2216%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F06%5C%2FD2%5C%2FChAFD1sdQ36APzQUAAIfiXnPqIA548.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2261342192%22%3A%7B%22id%22%3A%2261342192%22%2C%22sell_price%22%3A1830%2C%22title%22%3A%22%5Cu4f59%5Cu676d%5Cu4e54%5Cu53f81%5Cu53f7%5Cu7ebf%5Cu7fc1%5Cu6885%5Cu91d1%5Cu5730%5Cu827a%5Cu58835%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528957938%2C%22usage_area%22%3A15.3%2C%22floor%22%3A%2212%22%2C%22floor_total%22%3A%2217%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F01%5C%2F73%5C%2FChAFfVsasmKAQoVJAAJIRaLeMrI591.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2261318412%22%3A%7B%22id%22%3A%2261318412%22%2C%22sell_price%22%3A2130%2C%22title%22%3A%22%5Cu6c5f%5Cu5e72%5Cu706b%5Cu8f66%5Cu4e1c%5Cu7ad94%5Cu53f7%5Cu7ebf%5Cu666f%5Cu82b3%5Cu666f%5Cu82b3%5Cu4e00%5Cu533a4%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528955565%2C%22usage_area%22%3A11.9%2C%22floor%22%3A%224%22%2C%22floor_total%22%3A%227%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F04%5C%2FB5%5C%2FChAFD1scoxyAXGhrAAJ_WzbqONo776.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2261284128%22%3A%7B%22id%22%3A%2261284128%22%2C%22sell_price%22%3A5190%2C%22title%22%3A%22%5Cu4e0b%5Cu6c99%5Cu9ad8%5Cu6559%5Cu56ed%5Cu533a%5Cu897f1%5Cu53f7%5Cu7ebf%5Cu6587%5Cu6cfd%5Cu8def%5Cu548c%5Cu8fbe%5Cu57ce2%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528949063%2C%22usage_area%22%3A11.9%2C%22floor%22%3A%223%22%2C%22floor_total%22%3A%2233%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2FD9%5C%2F95%5C%2FChAFD1sEwP6AGvT5ABAKTNEFij4096.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%2C%2260783029%22%3A%7B%22id%22%3A%2260783029%22%2C%22sell_price%22%3A1830%2C%22title%22%3A%22%5Cu897f%5Cu6e56%5Cu7533%5Cu82b12%5Cu53f7%5Cu7ebf%5Cu4e09%5Cu58a9%5Cu9996%5Cu5f00%5Cu56fd%5Cu98ce%5Cu7f8e%5Cu57df5%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1528946584%2C%22usage_area%22%3A12.4%2C%22floor%22%3A%2227%22%2C%22floor_total%22%3A%2231%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2FF4%5C%2F75%5C%2FChAFD1sTuTqAKeEfABWAq795LQA043.JPG%22%2C%22city_name%22%3A%22%5Cu676d%5Cu5dde%22%7D%7D; Hm_lpvt_038002b56790c097b74c818a80e3a68e=1528962290',
            'Host': 'hz.ziroom.com',
            'Referer': 'http://hz.ziroom.com/z/vr/61318695.html',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        header['Referer'] = referer
        try:
            response = requests.get(url, headers=header, params=data)
            return response

        except Exception as e:
            return e

    def link(self, content):
        html = etree.HTML(content)
        return html.xpath('//div[@class="txt"]/h3/a/@href')

    def write(self, response):
        html = etree.HTML(response.content)
        city = "杭州"
        try:
            district_before = html.xpath('//p[@class="pr"]/span[@class="ellipsis"]/text()')[0]
            district = re.findall(r'\[(.*?)\s+(.*?)\]', district_before)[0][0]
            cell_name = re.findall(r'\[(.*?)\s+(.*?)\]', district_before)[0][1]
        except:
            district = '暂无数据'
            cell_name = '暂无数据'
        # cell_address = html.xpath('')[0]
        try:
            house_type = html.xpath('//ul[@class="detail_room"]/li[3]/text()')[0].strip()
        except:
            house_type = '暂无数据'
        try:
            area_before = html.xpath('//ul[@class="detail_room"]/li[1]/text()')[0]
            area = re.findall(r'\d+\.*\d*', area_before)[0]
        except:
            area = '暂无数据'
        try:
            decoration = html.xpath('//span[@class="style"]/text()')[0]
        except:
            decoration = '暂无数据'
        try:
            face = html.xpath('//ul[@class="detail_room"]/li[2]/text()')[0]
        except:
            face = '暂无数据'
        try:
            price = html.xpath('//span[@class="room_price"]/text()')[0]
        except:
            price = '暂无数据'
        try:
            pay_way = html.xpath('//span[@class="price"]/span[@class="gray-6"]/text()')[0]
        except:
            pay_way = '暂无数据'
        try:
            house_id = html.xpath('//input[@id="house_id"]/@value')[0]
        except:
            house_id = '暂无数据'
        try:
            resblock_id = html.xpath('//input[@id="resblock_id"]/@value')[0]
        except:
            resblock_id = ''
        roomid = re.findall(r'\d+', response.url)[0]
        data = {
            'resblock_id': resblock_id,
            'room_id': roomid,
            'house_id': house_id,
            'ly_name': '',
            'ly_phone': '',
        }
        res = self.jjr_request('http://hz.ziroom.com/detail/steward?', response.url, data=data).content
        res=json.loads(res)
        try:
            jjr_name = res["data"]["keeperName"]
            jjr_phone = res["data"]["keeperPhone"]
        except:
            jjr_name = '暂无数据'
            jjr_phone = '暂无数据'
        try:
            floor = html.xpath('//ul[@class="detail_room"]/li[4]/text()')[0]
            rental_method = html.xpath('//ul[@class="detail_room"]/li[3]/span/text()')[0]
        except:
            floor = '暂无数据'
            rental_method = '暂无数据'
        from_web = "自如"
        from_url = response.url

        try:
            image = html.xpath('//img[@class="loadImgError"]/@src')[0]
        except:
            image = '暂无数据'
        try:
            introduce = html.xpath('//div[@class="aboutRoom gray-6"]/p[1]/text()')[0]
        except:
            introduce = '暂无数据'
        try:
            titles=html.xpath('//div[@class="room_name"]/h2/text()')
            title = titles[0].strip()
        except:
            title = '暂无数据'

        crawl_time = datetime.datetime.utcnow()
        lis = [city,
               title,
               district,
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
               crawl_time,
               from_web,
               from_url,
               house_id,
               image,
               introduce,
               ]
        csvwrite = csv.writer(self.file, dialect='excel')
        csvwrite.writerow(lis)

    def manage(self):
        self.file = open('res.csv', 'w')
        for i in range(self.page_num):
            for link in self.link(self.send_request(self.base_url % self.page, "").content):
                # link = self.link(self.send_request(self.base_url % self.page, self.base_url % (self.page - 1) if self.page > 1 else self.page).content)
                self.write(self.send_request('http:' + link, self.base_url % self.page))
            self.page += 1
        self.file.close()

    def manage2(self):
        self.file = open('res.csv', 'w')
        for i in range(self.page_num):
            # print self.base_url%self.page
            link = self.link(self.send_request(self.base_url % self.page, "").content)[0]
            self.write(self.send_request('http:' + link, self.base_url % self.page))
            # with open('a.html', 'w') as f:
            #     f.write(self.send_request('http:' + link, self.base_url % self.page).content)
        self.file.close()


if __name__ == '__main__':
    a = ZiroomSpider()
    # a.manage()
    a.manage()
