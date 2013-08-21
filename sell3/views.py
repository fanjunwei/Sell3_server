#coding=utf-8
# Create your views here.
import urllib
import urllib2

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from sell3.tools import getResult
from django.contrib.auth import  login as auth_login


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
