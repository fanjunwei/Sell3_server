#coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

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


class Truename(models.Model):
    tel = models.CharField(max_length=11,unique=True,verbose_name=u'电话号码',help_text=u'手机号码')
    name = models.CharField(max_length=18,verbose_name=u'姓名',help_text=u'身份证证上的姓名')
    number = models.CharField(max_length=18,verbose_name=u'身份证号',help_text=u'身份证号')
    address = models.CharField(max_length=30,verbose_name=u'地址',help_text=u'居住地址')
    datetime = models.CharField(default=datetime.now(),verbose_name=u'默认时间')

    def __unicode__(self):
        return u'%s_%s_%s'%(self.tel,self.name,self.number)
    class Meta():
        verbose_name=u'实名记录'
        verbose_name_plural=u'实名记录'
