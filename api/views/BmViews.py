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
from app import models
import uuid

from untils.app.functions import uuid_time_czy


class bmView (APIView):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):

        courseid = request.data['courseid']
        queryset = models.Course_time.objects.filter(course__id=courseid, is_delete=0).order_by('-id')
        ser_course = bmViewModelSerializer(instance=queryset, many=True)
        # queryset = models.Course.objects.filter(id=request.data['newid'],is_delete=0)
        # ser_course = NewsModelSerializer(instance=queryset,many=True)
        #
        # teacher = models.teacher.objects.filter(is_delete=0)
        # ser_teacher = TeacherModelSerializer(instance=teacher,many=True)
        return Response(ser_course.data)



class bmdetilView (APIView):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        timeid = request.data['time']
        teacher = request.data['teacher']
        userid = request.data['userid']
        courseid = request.data['courseid']
        is_bm = models.Course_choose.objects.filter(course_id=courseid,course_time_id=timeid,User_id=userid,is_delete=0).values()
        if is_bm.count() == 0:
            uuid, time, czy = uuid_time_czy(request)
            user = models.User.objects.filter(id=userid,is_delete=0)
            username = user[0].username
            status = models.Course_choose(course_id=courseid, course_time_id=timeid, teacher_id=teacher, is_delete=False,User_id=userid,
                                        token=uuid,
                                        last_time=time, czy=username)
            status.save()
            return Response({"status": True, "message": "报名成功"})
        else:
            return Response({"status": False, "message": "已经报名请勿重复报名"})
