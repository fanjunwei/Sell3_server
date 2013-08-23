#coding=utf-8
# Create your views here.
import os
import shutil
import urllib
import urllib2
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Sell3_server.settings import COOKIES, MEDIA_ROOT
from sell3.models import Truename
from sell3.tools import getResult, client_login_required
from django.contrib.auth import  login as auth_login
from sell3.usernames import USERNAMES


@login_required
def default(request):
    return render_to_response('main.html',RequestContext(request))
@login_required
def default2(request):
    return render_to_response('workframe.html',RequestContext(request))
@login_required
def top(request):
    return render_to_response('topnav.html',RequestContext(request))
@login_required
def menu(request):
    return render_to_response('menu.html',RequestContext(request))
@login_required
def welcome(request):
    return render_to_response('welcome.html',RequestContext(request,{'num':range(30)}))



def clientLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if username:
            userlist = User.objects.filter(username=username)[:1]
            if len(userlist)>0:
                user=userlist[0]
                if not user.is_active:
                    return getResult(False,u'用户已经离职，不能在使用本系统。')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():


            # Okay, security checks complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return getResult(True,u'登录成功')
        else:
            return getResult(False,u'用户名密码错误')


def v(ap,flag=False):
    data=urllib.urlencode(ap)
    request = urllib2.Request('http://channel.bj.chinamobile.com/channelApp/identity/verifyIdentity',data)
    request.add_header('Cookie', COOKIES.get('cookie',''))
    try:
        response = urllib2.urlopen(request)
        result= response.read()
        print result
        r=json.loads(result)
        if  r.get('success')=='false':
            if r.get('msg',{}).get('code',0)=='300':
                if loginS():
                    return v(ap,flag)
                else:
                    return {'success':False,'msg':{"desc":u'账号异常，请联系管理员'}}
            else:
                return {'success':False,'msg':{"desc":r.get('msg',{}).get('desc',u'账号异常，请联系管理员')}}
        else:
            if flag:
                return {'success':True,'msg':{"desc":u'身份证号和姓名匹配'},'photo':r.get('data',{}).get('photo','')}
            else:
                return {'success':True,'msg':{"desc":u'身份证号和姓名匹配'}}


    except Exception,e:
        return {'success':False,'msg':{"desc":u'账号异常，请联系管理员'}}



def save(ap):
    if len(ap['number'])==18:
        ap['birth']=ap['number'][6:14]
        sex=int(ap['number'][-2:-1])

    elif len(ap['number'])==15:
        ap['birth']='19'+ap['number'][4:12]
        sex=int(ap['number'][-1:])
    else:
        return {'success':False,'msg':{"desc":u'身份证号不正确'}}
    if sex%2==0:
        ap['gender']=1
    else:
        ap['gender']=0
    ap['ethnic']=''
    # ap['address']='北京'

    ap['cred_type']='0'
    data=urllib.urlencode(ap)
    print data
    # save(data2)
    request = urllib2.Request('http://channel.bj.chinamobile.com/channelApp/identity/saveIdentity',data)
    request.add_header('Cookie', COOKIES.get('cookie',''))
    try:
        response = urllib2.urlopen(request)
        result= response.read()
        print result
        r=json.loads(result)
        if  r.get('success')=='false':
            if r.get('msg',{}).get('code',0)=='300':
                if loginS():
                    return save(data)
                else:
                    return {'success':False,'msg':{"desc":u'账号异常，请联系管理员'}}
            else:
                return {'success':False,'msg':{"desc":r.get('msg',{}).get('desc',u'账号异常，请联系管理员')}}
        else:
            try:
                order=Truename()
                order.tel=ap.get('phone',None)
                order.name=ap.get('name',None)
                order.number=ap.get('number',None)
                order.address=ap.get('address',None)
                order.save()
            except:
                pass
            return {'success':True,'msg':{"desc":u'实名制认证成功'}}


    except Exception,e:
        return {'success':False,'msg':{"desc":u'账号异常，请联系管理员'}}


