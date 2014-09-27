# coding=utf-8
# Date:2014/9/24
#Email:wangjian2254@gmail.com
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

    s = u'王健：'
    queryStr = '%s_%s:%s:%s' % (s, msg['FromUserName'], msg['ToUserName'], msg.get('Content', ''))


    return getReplyXml(msg, queryStr)


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