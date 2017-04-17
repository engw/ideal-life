# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IdeallifeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    rent = scrapy.Field()
    deposit = scrapy.Field()
    tip = scrapy.Field()
    nearest_stations = scrapy.Field()
    address = scrapy.Field()
    birthday = scrapy.Field()
    window_angle = scrapy.Field()
    dimension = scrapy.Field()
    layout = scrapy.Field()
