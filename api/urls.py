from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^courses/$', views.course_list),
    url(r'^courses/(?P<pk>\d+)/$', views.course_detail),
]
