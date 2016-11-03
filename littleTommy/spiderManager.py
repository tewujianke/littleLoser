from __future__ import print_function
from subprocess import Popen
import subprocess
import logging
import threading

logging.basicConfig(filename='./log/thread.log',level=logging.INFO)
class NotAString (Exception): pass

class startSpiderThread(threading.Thread):
    """
    Thread object to start a spider thread. 
    THIS OBJECT SHOULD NOT BE USED OUTSIDE
    """
    def __init__(self,spider):
        threading.Thread.__init__(self)
        self.spider_name = spider

    def run(self):
        logging.info('starting spider %s'%self.spider_name)
        #supremeSpider
        with Popen('scrapy crawl %s'%self.spider_name,stdout=subprocess.PIPE,shell=True) as Proc:
            logging.info("finished thread")
        logging.info('%s spider finished'%self.spider_name)
        
class spiderManager(object):
    """
    Spider Manager keeps track on all registered Spiders.
    SpiderManager provides multi-threading service for all Spiders
    """
    def __init__(self,spider_list):
        """
        Requires to pass a list of spiders' name in str
        Undefined behavior if the passed spider names don't match the real name
        """
        self.spider_list = {}
        for spi in spider_list:
            self.spider_list[str(spi)] = 1 #use dict for fast lookup 
        
        self.num_of_spiders = len(self.spider_list)
        
    def start_spider(self,spider):
        if not isinstance(spider,str):
            raise NotAString("passed spider is not a string")
        logging.info('start_spider called!')
        
        spi = startSpiderThread('supremeSpider')
        spi.start()
      
     
        spi.join() #wait for the spider
#pipe = subprocess.PIPE
#p  = Popen('scrapy crawl supremeSpider',shell=True,stdout=subprocess.PIPE)

#out,erros = p.communicate()

if __name__ == '__main__':

    manager = spiderManager(['supremeSpider'])
    manager.start_spider('supremeSpider')

