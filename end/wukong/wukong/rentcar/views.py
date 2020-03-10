from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import permissions as mypermissions

from .models import *
from rest_framework import viewsets, mixins, permissions, status
from .serializers import *


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class PricesViewSet(viewsets.ModelViewSet):
    """
    添加权限管理 未登录 不准看价格
    """
    queryset = Prices.objects.all()
    serializer_class = PriceSerializers

    def get_permissions(self):
        print("当前http方法为", self.action)
        # 登录可看
        return [permissions.IsAuthenticated()]


class CarImagesViewSet(viewsets.ModelViewSet):
    queryset = Carimgs.objects.all()
    serializer_class = CarImagesSerializers


class UserViewsSets(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
    声明用户操作 获取 更新 删除
    此处更新的用户密码是没有加密的
    """
    queryset = User.objects.all()

    # serializer_class = UserSerializer
    def get_serializer_class(self):
        print("", self.action)
        if self.action == "create":
            return UserRegisterSerializer
        return UserSerializer


class OrderViewsSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        print("当前http方法为", self.action)
        if self.action == "create" or self.action == "list":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or \
                self.action == 'retrieve' or self.action == "destroy":
            return [mypermissions.OrdersPermission()]
        else:
            return [permissions.IsAdminUser()]


@api_view(['GET'])
def getuserinfo(request):
    print("hello")
    print(request)
    print(request.headers["Authorization"])
    user = JWTAuthentication().authenticate(request)
    print("用户", user[0])
    seria = UserSerializer(instance=user[0])
    # seria.is_valid(raise_exception=True)
    # print(seria.data)
    return Response(seria.data, status=status.HTTP_200_OK)
