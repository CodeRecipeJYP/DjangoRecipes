from django.contrib import admin
from api.models import Post, Comment, Course

# Register your models here.


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Course)