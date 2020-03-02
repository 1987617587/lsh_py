"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from wages.views import *
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()

router.register("workers", WorkersViewSet)
router.register("department", DepartmentViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    # 为了方便 此处忽略api/版本号
    url('', include(router.urls))
]
