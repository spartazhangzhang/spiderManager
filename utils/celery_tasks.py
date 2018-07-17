# -*- coding: utf-8 -*-
from celery import task
import pymongo
import requests

client = pymongo.MongoClient('mongodb://localhost:27017')

@task
def check_counter():
    # print('adadasdadasd')
    col = client['tmall']['nvzhuang']
    num = col.find().count()
    requests.get('http://localhost:8000/counter/data_handler?number={}'.format(num))

