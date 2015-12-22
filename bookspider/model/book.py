# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    bookname = Column(String)
    author = Column(String)
    publisher = Column(String)
    downloadtime = Column(DateTime)
    intro = Column(String)
    picture = Column(String)
    type = Column(String)
    updatetime = Column(DateTime)

