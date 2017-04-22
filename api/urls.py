from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^courses/$', views.course_list),
    url(r'^courses/(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail),
    url(r'^courses/(?P<pk>\d+)/$', views.course_detail),
]
