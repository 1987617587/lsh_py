from django.conf.urls import url
from . import views
app_name = "booktest"
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^detail/(\d+)/$', views.detail,name='detail'),
    url(r'^delbook/(\d+)/$', views.delbook,name='delbook'),
    url(r'^delhero/(\d+)/$', views.delhero, name='delhero'),
    url(r'^addbook/$', views.addbook,name='addbook'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^edithero/(\d+)/$', views.edithero, name='edithero'),
    url(r'^editbook/(\d+)/$', views.editbook, name='editbook'),
]