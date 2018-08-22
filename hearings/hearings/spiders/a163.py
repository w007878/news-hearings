# -*- coding: utf-8 -*-
import scrapy


class A163Spider(scrapy.Spider):
    name = '163'
    allowed_domains = ['163.com']
    start_urls = ['https://news.163.com/']

    queue = []
    def parse(self, response):
        print(response.xpath('//a'))
        print('QAQ')
        pass
