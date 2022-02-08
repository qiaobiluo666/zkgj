import datetime
import json
import locale
import uuid

"""
    传到前端的layui的数据格式
"""
def uuid_time_czy(request):
    uuId = uuid.uuid4()
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%m")
    czy = request.session.get("name")
    return uuId,time,czy


def datetime_change(x):
    x = x.replace("月",'-').replace("年",'-').replace("日",'').replace("时",':').replace("分","")
    time = datetime.datetime.strptime(x, "%Y-%m-%d %H:%M")
    print(time)
    return time


def  datetime_zw(x):
    x=x.strftime("%Y年%m月%d日 %H时%M分")
    print(x)
    return x