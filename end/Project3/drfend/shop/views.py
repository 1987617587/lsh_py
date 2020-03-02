from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承viewsets.ModelViewSet 之后用于GET POST PATCH DELETE等HTTP动词操作
    serializer_class 指明序列化类
    """

    queryset = Category.objects.all()

    # 添加指定路由
    @action(methods=['GET'], detail=False)
    def get_category(self, request):
        # seria = CategorySerializer(instance=Category.objects.all()[:3],many=True)
        # 指定查询数量
        seria = CategorySerializer(instance=Category.objects.all()[:int(request.query_params.get("num"))], many=True)

        return Response(data=seria.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def get_goodsbycategory(self, request):
        # seria = CategorySerializer(instance=Category.objects.all()[:3],many=True)
        # 指定指定分类的商品
        seria = CategorySerializer(
            instance=Category.objects.filter(name=request.query_params.get("name"))[0].goods.all(), many=True)
        return Response(data=seria.data, status=status.HTTP_200_OK)

    # 1.通过属性指明
    # serializer_class = CategorySerializer
    # 2.通过方法指明
    def get_serializer_class(self):
        return CategorySerializer


class GoodViewsSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()

    serializer_class = GoodSerializer


class GoodImgsViewsSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer
