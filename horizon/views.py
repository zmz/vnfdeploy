# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import sys

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from horizon.models import Users

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def index(request):
    if request.session.get('session_u_id',default=None):
        session_u_id = request.session.get('session_u_id')
        user_login = Users.objects.get(u_id=session_u_id)
        user_info = {'u_id':user_login.u_id,'u_name':user_login.u_name,'u_enname':user_login.u_enname,
                      'u_email':user_login.u_email,'u_role':user_login.u_role,
                      'u_status':user_login.u_status
                      }
    else:
        return HttpResponseRedirect("/login/")

    return render_to_response('index.html',locals())

def login(request):

    if request.session.get('session_u_id',default=None):
        session_u_id = request.session.get('session_u_id')
        user_login = Users.objects.get(u_id=session_u_id)
        user_info = {'u_id':user_login.u_id,'u_name':user_login.u_name,'u_enname':user_login.u_enname,
                      'u_email':user_login.u_email,'u_role':user_login.u_role,
                      'u_status':user_login.u_status
                      }
        return HttpResponseRedirect("/")
    else:
        print "login fail"
        return_data = '用户登录失败'
        # return HttpResponse(json.dumps(return_data))

    if str(request.method) == "POST":
        form_type = request.POST.get('type','')
        if form_type == "login":
            engname = request.POST.get("engname",'')
            password = request.POST.get("password",'')

            try:
                check_login_user = Users.objects.get(u_enname=engname,u_password=password)
                if check_login_user:
                    request.session["session_u_id"] = check_login_user.u_id
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponseRedirect("/login/")
            except :
                return HttpResponseRedirect("/login/")
        else:
            pass
    return render_to_response('login.html',locals())

def logout(request):

    if request.session.get('session_u_id',default=None):
        del request.session["session_u_id"]

    return HttpResponseRedirect("/login/")