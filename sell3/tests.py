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
    request = urllib2.Request('http://channel.bj.chinamobile.com/channelApp/sys/login?u=nSI_iRcroMByplRNkQvKQERZyytPmW&p=B%40WDCCCTT7wKNW5XlvV1slp38YmuCV')
    # data = urllib.urlencode({"u":"nSI_iRcroMByplRNkQvKQERZyytPmW", "p":"B%40WDCCCTT7wKNW5XlvV1slp38YmuCV"})
    response = urllib2.urlopen(request)
    print response.read()
    cookies = response.headers["Set-cookie"]

    cookie = cookies[cookies.index("JSESSIONID"):]
    COOKIES['cookie'] = cookie[:cookie.index(";")+1]


def tellogin():

    datalist=[{'phone':'15901304635','name':'王伟','number':'152822198710226315'}]
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