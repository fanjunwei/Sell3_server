# coding=utf-8
#Date:2014/9/29
#Email:wangjian2254@gmail.com
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from sell3.tools import permission_required

__author__ = u'王健'



@login_required
@permission_required
def user_weixin_page(request):
    return render_to_response('oa/userWeiXinList.html', RequestContext(request, {}))


@login_required
@permission_required
def user_weixin_list_page(request):
    userquery = User.objects.filter(is_active=False).exclude(person__weixinid=None)

    return render_to_response('oa/userWeiXinListPage.html', RequestContext(request, {'userlist': userquery}))

