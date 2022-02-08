# _*_ coding: utf-8 _*_
import uuid

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

"""
    用户账户信息展示界面
"""
@csrf_exempt
@xframe_options_exempt
def user(request):
    if request.method == "GET":
        user = models.User.objects.filter(is_delete=0)
        data = serializers.serialize("json", user)
        return HttpResponse(data)
"""
    用户账户信息编辑界面
"""
@csrf_exempt
@xframe_options_exempt
def user_edit(request):
    if request.method == "GET":
        return render(request, "./page/users/edit.html")
    else:
        uuid, time, czy = uuid_time_czy(request)
        id =request.POST.get('f_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        models.User.objects.filter(id=id,is_delete=0).update(username=username,password=password,address=address,token=uuid,last_time=time,czy=czy)
        return HttpResponse(json.dumps({"data":'11',"media":"200"}))
"""
    用户账户信息添加界面
"""
@csrf_exempt
@xframe_options_exempt
def user_add(request):
    if request.method == "GET":
        return render(request, "./page/users/edit.html")
    else:
        uuid,time,czy = uuid_time_czy(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        print(username,password,address)
        status = models.User(username=username,password=password,address=address,is_delete=False,token=uuid,last_time=time,czy=czy)
        status.save()
        return HttpResponse(json.dumps({"status":"1","msg":"添加成功！"}))

@csrf_exempt
@xframe_options_exempt
def user_delete(request):
    if request.method == "POST":
        uuid, time, czy = uuid_time_czy(request)
        data = request.POST.get("delIds")
        for i in data.split(","):
            models.User.objects.filter(id=i).update(is_delete=1,token=uuid,last_time=time,czy=czy)
        return HttpResponse(json.dumps({"data":'11',"media":"200"}))