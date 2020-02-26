from django.conf.urls import url
from . import views

appname = "shop"
urlpatterns = [
    url('', views.index, name="index"),
]
