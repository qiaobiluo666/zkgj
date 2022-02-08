# _*_ coding: utf-8 _*_
import time
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
from demo.settings import MEDIA_ROOT, MEDIA_URL, URL_ROOT
# Create your views here.
from untils.app.functions import *
from app import models



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
        return render(request, "./page/course/edit.html")
    else:
        print("编辑页面")
        uuid, time, czy = uuid_time_czy(request)
        id = request.POST.get("f_id")
        name = request.POST.get("name")
        kcjj = request.POST.get("kcjj")
        image_url = request.session.get('image_url')
        video_url = request.session.get('video_url')
        models.Course.objects.filter(id=id, is_delete=0).update(name=name, kcjj=kcjj, image_url=image_url,video_url=video_url, is_delete=False, token=uuid,
                             last_time=time, czy=czy)
        return HttpResponse(json.dumps({"result_code":0}))
"""
    用户账户信息添加界面
"""
@csrf_exempt
@xframe_options_exempt
def course_add(request):
    if request.method == "GET":
        return render(request, "./page/course/add.html")
    else:
        uuid,time,czy = uuid_time_czy(request)
        name = request.POST.get("name")
        kcjj = request.POST.get("kcjj")
        image_url = request.session.get('image_url')
        video_url = request.session.get('video_url')
        status = models.Course(name=name, kcjj=kcjj, image_url=image_url,video_url=video_url, is_delete=False, token=uuid,
                             last_time=time, czy=czy)
        status.save()
        return HttpResponse(json.dumps({"data": '11', "media": "200"}))


@csrf_exempt
@xframe_options_exempt
def course_image(request):
    if request.method == "POST":

        image = request.FILES.get('file')
        token = uuid.uuid4()
        image_name = str(int(time.time()))+str(token).replace("-","")+".jpg"
        default_storage.save(MEDIA_ROOT+'/image/course/' + image_name, ContentFile(image.read()))  # 保存文件
        image_url = URL_ROOT+'image/course/' + image_name
        request.session["image_url"]=image_url
        return HttpResponse(json.dumps({"data":'11',"media":"200"}))


@csrf_exempt
@xframe_options_exempt
def course_video(request):
    if request.method == "POST":
        video = request.FILES.get('file')
        # id = request.POST.get("id")
        token = uuid.uuid4()
        video_name = str(int(time.time())) + str(token).replace("-", "") + ".mp4"
        default_storage.save(MEDIA_ROOT + '/video/course/' + video_name, ContentFile(video.read()))  # 保存文件
        video_url = URL_ROOT + 'video/course/' + video_name
        request.session["video_url"] = video_url
        return HttpResponse(json.dumps({"data":'11',"media":"200"}))

@csrf_exempt
@xframe_options_exempt
def course_delete(request):
    if request.method == "POST":
        uuid, time, czy = uuid_time_czy(request)
        data = request.POST.get("delIds")
        for i in data.split(","):
            models.Course.objects.filter(id=i).update(is_delete=1, token=uuid, last_time=time, czy=czy)
        return HttpResponse(json.dumps({"data":'11',"media":"200"}))