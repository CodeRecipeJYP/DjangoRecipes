from django.contrib import admin
from api.models import Post, Comment, Course, Step

# Register your models here.

class StepInline(admin.StackedInline):
    model = Step

class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline, ]


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Course, CourseAdmin)
admin.site.register(Step)