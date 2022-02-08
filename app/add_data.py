# import datetime
# import sys
# import os
# import django
#
# import uuid
# # 这两行很重要，用来寻找项目根目录，os.path.dirname要写多少个根据要运行的python文件到根目录的层数决定
# import requests
#
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(BASE_DIR)
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
# django.setup()
# from app import models
# def uuid_time(request):
#     uuId = uuid.uuid4()
#     time = datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%m")
#     czy = request.Session("name")
#     return uuId,time,czy
# def add_User():
#     #  获取出版社对象
#     uuId, time = uuid_time()
#     models.User.objects.create(last_time=time, token=uuId, username="222", password="222",address="啊啊",is_delete=False)
# def add_course():
#     #  获取出版社对象
#     uuId, time = uuid_time()
#     models.Course.objects.create(last_time=time, token=uuId, name="我是课程名称",kcjj="我是课程简介", is_delete=False,
#                                image_url=r"D:\Python_test\demo\media\image\hg.jpg",
#                                video_url=r"D:\Python_test\demo\media\video\test.mp4")
# if __name__ == "__main__":
#     # add_User()
#     add_course()
teacher = '["1","2"]'
teacher = teacher[1:len(teacher)-1].replace('"',"").split(",")
print(teacher)