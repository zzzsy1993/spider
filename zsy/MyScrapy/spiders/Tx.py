# -*- coding: utf-8 -*-
import scrapy
from MySpider.wyf.MyScrapy.items import MyscrapyItem


class TxSpider(scrapy.Spider):
    name = "Tx"
    allowed_domains = ["https://hr.tencent.com"]
    base_url = 'https://hr.tencent.com/position.php?keywords=python&tid=87&start=%d'
    start_urls = [
        base_url % num for num in range(0, 200, 10)
    ]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even']|tr[@class='odd']")
        for node in node_list:
            item = MyscrapyItem()
            item['name'] = node.xpath(".//a/text()").extract_first()
            item['link'] = node.xpath(".//a/@href").extract_first()
            item['type'] = node.xpath("./td[2]/text()").extract_first()
            item['number'] = node.xpath("./td[3]/text()").extract_first()
            item['location'] = node.xpath("./td[4]/text()").extract_first()
            item['time'] = node.xpath("./td[5]/text()").extract_first()
            yield item
