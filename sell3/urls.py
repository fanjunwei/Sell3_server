#coding=utf-8
'''
Created on 2011-3-19

@author: 王健
'''
from django.conf.urls import patterns
from sell3.views import top, menu, welcome, clientLogin, teltruename, checkteltruename, saveteltruename, getExcelPage, uploadExcel


urlpatterns = patterns('^oa/$',
                       (r'^top/$', top),
                       (r'^menu/$', menu),
                       (r'^welcome/$', welcome),
                        (r'^teltruename/$',teltruename),
                        (r'^checkteltruename/$',checkteltruename),
                        (r'^saveteltruename/$',saveteltruename),
                        (r'^getExcelPage/$',getExcelPage),
                        (r'^uploadExcel/$',uploadExcel),


                       )