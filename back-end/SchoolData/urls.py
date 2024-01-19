"""SchoolData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Login/", views.Login.as_view()),
    path("Query/", views.Query.as_view()),
    path("QuerybyRegion/", views.QuerybyRegion.as_view()),
    path('image/create/', views.CreateImageView.as_view(), name='create_image'),
    path('image/delete/', views.DeleteImageView.as_view(), name='delete_image'),
    path('image/search/', views.GetImageView.as_view(), name='get_image'),
    #path('image/search2/', views.GetImageView2.as_view(), name='get_image2'),
    path('idlist/', views.GetIdsBynameView.as_view(), name='get_image2'),

]

# 添加用于提供媒体文件的URL配置
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)