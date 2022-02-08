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
        return render(request,"./index.html",{"data":'11',"media":"200"})

@csrf_exempt
@xframe_options_exempt
def main(request):
    if request.method == "GET":
        print(1111)
        return render(request, "./page/welcome-1.html")

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
        id =request.POST.get('f_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        models.User.objects.filter(id=id).update(username=username,password=password,address=address)
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        status = models.User(username=username,password=password,address=address,is_delete=False)
        status.save()
        return HttpResponse(json.dumps({"status":"1","msg":"添加成功！"}))

@csrf_exempt
@xframe_options_exempt
def user_delete(request):
    if request.method == "POST":
        username = request.POST.get('username')
        print(username,333)
        return HttpResponse(json.dumps({"data":'11',"media":"200"}))

@csrf_exempt
@xframe_options_exempt
def course(request):
    if request.method == "GET":
        user = models.Course.objects.filter(is_delete=0)
        data = serializers.serialize("json", user)
        return HttpResponse(data)

"""
    课程信息编辑界面
"""
@csrf_exempt
@xframe_options_exempt
def course_edit(request):
    if request.method == "GET":
        return render(request, "./page/course/test.html")
    else:
        name = request.POST.get('username')
        print(name,"eidt")
        return HttpResponse(json.dumps({"result_code":0}))
"""
    用户账户信息添加界面
"""
@csrf_exempt
@xframe_options_exempt
def course_add(request):
    if request.method == "GET":
        return render(request, "./page/course/test.html")
    else:
        filename = request.FILES.get('file')
        print(filename)
        # path = default_storage.save(MEDIA_ROOT+'/image/' + image.name, ContentFile(image.read()))  # 保存文件
        return HttpResponse(json.dumps({"data": '11', "media": "200"}))
@csrf_exempt
@xframe_options_exempt
def course_delete(request):
    if request.method == "POST":
        username = request.POST.get('username')
        print(username,333)
        return HttpResponse(json.dumps({"data":'11',"media":"200"}))
