# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.link import Link
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.htmlparser import HtmlParserLinkExtractor
from hearings.items import HearingsItem
    
class A163Spider(CrawlSpider):

    name = '163'
    allowed_domains = ['news.163.com', 'gov.163.com']
    start_urls = ['http://' + url for url in allowed_domains]
    key_words = [u'听证']
    # ['https://news.163.com/', 'https://gov.163']
    
    rules = (
        Rule(LinkExtractor(allow=[r'/photoview/.*', r'/\d{2,5}/.*']), 
            callback='parse_item', follow=True),
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

        # print(page_title)
        
