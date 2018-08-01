from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Post  # models.py로부터 Post 모델을 가져온다.

admin.site.register(Post)  # Post를 관리자 페이지에 등록한다.