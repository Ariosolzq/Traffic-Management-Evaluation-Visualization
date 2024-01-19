# Register your models here.
from django.contrib import admin
from App.models import Schoolprocess,Userinfo


# 在这里注册所有的表，先导入进来，再注册
admin.site.register(Schoolprocess)
admin.site.register(Userinfo)