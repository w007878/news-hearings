# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class HearingsPipeline(object):
    def open_spider(self, spider):
        self.file = open('result.json', 'a', encoding='utf8')
    
    def close_spider(self, spider):
        self.file.close()
        
    def process_item(self, item, spider):
        print(dict(item))
        
        if item['title'] == None:
            return item
        
        for w in spider.key_words:
            if w in item['title'] or w in item['header']:
                line = json.dumps(dict(item), ensure_ascii=False) + '\n'
                self.file.write(line);
        return item
