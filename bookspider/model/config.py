# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# ��ʼ�����ݿ�����:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/bookspider')
# ����DBSession����:
DBSession = sessionmaker(bind=engine)
