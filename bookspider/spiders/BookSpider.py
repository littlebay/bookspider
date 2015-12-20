# -*-coding:utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from items import BookspiderItem


class BookSpider(CrawlSpider):
	name="novel"
	
	def __init__(self,rule):
		self.rule=rule
		self.name=rule.spidername
		self.allowed_domains=rule.allowed_domains.split(",")
		self.start_urls=rule.start_urls.split(",")
		rule_list=[]
		#添加下一页规则
		if rule.next_page:
			rule_list.append(Rule(LinkExtractor(restrict_xpaths=[rule.next_page])))
		#抽取文章链接规则
		rule_list.append(Rule(LinkExtractor(allow=[rule.allow_url],restrict_xpaths=[rule.extract_from]),callback='parse_item'))
		self.rules=tuple(rule_list)
		super(BookSpider,self).__init__()

  
	def parse_item(self,response):
		self.log('Hi, this is an novel page! %s' % response.url)
		item = BookspiderItem()
		item["link"] = response.url

		bookename = response.xpath(self.rule.bookename_xpath).extract()
		item["bookename"] = bookename[0] if bookename else ""

		#body = response.xpath(self.rule.body_xpath).extract()
		#item["body"] =  '\n'.join(body) if body else ""

		author= response.xpath(self.rule.author_xpath).extract()
		item["author"] = author[0] if author else ""

		picture= response.xpath(self.rule.picture_xpath).extract()
		item["picture"] = picture[0] if picture else ""
		
		type= response.xpath(self.rule.type_xpath).extract()
		item["type"] = type[0] if type else ""
		
		intro= response.xpath(self.rule.intro_xpath).extract()
		item["intro"] = intro[0] if intro else ""
		
		return item
        