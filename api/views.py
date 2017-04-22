from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from api.models import Course


def index(request):
    return render(request, 'home.html')

# def course_list(request):
#     courses = Course.objects.all()
#     output = ', '.join([str(course) for course in courses])
#     return HttpResponse(output)

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', { "courses": courses})

def course_detail(request, pk):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})