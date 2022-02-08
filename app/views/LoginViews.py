# _*_ coding: utf-8 _*_
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.forms import model_to_dict
from django.core import serializers

from untils.app.functions import *
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from demo.settings import MEDIA_ROOT,MEDIA_URL
# Create your views here.
from app import models

def zhuang(func):
    def methon(request):
        if request.COOKIES.get("isLogin"):
           return func(request)
        else:
            return  render(request,"./page/login.html")
    return methon


@zhuang
def index(request):
    if request.method == "GET":
        return render(request, "index.html")


@csrf_exempt
def login(request):
    if request.method == "GET":
        print(request.GET.get("username"), 1111)
        return render(request, "./page/login.html")
    else:
        print(request.POST.get("username"), 1111)
        userID = request.POST.get("username")
        password1 = request.POST.get("password")
        username = models.Admin.objects.filter(is_delete=False)
        print(userID,111)
        for i in username:
            if userID == i.username:
                if password1 == i.password:
                    response = redirect("../index/")
                    response.set_cookie("isLogin", True, max_age=60*60*2)
                    request.session["name"] =i.username
                    return response
                else:
                    return HttpResponse("账号密码有误请重新输入111")
        else:
            return HttpResponse("账号密码有误请重新输入")

@csrf_exempt
@xframe_options_exempt
def main(request):
    if request.method == "GET":
        return render(request, "./page/welcome-1.html")
