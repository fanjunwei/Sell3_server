# coding=utf-8
# Date:2014/9/24
#Email:wangjian2254@gmail.com
import httplib
import json, base64
import uuid
import datetime
from django.contrib.auth.models import User
from Sell3_server.settings import MEDIA_ROOT
from sell3.models import Person, Msg, Truename

__author__ = u'王健'

from django.http import HttpResponse
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode

import xml.etree.ElementTree as ET
import urllib, urllib2, time, hashlib

TOKEN = "pibgrj1409810714"

HANWANG_KEY = '3b1c7302-4d31-4c56-b034-94b48e59dd5d'

YOUDAO_KEY = '你申请到的有道的Key'
YOUDAO_KEY_FROM = "有道的key-from"
YOUDAO_DOC_TYPE = "xml"

YUNMAI_USERNAME = 'test141001'
YUNMAI_PASSWORD = 'asdg23sdgsuUILo878sdsdf'
YUNMAI_URL = 'http://eng.ccyunmai.com:5008/SrvEngine'


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
    picurl = msg.get('PicUrl', '')
    fuid = msg['FromUserName']
    result_msg = u''
    reg, person = isReg(fuid)
    if not reg:
        m = Msg()
        m.msg = content
        m.imageurl = picurl
        m.user = person.user
        m.save()
        result_msg = u'您的账号尚未被授权实名制，需要等待管理员审批。请您留言表明您的身份，方便管理员授权管理'
    else:
        if msgtype == 'event':
            eventMsg(msg)
        else:

            truename, created = Truename.objects.get_or_create(weixin=True, user=person.user)
            if msgtype == 'text':
                try:
                    tel = int(content)
                    truename.tel = tel
                    truename.save()
                except:
                    if truename.idstatus == 1:
                        downloadIDimage(truename.idimg, truename.id)
                        shibie2(truename.id)
                    elif truename.idstatus == 2:
                        shibie2(truename.id)
                    pass

            elif msgtype == 'image':
                if truename.idimg == picurl:
                    truename.idstatus = 1
                    truename.save()
                    if truename.idstatus == 1:
                        downloadIDimage(picurl, truename.id)
                        shibie2(truename.id)
                    elif truename.idstatus == 2:
                        shibie2(truename.id)
                else:
                    truename.idimg = picurl
                    truename.imgfile.delete()
                    truename.idstatus = 1
                    truename.save()
                    downloadIDimage(picurl, truename.id)
                    shibie2(truename.id)
            truename = Truename.objects.get(pk=truename.id)
            result_msg = u'手机号实名认证\n'
            if truename.tel:
                result_msg += u'手机号：%s\n'% truename.tel
            else:
                result_msg += u'手机号尚未提供！\n'
            if truename.idstatus == 0:
                result_msg += u'身份证尚未拍照上传！\n'
            elif truename.idstatus in [1, 2, 3]:
                result_msg += u'身份证正在识别！(%s)\n'%truename.idstatus
            elif truename.idstatus == 4:
                result_msg += u'姓名:%s\n身份证号:%s\n地址:%s\n' % (truename.name, truename.number, truename.address)
            elif truename.idstatus == 5:
                result_msg += u'身份证图片识别失败，请重新拍照'
            result_msg += u'（发送任意文字，显示实名进度！）\n'
            if picurl:
                return getReplyXmlImg(msg, result_msg.encode('utf-8'), picurl)

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

def getReplyXmlImg(msg, replyContent,url):
    extTpl='''<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>1</ArticleCount>
<Articles>
<item>
<Title><![CDATA[手机号实名]]></Title>
<Description><![CDATA[%s]]></Description>
<PicUrl><![CDATA[%s]]></PicUrl>
<Url><![CDATA[]]></Url>
</item>
</Articles>
</xml> '''
    extTpl = extTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), replyContent, url)
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


def downloadIDimage(url, trueid):
    import os,uuid
    try:
        f = urllib2.urlopen(url)
        data = f.read()
        filename = str(uuid.uuid4())
        with open("%s/%s" % (os.path.join(MEDIA_ROOT, "idimg"), filename), "wb") as code:
            code.write(data)
        truename = Truename.objects.get(pk=trueid)
        if truename.idstatus < 2:
            truename.imgfile = '%s/%s'%('idimg', filename)
            truename.idstatus = 2
            truename.save()
        return True
    except Exception,e:
        return False


def shibie(trueid):
    truename = Truename.objects.get(pk=trueid)
    if truename.idstatus == 2:
        truename.idstatus = 3
        truename.save()
        param = {'uid': '', 'lang': '', 'color': '', 'image': ''}


        data = open(truename.imgfile.path, 'rb').read()
        param['image'] = base64.encodestring(data)
        req = urllib2.Request("http://api.hanvon.com/rt/ws/v1/ocr/idcard/recg?key=%s&code=8d497db3-7341-4f1f-875a-2f5444884515" % HANWANG_KEY)
        req.add_header('Content-Type', 'application/octet-stream')
        connection = httplib.HTTPConnection(req.get_host())
        connection.request('POST', req.get_selector(), json.dumps(param))
        response = connection.getresponse()

        result = json.loads(response.read())
        if result.get('code', '') == '0':
            truename.name = result.get('name')
            truename.number = result.get('idnumber')
            truename.address = result.get('address')
            truename.idstatus = 4
            truename.save()
        else:
            truename.idstatus = 5
            truename.save()

def shibie2(trueid):
    truename = Truename.objects.get(pk=trueid)
    if truename.idstatus == 2:
        truename.idstatus = 3
        truename.save()
        extTpl='''<xml>
<action>idcard</action>
<client>%s</client>
<system>windows</system>
<key>%s</key>
<time>%s</time>
<verify>%s</verify>
<file>%s</file>
<ext>jpg</ext>
</xml> '''
        # MD5(action+client+key+time+%password%)

        key = str(uuid.uuid4())
        timeline = str(int(time.time()*1000))
        v = hashlib.md5('%s%s%s%s%s' % ('idcard', YUNMAI_USERNAME, key, timeline, YUNMAI_PASSWORD)).hexdigest().upper()
        extTpl = extTpl % (YUNMAI_USERNAME, key, timeline, v, open(truename.imgfile.path, 'rb').read())
        req = urllib2.Request(YUNMAI_URL)
        req.add_header('Content-Type', 'application/octet-stream')
        connection = httplib.HTTPConnection(req.get_host())
        connection.request('POST', req.get_selector(), extTpl)
        response = connection.getresponse()

        result = response.read()
        msg = paraseResultXml(ET.fromstring('<xml>%s</xml>'%result))
        if msg.get('result', '') == '1':
            truename.name = msg.get('name')
            truename.number = msg.get('cardno')
            truename.address = msg.get('address')
            truename.idstatus = 4
            truename.save()
        else:
            truename.idstatus = 5
            truename.save()


def paraseResultXml(rootElem):
    msg = {}
    if rootElem.tag == 'xml':
        for child in rootElem:
            if child.text:
                msg[child.tag] = smart_str(child.text)
            else:
                for c in child:
                    msg[c.tag] = smart_str(c.text)

    return msg