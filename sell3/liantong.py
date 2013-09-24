#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
import urllib
import urllib2
from django.http import HttpResponse
from sell3.usernames import LTKEY

__author__ = u'王健'

'''
POST / HTTP/1.1
Accept-Encoding: gzip
User-Agent: Google-HTTP-Java-Client/1.15.0-rc (gzip)
Content-Length: 589
Host: 123.125.96.6:8090
Connection: Keep-Alive

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body>
<ns:NetCardFind>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<agentId>78821B3D7E00DD5565607BBFEE530EEC</agentId>
<iccidnumber>B0A996850A3F8451AB958B4586B473B3469F9894C6579775</iccidnumber>
<versionName>1.0</versionName>
<clientType>01</clientType>
</ns:NetCardFind>
</SOAP-ENV:Body></SOAP-ENV:Envelope>

HTTP/1.1 200 OK
Server: gSOAP/2.8
Content-Type: text/html; charset=utf-8
Content-Length: 650
Connection: close

<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<ns:NetCardFindResponse>
<deviceID>0000000000000000</deviceID>
<communicaID>0003</communicaID>
<tradeState>0000</tradeState>
<description></description>
<cardnumber>201FB8827DE9D8EAC8EF8167442CA86D</cardnumber>
</ns:NetCardFindResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>

POST / HTTP/1.1
Accept-Encoding: gzip
User-Agent: Google-HTTP-Java-Client/1.15.0-rc (gzip)
Content-Length: 601
Host: 123.125.96.6:8090
Connection: Keep-Alive

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body><ns:checkTelphone>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<agentId>AA3C9309459562D9E04C47F38CAC04A6</agentId>
<telplone>2741AD34F808F19859F6D3F314651C66</telplone>
<versionCode>1.1</versionCode>
<versionName>1.0</versionName>
<clientType>01</clientType>
</ns:checkTelphone>
</SOAP-ENV:Body></SOAP-ENV:Envelope>

HTTP/1.1 200 OK
Server: gSOAP/2.8
Content-Type: text/html; charset=utf-8
Content-Length: 763
Connection: close

<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<ns:checkTelphoneResponse>
<deviceID>0000000000000000</deviceID>
<communicaID>0003</communicaID>
<tradeState>0000</tradeState>
<description></description>
<uploadType>2D7D4A5621BC7CC2</uploadType>
<certifyFlag>1000000</certifyFlag>
<noticeFlag>0</noticeFlag>
<noticeTitle></noticeTitle>
<noticeMsg></noticeMsg>
</ns:checkTelphoneResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>
POST / HTTP/1.1
Accept-Encoding: gzip
User-Agent: Google-HTTP-Java-Client/1.15.0-rc (gzip)
Content-Length: 687
Host: 123.125.96.6:8090
Connection: Keep-Alive

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body>
<ns:mobileClientLogin>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<sendSMSflag>1</sendSMSflag>
<agentId>78821B3D7E00DD5565607BBFEE530EEC</agentId>
<agentPasswd>54F59F146DCE3BEE</agentPasswd>
<clientType>C310C73A81C69EAF</clientType>
<versionCode>E07E985011131EFC</versionCode>
<versionName>C6818C139D02F7B3</versionName>
<lac></lac><ci></ci></ns:mobileClientLogin></SOAP-ENV:Body></SOAP-ENV:Envelope>


POST / HTTP/1.1
Accept-Encoding: gzip
User-Agent: Google-HTTP-Java-Client/1.15.0-rc (gzip)
Content-Length: 805
Host: 123.125.96.6:8090
Connection: Keep-Alive

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body>
<ns:uploadCertificateInfo>
<deviceID>0000000000000000</deviceID>
<communicaID>000C</communicaID>
<agentId>AA3C9309459562D9E04C47F38CAC04A6</agentId>
<telplone>2741AD34F808F19859F6D3F314651C66</telplone>
<certificateName>5E22BCEA426CEC30</certificateName>
<certificateType>8D1B6F7327986F7F</certificateType>
<certificateNum>8E52943D267AC851D05BB094B9FD8FD5DF3C91FB895D270C</certificateNum>
<certificateAdd>BB28AD9FDC3EB802BB28AD9FDC3EB802</certificateAdd>
<clientType>01</clientType>
</ns:uploadCertificateInfo></SOAP-ENV:Body></SOAP-ENV:Envelope>
  '''


