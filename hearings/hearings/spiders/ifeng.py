# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from hearings.items import HearingsItem

class IfengSpider(CrawlSpider):
    name = 'ifeng'
    allowed_domains = ['ifeng.com']
    start_urls = ['http://ifeng.com/']

    provinces = ['bj', 'tj', 'he', 'sx', 'nm','ln', 'jl', 'hlj', 'sh', 'js', 'zj', 
    'ah', 'fj', 'jx', 'sd', 'henan', 'hb', 'hn', 'gd', 'gx', 'hi', 'cq', 'sc',
    'gz', 'yn', 'xz', 'sn', 'gs', 'qh', 'nx', 'xj', 'sz']
    topics = ['gov', 'news', 'finance']

    allowed_domains = [i + '.ifeng.com' for i in (provinces + topics)]
    start_urls = ['http://' + i for i in allowed_domains]
    key_words = [u'听证']
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def __init__(self, *a, **kw):
        super(IfengSpider, self).__init__(*a, **kw)
        
    def parse_item(self, response):
        item = HearingsItem()
        item['source'] = self.name
        item['url'] = response.url.split('?')[0]
        title = response.css('h1::text').extract()
        if len(title) > 0:
            item['title'] = title[0]
        else:
            item['title'] = None
            
        item['header'] = response.css('title::text').extract_first()            
        return item
