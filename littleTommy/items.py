# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LittletommyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    valid = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    color = scrapy.Field()
    price = scrapy.Field()
    pic_url = scrapy.Field()
    
    filtered = scrapy.Field()
