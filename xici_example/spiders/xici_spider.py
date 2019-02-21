# -*- coding: utf-8 -*-
import scrapy
import json
from xici_example.items import XiciExampleItem


class XiciSpiderSpider(scrapy.Spider):
    name = 'xici_spider'
    allowed_domains = ['xicidaili.com']
    # start_urls = ['http://www.xicidaili.com/nn/']

    #构造起始Url，爬取西刺代理前3页的国内高匿代理IP
    def start_requests(self):
        Base_url='http://www.xicidaili.com/nn/{}'
        for offset in range(1,11):
            url=Base_url.format(str(offset))
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        # print(response.body.decode())
        table = response.xpath('//table[@id="ip_list"]')[0]
        # 去掉标题行
        ip_table = table.xpath('//tr')[1:]
        for tr in ip_table:
            item = XiciExampleItem()
            item['ip'] = tr.xpath('td[2]/text()').extract()[0]  # 获取ip
            item['port'] = tr.xpath('td[3]/text()').extract()[0]  # 获取端口号
            item['transfer_protocol'] = tr.xpath('td[6]/text()').extract()[0]  # 获取网络传输协议

            yield item







