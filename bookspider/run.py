# -*- coding: utf-8 -*-
from spiders.BookSpider import BookSpider
from model.config import DBSession
from model.rule import Rule

# scrapy api
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

settings = Settings()

# crawl settings
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")

settings.set("ITEM_PIPELINES", {
    'pipelines.DuplicatesPipeline': 200,
    'pipelines.BookSpiderPipeline': 300,
})

db = DBSession()
rules = db.query(Rule).filter(Rule.enable == 1)
process = CrawlerProcess(settings)

for rule in rules:
    spider = BookSpider(rule)
    process.crawl(spider, rule)
    process.start()
