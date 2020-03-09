from django.shortcuts import render
from .models import *
from rest_framework import viewsets, mixins
from .serializers import *


# Create your views here.
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class CarImagesViewSet(viewsets.ModelViewSet):
    queryset = Carimgs.objects.all()
    serializer_class = CarImagesSerializers


class UserViewsSets(viewsets.GenericViewSet,mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
    声明用户操作 获取 更新 删除
    此处更新的用户密码是没有加密的
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrderViewsSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
