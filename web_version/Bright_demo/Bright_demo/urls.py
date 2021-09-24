"""Bright_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from Bright_demo_app.views import hello,hello1,hello2,hello3,hello4,hello5
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello1),
    url(r'^(\d+)/$',hello),
    url(r'^student/(\d+)/$',hello2),
    url(r'^children/(\d+)/$',hello3),
    path('creat_student',hello5),
    path('get',hello4)
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
