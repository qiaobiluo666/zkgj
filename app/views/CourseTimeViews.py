# _*_ coding: utf-8 _*_
import uuid

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.forms import model_to_dict
from django.core import serializers
from django.utils.decorators import method_decorator

from untils.app.functions import *
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from demo.settings import MEDIA_ROOT,MEDIA_URL
from app import models


"""
    用户账户信息展示界面
"""
# class NewsModelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Course_time
#         fields = ['id', 'start_time', 'end_time',  "course", 'teacher']
#
#     def get_Course(self, obj):
#         return model_to_dict(obj.Course, fields=['id', 'name'])


# @method_decorator(csrf_exempt)
# @method_decorator(xframe_options_exempt)
# class user(APIView):
#     def get(self,request,*args,**kwargs):
#         queryset = models.Course_time.objects.filter(is_delete=0)
#         ser = NewsModelSerializer(instance=queryset, many=True)
#         print(ser.data)
#         return Response(ser.data)
#     def post(self,request,*args,**kwargs):
#         return Response( status=200)
@csrf_exempt
@xframe_options_exempt
def user(request):
        if request.method == "GET":
            Course_time = models.Course_time.objects.filter(is_delete=0)
            teacher_name = models.teacher.objects.filter(is_delete=0)
            kc = models.Course.objects.filter(is_delete=0)
            Course_time = serializers.serialize("json", Course_time)
            kc = serializers.serialize("json", kc)
            teacher_name = serializers.serialize("json", teacher_name)
            data = {}
            data["Course_time"] = Course_time
            data["teacher_name"] = teacher_name
            data["kc"] = kc
            return HttpResponse(json.dumps(data))
        else:
            kcid = request.POST.get("kcid")
            Course_time = models.Course_time.objects.filter(is_delete=0,course__id=kcid)
            teacher_name = models.teacher.objects.filter(is_delete=0)
            kc = models.Course.objects.filter(is_delete=0)
            Course_time = serializers.serialize("json", Course_time)
            kc = serializers.serialize("json", kc)
            teacher_name = serializers.serialize("json", teacher_name)
            data = {}
            data["Course_time"] = Course_time
            data["teacher_name"] = teacher_name
            data["kc"] = kc
            return HttpResponse(json.dumps(data))
"""
    用户账户信息编辑界面
"""
@csrf_exempt
@xframe_options_exempt
def user_edit(request):
    if request.method == "GET":
        teacher = models.teacher.objects.filter(is_delete=0).values('id', "name")
        course = models.Course.objects.filter(is_delete=0).values('id', 'name')
        return render(request, "./page/CourseTime/edit.html", context={'teacher': teacher, "course": course})
    else:
        uuid, time, czy = uuid_time_czy(request)
        id =request.POST.get('f_id')
        course = request.POST.get('course')
        start_time = request.POST.get('startDate')
        end_time = request.POST.get('endDate')
        teacher = request.POST.get('box')
        teacher = teacher[1:len(teacher) - 1].replace('"', "").split(",")
        start_time = datetime_change(start_time)
        end_time = datetime_change(end_time)
        models.Course_time.objects.filter(id=id, is_delete=0).update(start_time=start_time, end_time=end_time, course=course,
                                                                 is_delete=False, token=uuid,
                                                                last_time=time, czy=czy)
        course_obj = models.Course_time.objects.get(id=id)
        course_obj.teacher.clear()
        course_obj.teacher.set(teacher)

        return HttpResponse(json.dumps({"data":'11',"media":"200"}))
"""
    用户账户信息添加界面
"""
@csrf_exempt
@xframe_options_exempt
def user_add(request):
    if request.method == "GET":
        teacher = models.teacher.objects.filter(is_delete=0).values('id',"name")
        course = models.Course.objects.filter(is_delete=0).values('id','name')
    
        return render(request, "./page/CourseTime/edit.html", context={'teacher': teacher,"course":course})

    else:
        uuid,time,czy = uuid_time_czy(request)
        course = request.POST.get('course')
        start_time = request.POST.get('startDate')
        end_time = request.POST.get('endDate')
        teacher = request.POST.get('box')
        start_time = datetime_change(start_time)
        end_time = datetime_change(end_time)

        status = models.Course_time(course_id=course, start_time=start_time, end_time=end_time,  is_delete=False,
                               token=uuid,
                               last_time=time, czy=czy)
        status.save()

        course_obj = models.Course_time.objects.get(id=status.id)
        teacher = teacher[1:len(teacher)-1].replace('"',"").split(",")
        print(teacher)
        for i in teacher:
            teacher_obj = models.teacher.objects.get(id=int(float(i)))
            course_obj.teacher.add(teacher_obj)


        # status = models.User(username=username,password=password,address=address,is_delete=False,token=uuid,last_time=time,czy=czy)
        # status.save()
        return HttpResponse(json.dumps({"status":"1","msg":"添加成功！"}))

@csrf_exempt
@xframe_options_exempt
def user_delete(request):
    if request.method == "POST":
        uuid, time, czy = uuid_time_czy(request)
        data = request.POST.get("delIds")
        print(data)
        for i in data.split(","):
            models.Course_time.objects.filter(id=i).update(is_delete=1,token=uuid,last_time=time,czy=czy)
        return HttpResponse(json.dumps({"data":'11',"media":"200"}))