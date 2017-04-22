from django.contrib import admin
from api.models import Post, Comment, Course, Step

# Register your models here.


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(Step)