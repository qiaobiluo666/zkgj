from django.conf.urls import url
from django.contrib import admin
from api.views import LoginViews,IndexViews,CourseViews,BmViews,XkViews
urlpatterns = [
    url(r'^login/', LoginViews.loginView.as_view()),
    url(r'^index/', IndexViews.indexView.as_view()),
    url(r'^course/', CourseViews.courseView.as_view()),
    url(r'^bm/index/', BmViews.bmView.as_view(),name="bm"),
    url(r'^bm/detil/', BmViews.bmdetilView.as_view(),name='detil'),
    url(r'^xk/', XkViews.xkView.as_view()),
]
