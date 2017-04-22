from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^courses/$', views.course_list),
]
