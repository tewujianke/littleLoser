# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import scrapy.exceptions.DropItem as DropException
#import scrapy.exceptions.DropItem
from scrapy.exceptions import DropItem
from scrapy.exporters import XmlItemExporter
import os.path

class LittletommyPipeline(object):
    def process_item(self, item, spider):

        if(not os.path.exists('store.log')):
            db = open('store.log','w')
            db.write("#supreme log")
        else:
            db = open('store.log','a')
        
        if not item['valid'] or item['valid'] == '0':
            raise DropException('item not valid')
        feed = XmlItemExporter(db)

        db.close()
        return item
