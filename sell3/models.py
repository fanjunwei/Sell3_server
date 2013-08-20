#coding=utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User)
    sex = models.BooleanField(default=True, verbose_name=u'性别', help_text=u'性别')
    tel = models.CharField(max_length=15, verbose_name=u'电话')
    deviceid=models.CharField(max_length=100,unique=True,blank=True,null=True,verbose_name=u'手机唯一编码',help_text=u'手机的指纹')

    def __unicode__(self):
        if self.depate:
            return u'%s_%s_%s'%(self.depate,self.user.username,self.user.get_full_name())
        return u'%s_%s_%s'%(u'无隶属',self.user.username,self.user.get_full_name())

