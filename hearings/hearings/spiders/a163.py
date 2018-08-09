# -*- coding: utf-8 -*-
import scrapy


class A163Spider(scrapy.Spider):
    name = '163'
    allowed_domains = ['163.com']
    start_urls = ['http://163.com/']

    def parse(self, response):
        pass
