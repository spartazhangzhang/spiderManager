# -*- coding: utf-8 -*-

from django.conf.urls import url
from counter.views import get_data,data_handler
urlpatterns = [
    url(r'^data_handler',data_handler,name='handler'),
    url(r'^today$',get_data,name='today'),
]