# _*_coding:utf-8_*_

from django.conf.urls import url
from accounts.views import index,account_list,create,delete,update,get_acounts,get_all_acounts

urlpatterns = [
    url(r'^$',index),
    url(r'^list$',account_list, name='list'),
    url(r'^create$',create,name='create'),
    url(r'^update$',update,name='update'),
    url(r'^delete$',delete,name='delete'),
    url(r'^get_accounts',get_acounts,name='get_acounts'),
    url(r'^get_all_acounts',get_all_acounts,name='get_all_acounts'),

]