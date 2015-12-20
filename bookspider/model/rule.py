# -*- coding: utf-8 -*-
from sqlalchemy import Column, String , DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rule(Base):
    __tablename__ = 'rules'

    id = Column(Integer, primary_key=True)
    spidername = Column(String)
    allowed_domains = Column(String)
    start_urls = Column(String)
    next_page = Column(String)
    allow_url = Column(String)
    extract_from = Column(String)
    bookname_xpath = Column(String)
    author_xpath = Column(String)
    picture_xpath = Column(String)
    intro_xpath = Column(String)
    type_xpath = Column(String)
    enable = Column(Integer)