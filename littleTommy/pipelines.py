# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import scrapy.exceptions.DropItem as DropException
#import scrapy.exceptions.DropItem
from scrapy.exceptions import DropItem

from scrapy import signals
import os.path

import shelve
import logging
logging.basicConfig(filename='./log/log_pipe.log',level=logging.INFO)

class dbExportPipeline(object):

    def __init__(self):
        self.files = {}
        
    @classmethod
    def from_crawler(clc, crawler):
        pipeline = clc()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):

        pass

    def spider_closed(self, spider):
        pass

    def process_item(self, item, spider):
        logging.info("tommyPipeline: process_item called")
        item_dict = {}
        if not item['valid'] or item['valid'] == '0':
            logging.info("tommyPipeline: dropped an item")
            raise DropException('item not valid')
        
        logging.info("tommyPipeline: received an item. valid = %d",item['valid'])
        db = shelve.open('./db/%s_products'%spider.name)
        for key in item.keys():
            item_dict[str(key)] = item[str(key)][0]
#        logging.info("!! %s: %s"%(item.keys(),item[key]))
        db[str(item['name'][0])] = item_dict
        
        db.close()

        return item
