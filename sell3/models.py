# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.
class Msg(models.Model):
    user = models.ForeignKey(User)
    msg = models.TextField(verbose_name=u'聊天内容')
    imageurl = models.URLField(verbose_name=u'图片url')


class Person(models.Model):
    user = models.OneToOneField(User)
    weixinid = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name=u'微信openid')
    sex = models.BooleanField(default=True, verbose_name=u'性别', help_text=u'性别')
    tel = models.CharField(max_length=15, verbose_name=u'电话')
    deviceid = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name=u'手机唯一编码',
                                help_text=u'手机的指纹')

    def __unicode__(self):
        return u'%s_%s_%s' % (self.depate, self.user.username, self.user.get_full_name())


class ShiMingMsg(models.Model):
    msgid = models.CharField(max_length=64, unique=True, verbose_name=u'客户所发消息')
    user = models.ForeignKey(User)
    msg = models.TextField(verbose_name=u'聊天内容')
    imageurl = models.URLField(verbose_name=u'图片url')


class Truename(models.Model):
    choice = (('yidong', u'移动'), ('liantong', u'联通'))

    weixin = models.BooleanField(default=False, verbose_name=u'是否正在微信实名')
    tel = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name=u'电话号码', help_text=u'手机号码')
    idimg = models.URLField(null=True, blank=True, verbose_name=u'上传的身份证图片')
    imgfile = models.ImageField(upload_to='idimg', blank=True, null=True, verbose_name=u'身份证图片本地文件')
    idstatus = models.IntegerField(default=0, verbose_name=u'身份证图片识别状态',
                                   help_text=u'0 未提供身份证图片， 1：提供了但是没有完成下载， 2：下载了但是没有识别 3：正在识别, 4:识别完成')
    name = models.CharField(max_length=18, blank=True, null=True, verbose_name=u'姓名', help_text=u'身份证证上的姓名')
    number = models.CharField(max_length=18, blank=True, null=True, verbose_name=u'身份证号', help_text=u'身份证号')
    address = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'地址', help_text=u'居住地址')
    datetime = models.DateTimeField(default=datetime.now, verbose_name=u'默认时间')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name=u'提交账号', help_text=u'操作人')
    status = models.IntegerField(default=0, verbose_name=u'实名状态', help_text=u'0:未实名，1:实名通过，2:实名未通过,')
    help = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'错误内容', help_text=u'实名不通过的错误信息')
    company = models.CharField(max_length=10, default='yidong', choices=choice, null=True, blank=True,
                               verbose_name=u'手机号公司', help_text=u'移动、联通')

    def __unicode__(self):
        return u'%s_%s_%s' % (self.tel, self.name, self.number)

    class Meta():
        verbose_name = u'实名记录'
        verbose_name_plural = u'实名记录'