def getpwd(s1,s2):
    import subprocess
    from Sell3_server.settings import DES_ROOT
    p = subprocess.Popen("java -jar %s %s %s"%(DES_ROOT,s1,s2), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    r=[]
    for line in p.stdout.readlines():
        r.append(line)

    p.wait()
    return ''.join(r)
# print getpwd('1103786107',LTKEY)
# print getpwd('1103786107','sunnada0')
# print getpwd('123123',LTKEY)
# print getpwd('123123','sunnada0')
# print getpwd('8986011394110561407','sunnada0')
# print getpwd('13146033628',LTKEY)
# print getpwd(u'我我'.encode('gbk'),LTKEY)
# print getpwd(u'北京北京北京北京'.encode('gbk'),LTKEY)
# print getpwd('140826198805160015',LTKEY)
    # ls=subprocess.call (["java -jar /Users/wangjian2254/work/django/Sell3_server/test.jar %s %s"%(s1,s2)],shell=True)
    # return ls


ltlogins='''
<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body>
<ns:mobileClientLogin>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<sendSMSflag>1</sendSMSflag>
<agentId>78821B3D7E00DD5565607BBFEE530EEC</agentId>
<agentPasswd>54F59F146DCE3BEE</agentPasswd>
<clientType>C310C73A81C69EAF</clientType>
<versionCode>E07E985011131EFC</versionCode>
<versionName>C6818C139D02F7B3</versionName>
<lac></lac><ci></ci></ns:mobileClientLogin></SOAP-ENV:Body></SOAP-ENV:Envelope>
'''
'''
<clientType>C310C73A81C69EAF</clientType>

'''
registerKey={'k':''}

def ltlogin():
    # from suds.client import Client
    # client = Client('http://123.125.96.6:8090/wsdl')
    # result = client.service.mobileClientLogin({'deviceID':'0000000000000000','communicaID':'FFFF','sendSMSflag':'1','agentId':'ADA658DD7BCD302965607BBFEE530EEC','agentPasswd':'1CB942CDE5E5D625','clientType':'C310C73A81C69EAF','versionCode':'E07E985011131EFC','versionName':'C6818C139D02F7B3','lac':'','ci':'',})
    # print result
    request = urllib2.Request('http://123.125.96.6:8090',' ')
    try:
        response = urllib2.urlopen(request,ltlogins.replace('\n',''))
        result= response.read()
        print result
        start=result.find('registerKey')
        end=result.rfind('registerKey')
        return result[start+12:end-2]
    except Exception,e:
        return ''

ltcheck='''
<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body>
<ns:checkTelphone>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<agentId>AA3C9309459562D9E04C47F38CAC04A6</agentId>
<telplone>%s</telplone>
<versionCode>1.1</versionCode>
<versionName>1.0</versionName>
<clientType>01</clientType>
</ns:checkTelphone></SOAP-ENV:Body></SOAP-ENV:Envelope>
'''
ltfindtel='''
<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body>
<ns:NetCardFind>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<agentId>78821B3D7E00DD5565607BBFEE530EEC</agentId>
<iccidnumber>%s</iccidnumber>
<versionName>1.0</versionName>
<clientType>01</clientType>
</ns:NetCardFind>
</SOAP-ENV:Body></SOAP-ENV:Envelope>
'''
'''
POST / HTTP/1.1
Accept-Encoding: gzip
User-Agent: Google-HTTP-Java-Client/1.15.0-rc (gzip)
Content-Length: 589
Host: 123.125.96.6:8090
Connection: Keep-Alive

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body>
<ns:NetCardFind>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<agentId>78821B3D7E00DD5565607BBFEE530EEC</agentId>
<iccidnumber>B0A996850A3F8451AB958B4586B473B369CE8A89CE4267D1</iccidnumber>
<versionName>1.0</versionName><clientType>01</clientType></ns:NetCardFind></SOAP-ENV:Body></SOAP-ENV:Envelope>
'''
#CB06BAB8BABE34A77D694B3577D94A22

def ltc(tel1,flag=False):
    # data=urllib.urlencode(ap)
    # k=ltlogin()

    # agentid=getpwd('1103855807',LTKEY)
    tel=getpwd(tel1,LTKEY)
    request = urllib2.Request('http://123.125.96.6:8090',' ')
    try:
        response = urllib2.urlopen(request,ltcheck.replace('\n','')%(tel,))
        result= response.read()
        tradeState_start=result.find('tradeState')
        tradeState_end=result.rfind('tradeState')
        tradeState=result[tradeState_start+11:tradeState_end-2]
        description_start=result.find('description')
        description_end=result.rfind('description')
        description=result[description_start+len('description')+1:description_end-2]
        cardnumber_start=result.find('cardnumber')
        cardnumber_end=result.rfind('cardnumber')
        cardnumber=result[cardnumber_start+len('cardnumber')+1:cardnumber_end-2]
        if tradeState=='0000':

                return {'success':True,'msg':u'手机号可可以出售'}

        else:
            return {'success':False,'msg':description.decode('utf-8')}

    except Exception,e:
        return {'success':False,'msg':u'账号异常，请联系管理员'}


def ltv(tel1,phone,flag=False):
    # data=urllib.urlencode(ap)
    # k=ltlogin()

    # agentid=getpwd('1103855807',LTKEY)
    tel=getpwd(tel1,'sunnada0')
    request = urllib2.Request('http://123.125.96.6:8090',' ')
    try:
        response = urllib2.urlopen(request,ltfindtel.replace('\n','')%(tel,))
        result= response.read()
        tradeState_start=result.find('tradeState')
        tradeState_end=result.rfind('tradeState')
        tradeState=result[tradeState_start+11:tradeState_end-2]
        description_start=result.find('description')
        description_end=result.rfind('description')
        description=result[description_start+len('description')+1:description_end-2]
        cardnumber_start=result.find('cardnumber')
        cardnumber_end=result.rfind('cardnumber')
        cardnumber=result[cardnumber_start+len('cardnumber')+1:cardnumber_end-2]
        if tradeState=='0000':
            strl=getpwd(phone,'sunnada0')
            if cardnumber==strl:

                return {'success':True,'msg':u'手机号可可以出售'}
            else:
                return {'success':False,'msg':u'手机号和iccid不匹配'}
        else:
            return {'success':False,'msg':description.decode('utf-8')}

    except Exception,e:
        return {'success':False,'msg':u'账号异常，请联系管理员'}

ltuploadstr='''
<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body>
<ns:uploadCertificateInfo>
<deviceID>0000000000000000</deviceID>
<communicaID>000C</communicaID>
<agentId>AA3C9309459562D9E04C47F38CAC04A6</agentId>
<telplone>%s</telplone>
<certificateName>%s</certificateName>
<certificateType>8D1B6F7327986F7F</certificateType>
<certificateNum>%s</certificateNum>
<certificateAdd>%s</certificateAdd>
<clientType>01</clientType>
</ns:uploadCertificateInfo></SOAP-ENV:Body></SOAP-ENV:Envelope>
'''
'''
POST / HTTP/1.1
Accept-Encoding: gzip
User-Agent: Google-HTTP-Java-Client/1.15.0-rc (gzip)
Content-Length: 601
Host: 123.125.96.6:8090
Connection: Keep-Alive

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body><ns:checkTelphone><deviceID>0000000000000000</deviceID><communicaID>FFFF</communicaID><agentId>AA3C9309459562D9E04C47F38CAC04A6</agentId><telplone>AE413AE36428EE570E8E7BB076B2ECBA</telplone><versionCode>1.1</versionCode><versionName>1.0</versionName><clientType>01</clientType></ns:checkTelphone></SOAP-ENV:Body></SOAP-ENV:Envelope>
#%!oE$@@e{}`
#caxV;PPOST / HTTP/1.1
Accept-Encoding: identity
Content-Length: 805
Host: 123.125.96.6:8090
Content-Type:
Connection: close
User-Agent: Python-urllib/2.7

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body><ns:uploadCertificateInfo><deviceID>0000000000000000</deviceID><communicaID>006D</communicaID><agentId>AA3C9309459562D9E04C47F38CAC04A6</agentId><telplone>2741AD34F808F198D506664F25BF3BED</telplone><certificateName>5E22BCEA426CEC30</certificateName><certificateType>8D1B6F7327986F7F</certificateType><certificateNum>8E52943D267AC851D05BB094B9FD8FD5DF3C91FB895D270C</certificateNum><certificateAdd>BB28AD9FDC3EB802BB28AD9FDC3EB802</certificateAdd><clientType>01</clientType></ns:uploadCertificateInfo></SOAP-ENV:Body></SOAP-ENV:Envelope>
'''
def saveteltruename(request):
    ap=getParam(request)
    res=ap.get('res',u'')
    del ap['res']
    if  isinstance(ap,HttpResponse):
        return ap
    ltlogin()
    result=ltv(ap.get('tel'),ap.get('phone'),False)
    if result.get('success'):
        respone=ltc(ap.get('phone'),False)
        if respone.get('success'):
            r=ltsave(ap)
            return HttpResponse(res+r.get('msg',{}).get('desc'))

    return HttpResponse(res+result.get('msg'))


def ltsave(ap,flag=False):
    # data=urllib.urlencode(ap)
    # k=ltlogin()

    # agentid=getpwd('1103855807',LTKEY)

    name=getpwd(ap.get('name'),LTKEY)
    number=getpwd(ap.get('number'),LTKEY)
    address=getpwd(ap.get('address'),LTKEY)
    tel=getpwd(ap.get('phone'),LTKEY)
    request = urllib2.Request('http://123.125.96.6:8090',' ')
    try:
        response = urllib2.urlopen(request,ltuploadstr.replace('\n','')%(tel,name,number,address))
        result= response.read()
        tradeState_start=result.find('tradeState')
        tradeState_end=result.rfind('tradeState')
        tradeState=result[tradeState_start+11:tradeState_end-2]
        description_start=result.find('description')
        description_end=result.rfind('description')
        description=result[description_start+len('description')+1:description_end-2]
        if tradeState=='0000':

                return {'success':True,'msg':u'手机号可可以出售'}

        else:
            return {'success':False,'msg':description.decode('utf-8')}

    except Exception,e:
        return {'success':False,'msg':u'账号异常，请联系管理员'}

def ltcheckteltruename(request):
    ap=getParam(request)
    res=ap.get('res',u'')
    del ap['res']
    if  isinstance(ap,HttpResponse):
        return ap
    result=ltv(ap.get('tel'),ap.get('phone'),False)
    return HttpResponse(res+result.get('msg'))




def getParam(request):
    tel=request.REQUEST.get('tel','')
    phone=request.REQUEST.get('phone','')
    name=request.REQUEST.get('name','')
    number=request.REQUEST.get('number','')
    address=request.REQUEST.get('address','')
    if not tel:
        return HttpResponse(u'请提供手机号码')
    if not name:
        return HttpResponse(u'请提供姓名')
    if not number:
        return HttpResponse(u'请提供身份证号')
    if not address:
        return HttpResponse(u'请提供地址')
    ap={'name':name.encode('gbk'),'number':number,'tel':tel,'phone':phone,'address':address.encode('gbk'),'res':u'手机号:%s\n姓名:%s\n身份证号:%s\n地址:%s\n'%(tel,name,number,address)}
    return ap
