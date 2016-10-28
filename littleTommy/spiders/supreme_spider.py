from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import logging

logging.basicConfig(filename='log_supreme_spider.log',level=logging.INFO)
                    
class supremeSpider(CrawlSpider):

    name = "supremeSpider"
    allowed_domain = ['supremenewyork.com']
    start_urls = ['http://www.supremenewyork.com/shop/all']

    rules = [Rule(LinkExtractor(allow=('/shop/.+?/.+'),deny=('all')),callback='parse_item')]

    #can't use parse() in CrawlSpider! Must use customized parse_item
    def parse_item(self,response):

        logging.info("Supreme_spider: got an url %s",response.url)
        #load info to an Item object
        #set m_item['valid'] = 1 for valid parsing. Otherwise, set 0 to be dropped in pipeline
        m_item = LittletommyItem()

        #parse data here
