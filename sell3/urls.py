#coding=utf-8
'''
Created on 2011-3-19

@author: 王健
'''
from django.conf.urls import patterns
from sell3.views import top, menu, welcome, clientLogin, teltruename, checkteltruename, saveteltruename, getExcelPage, uploadExcel, androidCheck, androidSave, autoSaveTel, downloadTrue, reUpload
from sell3.views_user import check_username, userAdd, userSave, userDelete, userOpen, userPassword, userDeviceid, userList, userListPage


urlpatterns = patterns('^oa/$',
                       (r'^top/$', top),
                       (r'^menu/$', menu),
                       (r'^welcome/$', welcome),
                        (r'^teltruename/$',teltruename),
                        (r'^checkteltruename/$',checkteltruename),
                        (r'^saveteltruename/$',saveteltruename),
                        (r'^getExcelPage/$',getExcelPage),
                        (r'^uploadExcel/$',uploadExcel),
                        (r'^androidCheck/$',androidCheck),
                        (r'^androidSave/$',androidSave),

                        (r'^clientLogin/$',clientLogin),
                        (r'^check_username/$',check_username),
                        (r'^userAdd/$',userAdd),
                        (r'^userSave/$',userSave),
                        (r'^userDelete/$',userDelete),
                        (r'^userOpen/$',userOpen),
                        (r'^userPassword/$',userPassword),
                        (r'^userDeviceid/$',userDeviceid),
                        (r'^userList/$',userList),
                        (r'^userListPage/$',userListPage),


                        (r'^autoSaveTel/$',autoSaveTel),
                        (r'^downloadTrue/$',downloadTrue),
                        (r'^reUpload/$',reUpload),


                       )