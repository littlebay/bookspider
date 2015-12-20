# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import ConfigParser
import string
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno

class BookspiderPipeline(object):
    BASE_DIR = os.path.dirname(__file__) 
    DIR=BASE_DIR+"/model/db.cfg"
    cf=ConfigParser.ConfigParser()
    cf.read(DIR)
    def __init__(self):
        BASE_DIR = os.path.dirname(__file__) 
        DIR=BASE_DIR+"/model/db.cfg"
        cf=ConfigParser.ConfigParser()
        cf.read(DIR)
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db = cf.get("db","db_name"),
            user =cf.get("db","db_user"),
            passwd = cf.get("db","db_passwd"),
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
        )
       
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, tx, item):
        BASE_DIR = os.path.dirname(__file__) 
        DIR=BASE_DIR+"/model/db.cfg"
        cf=ConfigParser.ConfigParser()
        cf.read(DIR)
        sql=cf.get("SQL","book")
        tx.execute(sql, (item['bookname'], item['author'],item['intro'],item['picture'],item['type']))