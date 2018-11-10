# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import dataset


class A82TuPipeline(object):
    def __init__(self):
        tmp = {
                'title': '',
                'info': '',
                'url': ''}
        db = dataset.connect('sqlite:///82tu.db')
        self.table = db['movie']
        self.table.upsert(tmp, ['url'])
        self.table.create_index(['name', 'country'])


    def process_item(self, item, spider):
        self.table.upsert(item, ['url'])
        return item
