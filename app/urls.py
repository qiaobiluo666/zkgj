from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve

from django.views.decorators.csrf import csrf_exempt
from app.views import LoginViews,UserViews,CourseViews,HtzhglViews,CourseTimeViews,TeacherView,UserChooseViews,ZkgjViews
from demo import settings

urlpatterns = [
    path("index/", LoginViews.index,name="index"),
    path("login/", LoginViews.login,name="login"),
    path('index/main/',LoginViews.main,name="main"),


    path('index/user/',UserViews.user,name="user"),
    # re_path(r'^index/user/edit/(?P<pk>\d+)/',views.user_edit,name="user_edit"),
    path('index/user/edit/',UserViews.user_edit,name="user_edit"),
    path('index/user/add/',UserViews.user_add,name="user_add"),
    path('index/user/delete/',UserViews.user_delete,name="user_delete"),

    path('index/htzhgl/', HtzhglViews.user, name="user"),
    # re_path(r'^index/user/edit/(?P<pk>\d+)/',views.user_edit,name="user_edit"),
    path('index/htzhgl/edit/', HtzhglViews.user_edit, name="user_edit"),
    path('index/htzhgl/add/', HtzhglViews.user_add, name="user_add"),
    path('index/htzhgl/delete/', HtzhglViews.user_delete, name="user_delete"),



    path('index/course/',CourseViews.course,name="course"),
    path('index/course/add/',CourseViews.course_add,name="course_add"),
    path('index/course/edit/', CourseViews.course_edit, name="course_edit"),
    path('index/course/edit/video/', CourseViews.course_video, name="course_video"),
    path('index/course/edit/image/', CourseViews.course_image, name="course_image"),
    path('index/course/delete/', CourseViews.course_delete, name="course_delete"),

    path('index/kcsj/', CourseTimeViews.user, name="user"),
    # re_path(r'^index/user/edit/(?P<pk>\d+)/',views.user_edit,name="user_edit"),
    path('index/kcsj/edit/', CourseTimeViews.user_edit, name="user_edit"),
    path('index/kcsj/add/', CourseTimeViews.user_add, name="user_add"),
    path('index/kcsj/delete/', CourseTimeViews.user_delete, name="user_delete"),

    path('index/teacher/', TeacherView.user, name="user"),
    # re_path(r'^index/user/edit/(?P<pk>\d+)/',views.user_edit,name="user_edit"),
    path('index/teacher/edit/', TeacherView.user_edit, name="user_edit"),
    path('index/teacher/add/', TeacherView.user_add, name="user_add"),
    path('index/teacher/image/', TeacherView.user_image, name="user_image"),
    path('index/teacher/delete/', TeacherView.user_delete, name="user_delete"),


    path('index/choose/', UserChooseViews.UserChooseView.as_view(), name="user"),
    # re_path(r'^index/user/edit/(?P<pk>\d+)/',views.user_edit,name="user_edit"),
    path('index/choose/edit/', UserChooseViews.UserChooseEditView.as_view(), name="user_edit"),
    path('index/choose/edit/time/', UserChooseViews.UserChooseEditTimeView.as_view(), name="user_edit"),
    path('index/choose/edit/teacher/', UserChooseViews.UserChooseEditTeacherView.as_view(), name="user_edit"),
    path('index/choose/add/', UserChooseViews.UserChooseAddView.as_view(), name="user_add"),
    path('index/choose/delete/', UserChooseViews.UserChooseDeleteView.as_view(), name="user_delete"),

    # path('index/zkgj/', ZkgjViews.user, name="zkgj"),
    # path('index/zkgj/edit/', ZkgjViews.user_edit, name="zkgj_edit"),
    # path('index/zkgj/add/', ZkgjViews.user_add, name="zkgj_add"),
    # path('index/zkgj/image/', ZkgjViews.user_image, name="zkgj_image"),
    # path('index/zkgj/delete/', ZkgjViews.user_delete, name="zkgj_delete"),
]