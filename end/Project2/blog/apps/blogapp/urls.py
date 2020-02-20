from django.conf.urls import url
from django.urls import path, include

from blogapp import admin, views
app_name = 'blogapp'
urlpatterns = [
    # url(r'^index/$',views.index,name='index'),

    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^favicon.ico$', views.favicon, name='favicon'),

]
