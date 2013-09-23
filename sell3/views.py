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
from django.db.transaction import autocommit
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from Sell3_server.settings import COOKIES, MEDIA_ROOT
from sell3.models import Truename
from sell3.tools import getResult, client_login_required
from django.contrib.auth import  login as auth_login
from sell3.usernames import USERNAMES,LTKEY


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



def save(ap,user=None,o=None):
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
                if o==None:
                    order=Truename()
                    order.tel=ap.get('phone',None)
                    order.name=ap.get('name',None)
                    order.number=ap.get('number',None)
                    order.address=ap.get('address',None)
                    order.company='yidong'
                    order.user=user
                    order.status=1
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
    ap={'name':name.encode('utf-8'),'number':number,'phone':tel,'address':address.encode('utf-8'),'res':u'手机号:%s\n姓名:%s\n身份证号:%s\n地址:%s\n'%(tel,name,number,address)}
    return ap

def teltruename(request):
    ap=getParam(request)
    res=ap.get('res',u'')
    del ap['res']
    if  isinstance(ap,HttpResponse):
        return ap
    result=v(ap,False)
    if not result.get('success'):
        return HttpResponse(res+result.get('msg',{}).get('desc',u''))
    else:
        r=save(ap)
        return HttpResponse(res+r.get('msg',{}).get('desc'))


        # if not r.get('success'):
        #     return r.get('msg',{}).get('desc')
        # else:
        #     return


def checkteltruename(request):
    ap=getParam(request)
    res=ap.get('res',u'')
    del ap['res']
    if  isinstance(ap,HttpResponse):
        return ap
    result=v(ap,False)
    return HttpResponse(res+result.get('msg',{}).get('desc'))
    # if not result.get('success'):
    #     return result.get('msg',{}).get('desc',u'')
    # else:
    #     r=save(ap)
    #     return r.get('msg',{}).get('desc')

def saveteltruename(request):
    ap=getParam(request)
    res=ap.get('res',u'')
    del ap['res']
    if  isinstance(ap,HttpResponse):
        return ap
    r=save(ap)
    return HttpResponse(res+r.get('msg',{}).get('desc'))

@client_login_required
def androidCheck(request):
    ap=getParam(request)
    del ap['res']
    if  isinstance(ap,HttpResponse):
        return getResult(False,ap.content,None)
    result=v(ap,True)
    return getResult(result.get('success'),result.get('msg',{}).get('desc',u''),result)

@client_login_required
def androidSave(request):
    ap=getParam(request)
    del ap['res']
    if  isinstance(ap,HttpResponse):
        return getResult(False,ap.content,None)
    result=save(ap,request.user)
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
        # namedict={}
        faile=[]
        retel=[]
        for i in range(0,rownum):
            row_data = sheet.row_values(i,0,5)
            if str(int(row_data[0])) and row_data[1] and row_data[2] and row_data[3]:
                try:
                    order=Truename.objects.get(tel=str(int(row_data[0])))
                except:
                    order=None
                if order==None:
                    order=Truename()
                order.tel=str(int(row_data[0]))
                order.name=row_data[1]
                order.number=row_data[2]
                order.address=row_data[3]
                order.user=request.user
                order.status=0
                order.company='yidong'
                order.save()

            else:
                faile.append(i+1)
            # print row_data
        msg=u''
        if faile:
            msg+=u'第%s行数据不完整，无法进行实名制。'%(u'、'.join(faile),)
        if retel:
            msg+=u'<br/>第%s行,电话号码已经存在，无法进行实名制。'%(u'、'.join(retel),)
        if not msg:
            msg=u'上传成功。'
        return render_to_response('oa/excelUpload.html',RequestContext(request,{'msg':msg}))
    except:
        pass
    finally:
       os.remove(MEDIA_ROOT+newfilename)

@login_required
@autocommit
def autoSaveTel(request):
    '''
    自动实名认证
    '''
    num=0
    for o in Truename.objects.filter(status=0).order_by('datetime')[:10]:
        if 'yidong'==o.company:
            ap={'phone':o.tel,'name':o.name.encode('utf-8'),'number':o.number,'address':o.address.encode('utf-8')}
            r=v(ap,False)
            if r.get('success'):
                r=save(ap,request.user,o)
            if r.get('success'):
                o.status=1
            else:
                o.status=2
                o.help=r.get('msg',{}).get('desc',u'')
            o.save()
            num+=1
    return render_to_response('oa/truename.html',RequestContext(request,{'count':Truename.objects.filter(status=0).count(),'failcount':Truename.objects.filter(status=2).count()}))

@login_required
def reUpload(request):
    '''
    重新实名制
    '''
    Truename.objects.filter(status=2).update(status=0)
    return HttpResponseRedirect('/oa/getExcelPage/')

@login_required
def downloadTrue(request):
    response = HttpResponse(mimetype=u'application/ms-excel')
    filename = u'错误实名制列表.xls'
    response['Content-Disposition'] = (u'attachment;filename=%s' % filename).encode('utf-8')
    import xlwt
    from xlwt import Font, Alignment

    style1 = xlwt.XFStyle()
    font1 = Font()
    font1.height = 250
    font1.name = u'仿宋'
    style1.font = font1
    algn = Alignment()
    algn.horz = Alignment.HORZ_LEFT
    style1.alignment = algn
    style1.font = font1

    wb = xlwt.Workbook()
    ws = wb.add_sheet(u"错误实名制列表", cell_overwrite_ok=True)
    rownum = 0
    ws.write_merge(rownum, rownum, 0, 0, u'手机号', style1)
    ws.write_merge(rownum, rownum, 1, 1, u'姓名', style1)
    ws.write_merge(rownum, rownum, 2, 2, u'身份证号', style1)
    ws.write_merge(rownum, rownum, 3, 3, u'地址', style1)
    ws.write_merge(rownum, rownum, 4, 4, u'错误原因', style1)

    rownum += 1
    for o in Truename.objects.filter(status=2).order_by('datetime'):
        ws.write_merge(rownum, rownum, 0, 0, o.tel, style1)
        ws.write_merge(rownum, rownum, 1, 1,o.name , style1)
        ws.write_merge(rownum, rownum, 2, 2,o.number, style1)
        ws.write_merge(rownum, rownum, 3, 3, o.address, style1)
        ws.write_merge(rownum, rownum, 4, 4, o.help, style1)

        rownum += 1
    for i in range(5):
        ws.col(i).width = 256 * 20
    wb.save(response)
    return response
