# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from hearings.items import HearingsItem

class PeopleSpider(CrawlSpider):
    name = 'people'
    allowed_domains = ['people.com.cn']
    start_urls = ['http://people.com.cn/']
    key_words = [u'听证']
    
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

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
