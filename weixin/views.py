# coding=utf-8
# Date:2014/9/24
#Email:wangjian2254@gmail.com
from django.contrib.auth.models import User
from sell3.models import Person, Msg

__author__ = u'王健'

from django.http import HttpResponse
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode

import xml.etree.ElementTree as ET
import urllib, urllib2, time, hashlib

TOKEN = "pibgrj1409810714"

YOUDAO_KEY = '你申请到的有道的Key'
YOUDAO_KEY_FROM = "有道的key-from"
YOUDAO_DOC_TYPE = "xml"


def handleRequest(request):
    if request.method == 'GET':
        #response = HttpResponse(request.GET['echostr'],content_type="text/plain")
        response = HttpResponse(checkSignature(request), content_type="text/plain")
        return response
    elif request.method == 'POST':
        #c = RequestContext(request,{'result':responseMsg(request)})
        #t = Template('{{result}}')
        #response = HttpResponse(t.render(c),content_type="application/xml")
        response = HttpResponse(responseMsg(request), content_type="application/xml")
        return response
    else:
        return None


def checkSignature(request):
    global TOKEN
    signature = request.GET.get("signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echoStr = request.GET.get("echostr", None)

    token = TOKEN
    tmpList = [token, timestamp, nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return echoStr
    else:
        return None


def responseMsg(request):
    rawStr = smart_str(request.body)
    #rawStr = smart_str(request.POST['XML'])
    msg = paraseMsgXml(ET.fromstring(rawStr))
    msgtype = msg.get('MsgType')
    content = msg.get('Content', '')
    picurl = msg.get('PicUrl ', '')
    fuid = msg['FromUserName']
    result_msg = u''
    reg, person = isReg(fuid)
    if not reg:
        m = Msg()
        m.msg = content
        m.imageurl = picurl
        m.user = person.user
        m.save()
        # result_msg = u'您的账号尚未被授权实名制，需要等待管理员审批。请您留言表明您的身份，方便管理员授权管理:%s:%s_%s'%(content.decode('utf-8'), picurl,request.body.decode('utf-8'))
        result_msg = u'%s:%s'%(msgtype,picurl)
    else:
        if msgtype == 'event':
            eventMsg(msg)
        else:
            if msgtype == 'text':
                pass
            elif msgtype == 'image':
                pass



    return getReplyXml(msg, result_msg.encode('utf-8'))


def paraseMsgXml(rootElem):
    msg = {}
    if rootElem.tag == 'xml':
        for child in rootElem:
            msg[child.tag] = smart_str(child.text)
    return msg


def getReplyXml(msg, replyContent):
    extTpl = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>";
    extTpl = extTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), 'text', replyContent)
    return extTpl

def eventMsg(msg):
    eventtype = msg.get('Event')
    eventkey = msg.get('EventKey', '')

    if eventtype == 'CLICK':
        if eventkey == 'user':
            # 注册
            pass
        elif eventkey == 'shiming':
            # 实名
            pass
    elif eventtype == 'subscribe':
        pass

def isReg(weixinid):
    if not Person.objects.filter(weixinid=weixinid).exists():
        person = Person()
        user = User()
        user.username = weixinid
        user.is_active = False
        user.save()
        person.user = user
        person.weixinid = weixinid
        person.save()
        return False, person
    else:
        person = Person.objects.get(weixinid=weixinid)
        if person.user.is_active:
            return True, person
        else:
            return False, person