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
    XkViewModelSerializer
from app import models
# from api.serializer.account import MessageSerializer,LoginSerializer,NewsModelSerializer,NewsDetailModelSerializer
import uuid

class xkView (APIView):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        userid = request.data['userid']
        queryset = models.Course_choose.objects.filter(User=userid,is_delete=0)
        ser_course = XkViewModelSerializer(instance=queryset,many=True)
        return Response(ser_course.data)