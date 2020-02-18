from django.conf.urls import url

from . import views

app_name = "vote"
urlpatterns = [
    # 一、视图函数FBV
    # url(r'^$', views.index, name='index'),
    # url(r'^detail/(\d+)/$', views.detail, name='detail'),
    # url(r'^result/(\d+)/$', views.result, name='result'),
    # 二、视图类CBV
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^loginout/$', views.loginout, name='loginout'),
    # url(r'^detail/(\d+)/$', views.DetailView.as_view(), name='detail'),
    #
    # url(r'^result/(\d+)/$', views.Result.as_view(), name='result'),

    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^result/(\d+)/$', views.result, name='result'),
    url(r'^look/$', views.IndexView.as_view(), name='look'),
]
