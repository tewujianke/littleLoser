from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import logging
import sys
from littleTommy.items import LittletommyItem
from scrapy.loader import ItemLoader



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
        l = ItemLoader(item=LittletommyItem(),response=response)
        #parse data here
        category = (str(response.url).split('/'))[-3]
        #Supreme web uses utf-8, will cause decode to str error. Add encode and ignore \ to solve the issue
        title = response.selector.xpath('//head/title/text()').extract_first().encode('ascii','backslashreplace')
        tmpList = str(title).split('-')
        color = tmpList[-1]
        picUrl = response.selector.xpath('//*[@id="img-main"]/@src').extract_first().encode('ascii','backslashreplace')
        picUrl = 'http:' + str(picUrl)
        name = tmpList[0]
        name = name.replace('\\\\xae','')
        name = name.replace('\\xae','')
        l.add_value('name',name[:-1])#no space wanted in the end
        l.add_value('color',color[1:])#no space wanted in the begginging
        l.add_value('url',response.url)
        l.add_xpath('price','//p[@class="price"]/span/text()')
        l.add_value('pic_url',picUrl)
        l.add_value('category',category)
        if picUrl :
            l.add_value('valid','1')
        else :
            l.add_value('valid','0')
        return l.load_item()

