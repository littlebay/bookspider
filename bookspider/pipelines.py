# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from model.config import DBSession
from model.book import Book


class BookSpiderPipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        a = Book(bookname=item["bookname"].encode("utf-8"),
                 author=item["author"].encode("utf-8"),
                 intro=item["intro"].encode("utf-8"),
                 picture=item["picture"].encode("utf-8"),
                 type=item["type"].encode("utf-8")
                 )
        self.session.add(a)
        self.session.commit()

    def close_spider(self, spider):
        self.session.close()


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['bookname'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['bookname'])
            return item


