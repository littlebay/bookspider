# -*- coding: utf-8 -*-
from spiders.BookSpider import BookSpider
from model.config import DBSession
from model.rule import Rule



# scrapy api
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import logging

RUNNING_CRAWLERS = []


def spider_closing(spider):
    logging.info("Spider closed: %s" % spider)
    RUNNING_CRAWLERS.remove(spider)
    if not RUNNING_CRAWLERS:
        reactor.stop()


settings = Settings()

# crawl settings
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")

db = DBSession()
rules = db.query(Rule).filter(Rule.enable == 1)
for rule in rules:
    crawler = CrawlerProcess(settings)
    spider = BookSpider(rule)  # instantiate every spider using rule
    RUNNING_CRAWLERS.append(spider)

    # stop reactor when spider closes
    crawler.crawl(spider)
    crawler.start()

# blocks process so always keep as the last statement
reactor.run()
