# _*_coding:utf-8_*_

from django.conf.urls import url
from accounts.views import index,account_list

urlpatterns = [
    url(r'^$',index),
    url(r'^list$',account_list, name='list'),
    # url(r'^$',post_list,name='home'),
    # url(r'^create$',post_create,name='create'),
    # url(r'^posts/(?P<id>(\d+))$',post_detail,name='detail'),
    # url(r'^posts/(?P<id>(\d+))/delete$',post_delete, name='delete'),

]