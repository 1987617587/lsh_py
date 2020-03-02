"""drfend URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from drfend.settings import MEDIA_ROOT
from shop.views import *
# 引入DRF自带的路由类
from rest_framework import routers

router = routers.DefaultRouter()
# 可以通过router默认路由注册资源
router.register('categories', CategoryViewSets)
router.register('goods', GoodViewsSets)
router.register('images', GoodImgsViewsSets)
router.register('users', UserViewsSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),
    path('', include(router.urls)),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # url(r'^category_list/$', category_list, name="category_list"),
    # url(r'^category_detail/(\d+)/$', category_detail, name="category_detail"),
    # url(r'^category_list/$', CategoryListView.as_view(), name="category_list"),
    # url(r'^category_detail/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name="category_detail"),
    # 为了在DRF路由调试页面 需要引入以下路由
    # path('', include('rest_framework.urls')),
]
