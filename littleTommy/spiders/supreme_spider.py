from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class supremeSpider(CrawlSpider):

    name = "supremeSpider"
    allowed_domain = ['supremenewyork.com']
    start_urls = ['http://www.supremenewyork.com/shop/all']

    rules = [Rule(LinkExtractor(allow=('/shop/') ) ,callback='parse_item')]

    def parse_item(self,response):
        self.logger.info("got an url = %s",response.url)
        print "yes"
        
