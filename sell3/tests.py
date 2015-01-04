#coding=utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import urllib
import urllib2,json

from django.test import TestCase
import Sell3_server
from Sell3_server.settings import COOKIES


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
#
# from Crypto.Cipher import AES
# import os
# import base64
#
# BS = AES.block_size
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# unpad = lambda s : s[0:-ord(s[-1])]
#
# #key = os.urandom(16) # the length can be (16, 24, 32)
# #text = 'to be encrypted'
# key = '12345678901234567890123456789012' # the length can be (16, 24, 32)
# #text = '1234567890123456'
# #text = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
# text = 'bj040_01'
#
# cipher = AES.new(key)
#
# #encrypted = cipher.encrypt(pad(text)).encode('hex')
# encrypted = cipher.encrypt(pad(text))
# print encrypted  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'
# result = base64.b64encode(encrypted)
# print result  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'
#
# #decrypted = unpad(cipher.decrypt(encrypted.decode('hex')))
# result2 = base64.b64decode(result)
# print result2  # will be 'to be encrypted'
# decrypted = unpad(cipher.decrypt(result2))
# print decrypted  # will be 'to be encrypted'
# p:Nsi4IrCROmbYPLrnKqtyqErzyWmPVk
# w:7dszIetwFCU_lTB78cxHHktz60Rrud

def v(data):
    request = urllib2.Request('http://channel.bj.chinamobile.com/channelApp/identity/verifyIdentity',data)
    request.add_header('Cookie', COOKIES.get('cookie',''))
    try:
        response = urllib2.urlopen(request)
        result= response.read()
        print result
        r=json.loads(result)
        if  r.get('success')=='false':
            if r.get('msg',{}).get('code',0)=='300':
                loginS()
                v(data)


    except Exception,e:
        print e



def save(data):
    request = urllib2.Request('http://channel.bj.chinamobile.com/channelApp/identity/saveIdentity',data)
    request.add_header('Cookie', COOKIES.get('cookie',''))
    try:
        response = urllib2.urlopen(request)
        result= response.read()
        print result


    except Exception,e:
        print e


def loginS():
    data = json.dumps({"u":"Nsi4IrCROmbYPLrnKqtyqErzyWmPVk", "p":"7dszIetwFCU_lTB78cxHHktz60Rrud"})
    request = urllib2.Request('http://channel.bj.chinamobile.com/channelApp/sys/login',data)
    # request = urllib2.Request('http://channel.bj.chinamobile.com/channelApp/sys/login?u=nSI_iRcroMByplRNkQvKQERZyytPmW&p=B%40WDCCCTT7wKNW5XlvV1slp38YmuCV')

    response = urllib2.urlopen(request)
    print response.read()
    cookies = response.headers["Set-cookie"]

    cookie = cookies[cookies.index("JSESSIONID"):]
    COOKIES['cookie'] = cookie[:cookie.index(";")+1]


def tellogin():

    datalist=[{'phone':'15901304543','name':'王伟','number':'152822198710226315'}]
    for dm in datalist:
        data=urllib.urlencode(dm)
        print data
        v(data)
        ap={'phone':dm['phone'],'name':dm['name'],'number':dm['number']}
        ap['birth']=dm['number'][6:14]
        ap['ethnic']=''
        ap['address']='北京'
        sex=int(dm['number'][-2:-1])
        if sex%2==0:
            ap['gender']=1
        else:
            ap['gender']=0
        ap['cred_type']='0'
        data2=urllib.urlencode(ap)
        print data2
        save(data2)

tellogin()
def urlparm():
    s='birth=19871022&ethnic=&phone=18801191987&address=%E5%A4%A9%E6%B4%A5&name=%E7%8E%8B%E4%BC%9F&gender=0&number=152822198710226315&cred_type=0'
    pl=s.split('&')
    for p in pl:
        print p
        for k in p.split('='):
            print urllib.unquote(k),
        print ''
# urlparm()

'''
gender 性别
ethnic 民族
cred_type 证件类型
'''

# from sell3.desstruct import *
# from sell3.des import *

