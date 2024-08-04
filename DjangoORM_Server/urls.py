"""DjangoORM_Server URL Configuration

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
from parts.views import marks_list, models_list, search_parts

urlpatterns = [
    path("admin/", admin.site.urls),
    path('mark/', marks_list, name='marks_list'),
    path('model/', models_list, name='models_list'),
    path('search/part/', search_parts, name='search_parts'),
]
