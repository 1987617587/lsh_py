"""wukong URL Configuration

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
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from rentcar.views import *
from wukong.settings import MEDIA_ROOT

router = routers.DefaultRouter()
router.register('shops', ShopViewSet)
router.register('cars', CarViewSet)
router.register('carimgs', CarImagesViewSet)
router.register('categories', CategoryViewSet)
router.register('cities', CityViewSet)
router.register('prices', PricesViewSet)
router.register('users', UserViewsSets)
router.register('orders', OrderViewsSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('rest_framework.urls')),
    url('', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 使用simplejwt认证
    url(r'^login/$', token_obtain_pair, name='login'),
    url(r'^refresh/$', token_refresh, name='refresh'),
    # 支持使用token获取用户信息
    url(r'^userinfo/$', getuserinfo, name='userinfo'),
    url(r'^userorders/$', getuserorders, name='getuserorders'),
    url(r'^userordersmoney/$', getuserordersmoney, name='getuserordersmoney'),

    # API文档地址
    path('docs/', include_docs_urls(title="RestFulAPI", description="RestFulAPI v1")),

]
