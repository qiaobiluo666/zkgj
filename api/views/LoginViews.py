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
from app import models
# from api.serializer.account import MessageSerializer,LoginSerializer,NewsModelSerializer,NewsDetailModelSerializer
import uuid

class loginView (APIView):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        username = request.data["username"]
        password = request.data["password"]
        name = models.User.objects.filter(username=username,is_delete=0)
        if name:
            for i in name:
                if password==i.password:
                    token = i.token
                    return Response({"status":True,"message":"登陆成功","token":token,"userid":i.id})

                else:
                    return Response({"status": False, "message": "账号或密码有误"})
        else:

            return Response({"status": False, "message": "账号或密码有误"})