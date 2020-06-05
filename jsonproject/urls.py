"""jsonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from myapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('student_create', views.student_create, name='student_create'),
    re_path(r'^display/\D+/',views.display,name='display'),
    path('student_update/<int:id>', views.student_update, name='student_update'),
    path('student_delete/<int:id>', views.student_delete, name='student_delete'),
    url(r'^api/studentmodify/(?P<pk>[0-9]+)$', views.student_detail),
    url(r'^api/studentcreate$', views.student_list),
]
