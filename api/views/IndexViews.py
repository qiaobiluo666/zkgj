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
from api.serializer.account import NewsModelSerializer
from app import models
# from api.serializer.account import MessageSerializer,LoginSerializer,NewsModelSerializer,NewsDetailModelSerializer
import uuid

class indexView (APIView):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        print(123)
        if request.data['min_id']:
                min_id = request.data['min_id']
                queryset = models.Course.objects.filter(id__lt=min_id,is_delete=0).order_by('-id')[0:4]
                for user in queryset:
                    print(user.id)
        elif request.data['max_id']:
            max_id = request.data['max_id']
            queryset = models.Course.objects.filter(id__gt=max_id,is_delete=0).order_by('id')[0:4]
        else:
            queryset = models.Course.objects.filter(is_delete=0).order_by('-id')[0:4]

        ser = NewsModelSerializer(instance=queryset, many=True)
        return Response(ser.data,status=200)