def loginS():
    request = urllib2.Request('http://channel.bj.chinamobile.com/channelApp/sys/login?%s'%USERNAMES)
    # data = urllib.urlencode({"u":"nSI_iRcroMByplRNkQvKQERZyytPmW", "p":"B%40WDCCCTT7wKNW5XlvV1slp38YmuCV"})
    response = urllib2.urlopen(request)
    result= response.read()
    cookies = response.headers["Set-cookie"]

    cookie = cookies[cookies.index("JSESSIONID"):]
    COOKIES['cookie'] = cookie[:cookie.index(";")+1]
    r=json.loads(result)
    if  r.get('success')=='true':
        return True
    else:
        return False

#
# def tellogin(ap,flag=False):
#
#     # datalist=[{'phone':'15901304635','name':'王伟','number':'152822198710226315'}]
#     # for dm in datalist:
#
#         # print data
#         result=v(data,flag)
#         if flag:
#             if not result.get('success'):
#                 return result
        # ap={'phone':dm['phone'],'name':dm['name'],'number':dm['number']}

def getParam(request):
    tel=request.REQUEST.get('tel','')
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
    ap={'name':name.encode('gbk'),'number':number,'phone':tel,'address':address.encode('gbk'),'res':u'手机号:%s\n姓名:%s\n身份证号:%s\n地址:%s'}
    return ap

def teltruename(request):
    ap=getParam(request)
    if  isinstance(ap,HttpResponse):
        return ap
    result=v(ap,False)
    if not result.get('success'):
        return HttpResponse(ap.get('res',u'')+result.get('msg',{}).get('desc',u''))
    else:
        r=save(ap)
        return HttpResponse(ap.get('res',u'')+r.get('msg',{}).get('desc'))


        # if not r.get('success'):
        #     return r.get('msg',{}).get('desc')
        # else:
        #     return


def checkteltruename(request):
    ap=getParam(request)
    if  isinstance(ap,HttpResponse):
        return ap
    result=v(ap,False)
    return HttpResponse(ap.get('res',u'')+result.get('msg',{}).get('desc'))
    # if not result.get('success'):
    #     return result.get('msg',{}).get('desc',u'')
    # else:
    #     r=save(ap)
    #     return r.get('msg',{}).get('desc')

def saveteltruename(request):
    ap=getParam(request)
    if  isinstance(ap,HttpResponse):
        return ap
    r=save(ap)
    return HttpResponse(ap.get('res',u'')+r.get('msg',{}).get('desc'))

@client_login_required
def androidCheck(request):
    ap=getParam(request)
    if  isinstance(ap,HttpResponse):
        return getResult(False,ap.content,None)
    result=v(ap,False)
    return getResult(result.get('success'),result.get('msg',{}).get('desc',u''),result)

@client_login_required
def androidSave(request):
    ap=getParam(request)
    if  isinstance(ap,HttpResponse):
        return getResult(False,ap.content,None)
    result=save(ap)
    return getResult(result.get('success'),result.get('msg',{}).get('desc',u''),result)



@login_required
def getExcelPage(request):
    return render_to_response('oa/excelUpload.html',RequestContext(request))


@login_required
def uploadExcel(request):
    import xlrd
    newfilename='%s.xls'%request.user.pk
    try:
        f=request.FILES['excel']
        fileatt=open(MEDIA_ROOT+newfilename,'wb+')
        for chunk in f.chunks():
            fileatt.write(chunk)
        fileatt.close()
        book = xlrd.open_workbook(MEDIA_ROOT+newfilename)
        sheet=book.sheet_by_name(book.sheet_names()[0])
        rownum=sheet.nrows
        namedict={}
        for i in range(1,rownum):
            row_data = sheet.row_values(i,1,2)
            print row_data
        return HttpResponse(u'成功')
    except:
        pass
    finally:
       os.remove(MEDIA_ROOT+newfilename)