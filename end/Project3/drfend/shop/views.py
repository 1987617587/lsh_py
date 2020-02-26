import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# django本身自带的序列化
from django.core import serializers
from .models import *


# Create your views here.
def index(request):
    # return HttpResponse("首页")

    category = Category.objects.all()
    # 如果使用django模板就是前后的不分离
    # return JsonResponse(locals())
    # 如果已json或者xml返回的数据，可以实现前后的分离开发
    # 以下返回的数据 需要序列化处理
    # return JsonResponse({"category": category})
    # return JsonResponse( category,safe=False)
    # result = {"name":"zzy"}
    # 使用django 自带的序列化
    result = serializers.serialize('json',category)
    return JsonResponse(result,safe=False)