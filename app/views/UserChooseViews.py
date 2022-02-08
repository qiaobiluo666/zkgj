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
# Create your views here.
from app import models

import json
import random
import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django_redis import get_redis_connection
# Create your views here.
from api.serializer.account import NewsModelSerializer, NewsDetailModelSerializer, TeacherModelSerializer, \
    bmViewModelSerializer
from api.serializer.validators import CourseChooseSerializer
from app import models
import uuid

from untils.app.functions import uuid_time_czy
@method_decorator(csrf_exempt,name="dispatch")
@method_decorator(xframe_options_exempt,name="dispatch")
class UserChooseView (APIView):
    def get(self,request,*args,**kwargs):
        queryset = models.Course_choose.objects.filter(is_delete=0).order_by('-id')
        ser_course = CourseChooseSerializer(instance=queryset, many=True)
        return Response(ser_course.data)



@method_decorator(csrf_exempt,name="dispatch")
@method_decorator(xframe_options_exempt,name="dispatch")
class UserChooseEditView (APIView):
    def get(self,request,*args,**kwargs):
        user = models.User.objects.filter(is_delete=0).values('id', "username")
        course = models.Course.objects.filter(is_delete=0).values('id', 'name')

        return render(request, "./page/UserChoose/edit.html", context={'user': user, "course": course})
    def post(self,request,*args,**kwargs):
        uuid, time, czy = uuid_time_czy(request)
        course = request.data['course']
        course_time = request.data['time']
        user = request.data['user']
        id = request.data['f_id']
        teacher = request.data['teacher']
        models.Course_choose.objects.filter(id=id, is_delete=0).update(course_id=course, course_time_id=course_time, teacher_id=teacher,
                                                                User_id=user, is_delete=False, token=uuid,
                                                                last_time=time, czy=czy)

        return HttpResponse(json.dumps({"result_code": 0}))




@method_decorator(csrf_exempt,name="dispatch")
@method_decorator(xframe_options_exempt,name="dispatch")
class UserChooseEditTimeView (APIView):


    def post(self,request,*args,**kwargs):
        course_id = request.data['course_id']
        queryset = models.Course_time.objects.filter(is_delete=0,course_id=course_id).values('id','start_time')
        print(queryset)


        return Response({"time": queryset})


@method_decorator(csrf_exempt,name="dispatch")
@method_decorator(xframe_options_exempt,name="dispatch")
class UserChooseEditTeacherView (APIView):


    def post(self,request,*args,**kwargs):
        time_id = request.data['time_id']
        queryset = models.Course_time.objects.filter(is_delete=0,id=time_id)
        ser_techaer = bmViewModelSerializer(instance=queryset,many=True)
        return Response(ser_techaer.data)


@method_decorator(csrf_exempt,name="dispatch")
@method_decorator(xframe_options_exempt,name="dispatch")
class UserChooseAddView (APIView):
    def get(self, request, *args, **kwargs):
        user = models.User.objects.filter(is_delete=0).values('id', "username")
        course = models.Course.objects.filter(is_delete=0).values('id', 'name')
        return render(request, "./page/UserChoose/edit.html", context={'user': user, "course": course})
    def post(self,request,*args,**kwargs):
        uuid, time, czy = uuid_time_czy(request)
        course = request.data['course']
        course_time = request.data['time']
        user = request.data['user']
        teacher = request.data['teacher']
        status =models.Course_choose(course_id=course, course_time_id=course_time,is_delete=0,
                                        teacher_id=teacher,User_id=user, token=uuid,last_time=time, czy=czy)
        status.save()
        return HttpResponse(json.dumps({"result_code": 0}))

@method_decorator(csrf_exempt,name="dispatch")
@method_decorator(xframe_options_exempt,name="dispatch")
class UserChooseDeleteView (APIView):

    def post(self,request,*args,**kwargs):
        uuid, time, czy = uuid_time_czy(request)
        data = request.data["delIds"]
        print(data,111)
        for i in data.split(","):
            models.Course_choose.objects.filter(id=i).update(is_delete=1, token=uuid, last_time=time, czy=czy)
        return HttpResponse(json.dumps({"data": '11', "media": "200"}))