# print desencode(u"1103855807".encode('gbk'),u"sunnada0".encode('gbk'))
'''
POST / HTTP/1.1
Accept-Encoding: gzip
User-Agent: Google-HTTP-Java-Client/1.15.0-rc (gzip)
Content-Length: 687
Host: 123.125.96.6:8090
Connection: Keep-Alive

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body>
<ns:mobileClientLogin>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<sendSMSflag>1</sendSMSflag>
<agentId>ADA658DD7BCD302965607BBFEE530EEC</agentId>
<agentPasswd>1CB942CDE5E5D625</agentPasswd>
<clientType>C310C73A81C69EAF</clientType>
<versionCode>E07E985011131EFC</versionCode>
<versionName>C6818C139D02F7B3</versionName>
<lac></lac><ci></ci></ns:mobileClientLogin>
</SOAP-ENV:Body></SOAP-ENV:Envelope>

HTTP/1.1 200 OK
Server: gSOAP/2.8
Content-Type: text/html; charset=utf-8
Content-Length: 1261
Connection: close

<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<ns:mobileClientLoginResponse>
<deviceID>0000000000000000</deviceID>
<communicaID>0008</communicaID>
<tradeState>0000</tradeState>
<description></description>
<clientType>C310C73A81C69EAF</clientType>
<ftpSerIP>AFFE5F896C0681913945DA14011D48D9</ftpSerIP>
<ftpSerPort>6700F97002B11734</ftpSerPort><
ftpSerUser>CDDE001807AD12F9</ftpSerUser>
<ftpSerPass>5F361207B50476322C3937D077060CE6</ftpSerPass>
<upLoadPATH>F92878AC4CBAFABE</upLoadPATH>
<upgradeFlag>37B91FE630E58597</upgradeFlag>
<newVerCode>C6818C139D02F7B3</newVerCode>
<newVerName>C6818C139D02F7B3</newVerName>
<newVerLog>653F3A08787C48F1779F0C971315A58F279CE4368E4A1D1A</newVerLog>
<upgradePATH>9C84E02B8AF9B213F44D56DF3262B059A9EE932880694779</upgradePATH>
<registerKey>qwertyui</registerKey>
<noticeFlag>0</noticeFlag>
<noticeTitle></noticeTitle>
<noticeMsg></noticeMsg>
</ns:mobileClientLoginResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>


lsp"aE@@1n{}`EO1/B
ia

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body><ns:checkTelphone>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<agentId>935CE99C05CE8E1DE04C47F38CAC04A6</agentId>
<telplone>CB06BAB8BABE34A77D694B3577D94A22</telplone>
<versionCode>1.1</versionCode><versionName>1.0</versionName>
<clientType>01</clientType></ns:checkTelphone>
</SOAP-ENV:Body></SOAP-ENV:Envelope>


HTTP/1.1 200 OK
Server: gSOAP/2.8
Content-Type: text/html; charset=utf-8
Content-Length: 800
Connection: close

<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<ns:checkTelphoneResponse>
<deviceID>0000000000000000</deviceID>
<communicaID>0018</communicaID>
<tradeState>0002</tradeState>
<description>(25007)</description>
<uploadType>2D7D4A5621BC7CC2</uploadType>
<certifyFlag>1000000</certifyFlag>
<noticeFlag>0</noticeFlag>
<noticeTitle></noticeTitle>
<noticeMsg></noticeMsg>
</ns:checkTelphoneResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>

<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<ns:checkTelphoneResponse>
<deviceID>0000000000000000</deviceID>
<communicaID>0000</communicaID>
<tradeState>0003</tradeState>
<description>该号码已登记，不能重复登记，请勿销售。(序号：20015)</description>
<uploadType>2D7D4A5621BC7CC2</uploadType>
<certifyFlag>1000000</certifyFlag>
<noticeFlag>0</noticeFlag>
<noticeTitle></noticeTitle>
<noticeMsg></noticeMsg>
</ns:checkTelphoneResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>

<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<ns:mobileClientLoginResponse>
<deviceID>0000000000000000</deviceID>
<communicaID>0008</communicaID>
<tradeState>0000</tradeState>
<description></description>
<clientType>C310C73A81C69EAF</clientType>
<ftpSerIP>AFFE5F896C0681913945DA14011D48D9</ftpSerIP>
<ftpSerPort>6700F97002B11734</ftpSerPort><
ftpSerUser>CDDE001807AD12F9</ftpSerUser>
<ftpSerPass>5F361207B50476322C3937D077060CE6</ftpSerPass>
<upLoadPATH>F92878AC4CBAFABE</upLoadPATH>
<upgradeFlag>37B91FE630E58597</upgradeFlag>
<newVerCode>C6818C139D02F7B3</newVerCode>
<newVerName>C6818C139D02F7B3</newVerName>
<newVerLog>653F3A08787C48F1779F0C971315A58F279CE4368E4A1D1A</newVerLog>
<upgradePATH>9C84E02B8AF9B213F44D56DF3262B059A9EE932880694779</upgradePATH>
<registerKey>qwertyui</registerKey>
<noticeFlag>0</noticeFlag>
<noticeTitle></noticeTitle>
<noticeMsg></noticeMsg>
</ns:mobileClientLoginResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>


<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns="urn:SmsWBS">
<SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<ns:mobileClientLoginResponse>
<deviceID>0000000000000000</deviceID>
<communicaID>0000</communicaID>
<tradeState>0000</tradeState>
<description>成功</description>
<clientType>C310C73A81C69EAF</clientType>
<ftpSerIP></ftpSerIP><ftpSerPort></ftpSerPort>
<ftpSerUser>CDDE001807AD12F9</ftpSerUser>
<ftpSerPass>5F361207B50476322C3937D077060CE6</ftpSerPass>
<upLoadPATH>F92878AC4CBAFABE</upLoadPATH>
<upgradeFlag>37B91FE630E58597</upgradeFlag>
<newVerCode>C310C73A81C69EAF</newVerCode>
<newVerName>3C640A39BFD17905</newVerName>
<newVerLog>653F3A08787C48F1779F0C971315A58F279CE4368E4A1D1A</newVerLog>
<upgradePATH>A8A62F17C3155CFA00C685128DF33406F23E90344BCAEC60</upgradePATH>
<registerKey>qwertyui</registerKey>
<noticeFlag>0</noticeFlag>
<noticeTitle></noticeTitle>
<noticeMsg></noticeMsg>
</ns:mobileClientLoginResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>


POST / HTTP/1.1
Accept-Encoding: gzip
User-Agent: Google-HTTP-Java-Client/1.15.0-rc (gzip)
Content-Length: 601
Host: 123.125.96.6:8090
Connection: Keep-Alive

<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns="urn:SmsWBS"><SOAP-ENV:Body>
<ns:checkTelphone>
<deviceID>0000000000000000</deviceID>
<communicaID>FFFF</communicaID>
<agentId>935CE99C05CE8E1DE04C47F38CAC04A6</agentId>
<telplone>CB06BAB8BABE34A77D694B3577D94A22</telplone>
<versionCode>1.1</versionCode>
<versionName>1.0</versionName>
<clientType>01</clientType>
</ns:checkTelphone></SOAP-ENV:Body></SOAP-ENV:Envelope>

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

import subprocess
ls=subprocess.call (["java -jar /Users/wangjian2254/work/django/Sell3_server/test.jar 1103855807 sunnada0"],shell=True)
print ls


