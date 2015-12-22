# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    bookname = scrapy.Field()
    author = scrapy.Field()
    picture = scrapy.Field()
    intro = scrapy.Field()
    type = scrapy.Field()
