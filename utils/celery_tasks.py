# -*- coding: utf-8 -*-
from celery import task
import pymongo
import requests

client = pymongo.MongoClient('mongodb://rwuser:48bb67d7996f327b@10.0.0.120:57017,10.0.0.121:57017,10.0.0.122:57017/?replicaSet=rs1')

@task
def check_counter(db,collection):
    col = client[db][collection]
    num = col.find().count()
    requests.get('localhost:8000/data_handler?number={}'.format(num))

