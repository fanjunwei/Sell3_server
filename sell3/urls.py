#coding=utf-8
'''
Created on 2011-3-19

@author: 王健
'''
from django.conf.urls import patterns
from sell3.views import top, menu, welcome, clientLogin


urlpatterns = patterns('^oa/$',
                       (r'^top/$', top),
                       (r'^menu/$', menu),
                       (r'^welcome/$', welcome),
                        (r'^clientLogin/$',clientLogin),


                       )