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
from api.serializer.account import NewsModelSerializer, NewsDetailModelSerializer, TeacherModelSerializer
from app import models
# from api.serializer.account import MessageSerializer,LoginSerializer,NewsModelSerializer,NewsDetailModelSerializer
import uuid

class courseView (APIView):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        queryset = models.Course.objects.filter(id=request.data['courseid'],is_delete=0)
        ser_course = NewsModelSerializer(instance=queryset,many=True)

        teacher = models.teacher.objects.filter(is_delete=0)
        ser_teacher = TeacherModelSerializer(instance=teacher,many=True)

        return Response({"teacher":ser_teacher.data,"course":ser_course.data})