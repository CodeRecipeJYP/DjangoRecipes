from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from api.models import Course


def index(request):
    return HttpResponse("Hello world")

def course_list(request):
    courses = Course.objects.all()
    output = ', '.join([str(course) for course in courses])
    return HttpResponse(output)