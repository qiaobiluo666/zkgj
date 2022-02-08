from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django_redis import get_redis_connection
from app import models

#
# class MessageSerializer(serializers.Serializer):
#     phone = serializers.CharField(label='手机号',validators=[phone_validator,])
#
# class LoginSerializer(serializers.Serializer):
#     phone = serializers.CharField(label='手机号', validators=[phone_validator, ])
#     code = serializers.CharField(label='短信验证码')
#
#     def validate_code(self, value):
#         if len(value) !=4:
#             raise ValidationError('短信格式错误')
#         if not value.isdecimal():
#             raise ValidationError('短信格式错误')
#
#         phone = self.initial_data.get('phone')
#         conn = get_redis_connection()
#         code = conn.get(phone)
#         if not code:
#             raise ValidationError('验证码过期')
#         if value != code.decode('utf-8'):
#             raise ValidationError('验证码错误')
#
#         return value
#
#
class NewsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = "__all__"

class TeacherModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.teacher
        fields = "__all__"
#
#
#
class NewsDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        #exclude 提出这个字段
        fields =  "__all__"
        def get_news(self, obj):
            return model_to_dict(obj.news, fields=['id', 'content'])


class TeacherSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()





class bmViewModelSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    class Meta:
        model = models.Course_time
        #exclude 提出这个字段
        fields =  "__all__"
    def get_course(self, obj):
        return model_to_dict(obj.course, fields=['id', 'name'])
        # 返回关联属性的主键，因为有多个，所以必须加上many=True


    # 钩子函数序列化,必须是以get_开头的
    def get_teacher(self, obj):
        teacher = obj.teacher.all()
        auth = TeacherSerializers(teacher, many=True)
        return auth.data


class XkViewModelSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    course_time = serializers.SerializerMethodField()

    class Meta:
        model = models.Course_choose
        # exclude 提出这个字段
        fields = "__all__"

    def get_course(self, obj):
        return model_to_dict(obj.course, fields=['id', 'name'])
        # 返回关联属性的主键，因为有多个，所以必须加上many=True

        # 钩子函数序列化,必须是以get_开头的

    def get_teacher(self, obj):
        return model_to_dict(obj.teacher, fields=['id', 'name'])

    def get_course_time(self, obj):
        return model_to_dict(obj.course_time, fields=['id', 'start_time'])