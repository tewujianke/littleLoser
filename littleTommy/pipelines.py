# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import scrapy.exceptions.DropItem as DropException
#import scrapy.exceptions.DropItem
from scrapy.exceptions import DropItem
from scrapy.exporters import XmlItemExporter
from scrapy import signals
import os.path
import logging
logging.basicConfig(filename='log_pipe.log',level=logging.INFO)

class xmlExportPipeline(object):

    def __init__(self):
        self.files = {}
        
    @classmethod
    def from_crawler(clc, crawler):
        pipeline = clc()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        m_file = open('%s_products.xml' % spider.name, 'w+b')
        self.files[spider] = m_file
        self.exporter = XmlItemExporter(m_file,"Products","Item")
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        m_file = self.files.pop(spider)
        m_file.close()

    def process_item(self, item, spider):
        logging.info("tommyPipeline: process_item called")
        
        if not item['valid'] or item['valid'] == '0':
            logging.info("tommyPipeline: dropped an item")
            raise DropException('item not valid')
        
        logging.info("tommyPipeline: received an item. valid = %d",item['valid'])

        self.exporter.export_item(item)
        return item
