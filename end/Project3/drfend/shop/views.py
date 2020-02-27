from rest_framework import viewsets
from .models import *
from .serializers import *


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承viewsets.ModelViewSet 之后用于GET POST PATCH DELETE等HTTP动词操作
    serializer_class 指明序列化类
    """

    queryset = Category.objects.all()

    # 1.通过属性指明
    # serializer_class = CategorySerializer
    # 2.通过方法指明
    def get_serializer_class(self):
        return CategorySerializer


class GoodViewsSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
