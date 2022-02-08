# import random
# import re
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.generics import RetrieveAPIView
# from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework.exceptions import ValidationError
# from django_redis import get_redis_connection
# # Create your views here.
# from api import models
# from api.serializer.account import MessageSerializer,LoginSerializer,NewsModelSerializer,NewsDetailModelSerializer
# import uuid
#
#
#
#
#
# class messageView(APIView):
#     def post(self,request,*args,**kwargs):
#
#         # phone = request.data["phone"]
#         # #验证手机长度和格式是否正确
#         # ser = MessageSerializer(data=request.data)
#         # if not ser.is_valid():
#         #     print(ser.errors)
#         #     return Response({"status":False,'message':ser.errors})
#         # random_code = random.randint(100000,999999)
#         # conn = get_redis_connection()
#         # conn.set(phone,random_code,ex =30)
#
#         # stutas = send_message(phone,random_code)
#         # print(stutas)
#         #     # 属性可能是基本类型，也可能引用了另一个数据结构
#         #     # 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明
#         #     req = models.SendSmsRequest()
#         #     # 短信控制台: https://console.cloud.tencent.com/smsv2
#         #     # 短信应用ID: 短信SdkAppId在 [短信控制台] 添加应用后生成的实际SdkAppId，示例如1400006666
#         #     req.SmsSdkAppId = "1400593527"
#         #     # 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看
#         #     req.SignName = "一个牙不好的吃货"
#         #     # 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号
#         #     phone = "+86"+str(phone)
#         #     req.PhoneNumberSet = [phone]
#         #     # 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看
#         #     req.TemplateId = "1186284"
#         #     # 模板参数: 若无模板参数，则设置为空
#         #     req.TemplateParamSet = [str(random_code),"1"]
#         #     # 通过client对象调用DescribeInstances方法发起请求。注意请求方法名与请求对象是对应的。
#         #     # 返回的resp是一个DescribeInstancesResponse类的实例，与请求对象对应。
#         #     resp = client.SendSms(req)
#         #     # 输出json格式的字符串回包
#         #     print(resp.to_json_string(indent=2))
#         # except TencentCloudSDKException as err:
#         #     print(err)
#         return Response({"stutas":True,"message":"发送成功"})
# class loginView (APIView):
#     def post(self,request,*args,**kwargs):
#         ser = LoginSerializer(data=request.data)
#         if not ser.is_valid():
#             return Response({"status": False, 'message': '验证码错误'})
#
#         # 3. 去数据库中获取用户信息（获取/创建）
#         phone = ser.validated_data.get('phone')
#         # user_object, flag = models.UserInfo.objects.get_or_create(phone=phone)
#         # user_object.token = str(uuid.uuid4())
#         # user_object.save()
#
#         return Response({"status": True, "data": {"token": user_object.token, 'phone': phone}})
# #
# class NewsView(APIView):
#     def post(self,request,*args,**kwargs):
#         print(request.data)
#         if request.data['min_id']:
#             min_id = request.data['min_id']
#             queryset = models.News.objects.filter(id__lt=min_id).order_by('-id')[0:4]
#             for user in queryset:
#                 print(user.id)
#         elif request.data['max_id']:
#             max_id = request.data['max_id']
#             queryset = models.News.objects.filter(id__gt=max_id).order_by('id')[0:4]
#             print(queryset)
#         else:
#             queryset = models.News.objects.all().order_by('-id')[0:4]
#         ser = NewsModelSerializer(instance=queryset,many=True)
#         return Response(ser.data,status=200)
#
#
# class NewsDetialView(APIView):
#     def post(self,request,*args,**kwargs):
#         # queryset = models.NewsDetail.objects.filter(news_id=request.data['newid'])
#         # ser = NewsDetailModelSerializer(instance=queryset, many=True)
#         # print(ser.data)
#         # return Response(ser.data, status=200)
#
#
#
#
#
