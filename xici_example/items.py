# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiciExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip=scrapy.Field()
    port=scrapy.Field()
    transfer_protocol=scrapy.Field()
