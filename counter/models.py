from django.db import models
from mongoengine import *
from mongoengine import connect
connect('qichacha_com', host='10.0.0.120', port=57017)

# Create your models here.
class Counter(models.Model):
    number = models.IntegerField()
    timestamp = models.DateField(auto_now=False,auto_now_add=False)

class Qcc(Document):
    url = StringField()
    title = StringField()
    meta = {'collection': 'detail_results'}