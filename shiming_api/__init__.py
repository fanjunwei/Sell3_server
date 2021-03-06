# coding=utf-8
# Date: 15/1/4
# Time: 14:16
# Email:fanjunwei003@163.com
from threading import local
import base64
import os
import requests
from sell3.models import Truename

__author__ = u'范俊伟'


class Shiming:
    cookies = {}
    username = None
    password = None
    errorMsg = local()
    photo = local()
    exception = local()
    result = local()

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()

    def encrypt(self, value):
        encrypt_jar = os.path.join(os.path.dirname(__file__), "shiming.jar").replace('\\', '/')
        res = os.popen('java -jar %s %s' % ( encrypt_jar, value))
        data = res.read()
        data = base64.decodestring(data)
        return data


    def login(self):
        try:
            username = self.encrypt(self.username)
            password = self.encrypt(self.password)
            data = {
                "u": username,
                "p": password
            }

            r = requests.post("http://channel.bj.chinamobile.com/channelApp/sys/login", data=data)

            if r.status_code == 200:
                self.cookies['JSESSIONID'] = r.cookies['JSESSIONID']
                # {u'data': {u'registerVer': u'1394435524000'}, u'success': u'true'}
                # {u'msg': {u'code': u'1', u'desc': u'\u8d26\u53f7\u4e0d\u5b58\u5728\uff01'}, u'success': u'false'}
                res = r.json()
                self.result.value = res
                success = res.get('success')
                self.errorMsg.value = res.get('msg', {}).get('desc', None)
                return success == 'true'
            else:
                self.errorMsg.value = u'网络错误(%d),请稍后重试' % r.status_code
                return False
        except Exception, e:
            self.exception.value = e
            self.errorMsg.value = u'内部错误,请稍后重试'
            return False


    def verifyIdentity(self, phone, name, number, *args, **kwargs):
        try:
            phone = self.encrypt(phone)
            name = self.encrypt(name)
            number = self.encrypt(number)
            data = {
                "phone": phone,
                "name": name,
                "number": number,
            }

            r = requests.post("http://channel.bj.chinamobile.com/channelApp/identity/verifyIdentity", data=data,
                              cookies=self.cookies)
            if r.status_code == 200:
                res = r.json()
                self.result.value = res
                self.errorMsg.value = res.get('msg', {}).get('desc', None)
                if res.get('msg', {}).get('code') == 300:
                    if self.login():
                        return self.verifyIdentity(phone, name, number)
                    else:
                        return False
                else:
                    success = res.get('success')
                    self.photo.value = res.get('data', {}).get('photo', None)
                    return success == 'true'
            else:
                self.errorMsg.value = u'网络错误(%d),请稍后重试' % r.status_code
                return False
        except Exception, e:
            self.exception.value = e
            self.errorMsg.value = u'内部错误,请稍后重试'
            return False

    def saveIdentity(self, phone, name, address, number, ethnic='', cred_type='0', user=None, o=None, *args, **kwargs):
        if len(number) == 18:
            birth = number[6:14]
            sex = int(number[-2:-1])

        elif len(number) == 15:
            birth = '19' + number[4:12]
            sex = int(number[-1:])
        else:
            self.errorMsg.value = u'身份证号不正确'
            return False

        if sex % 2 == 0:
            gender = 1
        else:
            gender = 0

        try:
            if not getattr(self.photo, "value", None):
                if not self.verifyIdentity(phone, name, number):
                    return False

            data = {
                "phone": self.encrypt(phone),
                "name": self.encrypt(name),
                "gender": self.encrypt(gender),
                "ethnic": self.encrypt(ethnic),
                "birth": self.encrypt(birth),
                "address": self.encrypt(address),
                "cred_type": self.encrypt(cred_type),
                "number": self.encrypt(number),
                "photo": getattr(self.photo, "value", ""),  # photo 无需加密
            }

            r = requests.post("http://channel.bj.chinamobile.com/channelApp/identity/saveIdentity", data=data,
                              cookies=self.cookies)
            if r.status_code == 200:
                res = r.json()
                self.result.value = res
                self.errorMsg.value = res.get('msg', {}).get('desc', None)
                if res.get('msg', {}).get('code') == 300:
                    if self.login():
                        return self.verifyIdentity(phone, name, number)
                    else:
                        return False
                else:
                    success = res.get('success')
                    success = (success == 'true')
                    if success:
                        try:
                            if o == None:
                                order = Truename()
                                order.tel = phone
                                order.name = name
                                order.number = number
                                order.address = address
                                order.company = 'yidong'
                                order.user = user
                                order.status = 1
                                order.save()
                        except:
                            pass
                    return success
            else:
                self.errorMsg.value = u'网络错误(%d),请稍后重试' % r.status_code
                return False
        except Exception, e:
            self.exception.value = e
            self.errorMsg.value = u'内部错误,请稍后重试'
            return False

    def getLastError(self):
        message = getattr(self.errorMsg, "value", u"")
        if type(message) == str:
            message = message.encode('utf-8')
        return message

    def getLastException(self):
        return getattr(self.exception, "value", None)

    def getLastResult(self):
        return getattr(self.result, "value", {})

    def getPhoto(self):
        return getattr(self.photo, "value", None)


