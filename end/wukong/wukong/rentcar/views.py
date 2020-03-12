from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import permissions as mypermissions

from .models import *
from rest_framework import viewsets, mixins, permissions, status, filters
from .serializers import *


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    # 局部过滤配置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name']
    # 局部搜索配置
    search_fields = ["name"]
    # 局部排序配置
    ordering_fields = ["id"]




class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers
    # 局部过滤配置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name']
    # 局部搜索配置
    search_fields = ["name"]
    # 局部排序配置
    ordering_fields = ["id"]


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers
    # 局部过滤配置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name']
    # 局部搜索配置
    search_fields = ["name"]
    # 局部排序配置
    ordering_fields = ["id"]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    # 局部过滤配置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name']
    # 局部搜索配置
    search_fields = ["name"]
    # 局部排序配置
    ordering_fields = ["id"]


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


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # 局部过滤配置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name']
    # 局部搜索配置
    search_fields = ["name"]
    # 局部排序配置s
    ordering_fields = ["-id"]



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

    # 添加指定路由
    # @action(methods=['GET'], detail=False)
    # def get_category(self, request):
    #     # seria = CategorySerializer(instance=Category.objects.all()[:3],many=True)
    #     # 指定查询数量
    #     seria = CategorySerializer(instance=Category.objects.all()[:int(request.query_params.get("num"))], many=True)
    #
    #     return Response(data=seria.data, status=status.HTTP_200_OK)

    # @action(methods=['GET'], detail=False)
    # def get_ordersbyuser(self, request):
    # seria = CategorySerializer(instance=Category.objects.all()[:3],many=True)
    # 指定指定用户的订单
    # seria = OrderSerializer(
    #     instance=Order.objects.filter(user=request)[0].cars.all(), many=True)
    # print(seria)
    # return Response(data=seria.data, status=status.HTTP_200_OK)

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


@api_view(['GET'])
def getuserorders(request):
    print("hello")
    print(request)
    print(request.headers["Authorization"])
    user = JWTAuthentication().authenticate(request)
    print("用户", user[0])
    # seria = OrderSerializer(instance=user[0])
    seria = OrderSerializer(instance=Order.objects.filter(user=user[0]), many=True)
    # seria.is_valid(raise_exception=True)
    print(seria.data)
    # seria2 = CarSerializers(instance=Car.objects.filter(id=Order.objects.filter(user=user[0]).get("cars")[0]), many=True)
    # print(seria2.data)
    return Response(seria.data, status=status.HTTP_200_OK)


# 用户订单总金额
@api_view(['GET'])
def getuserordersmoney(request):
    print("hello")
    print(request)
    print(request.headers["Authorization"])
    user = JWTAuthentication().authenticate(request)[0]
    print("用户", user,type(user))
    # car = CarSerializers(instance=Car.objects.filter(id=Order.objects.filter(user=user).get("cars")[0]), many=True)
    print(Order.objects.filter(user=user))
    orders = Order.objects.filter(user=user)
    price = 0
    for order in orders:
        # 订单对应车辆的价格
        print(order.cars.all()[0].price.day)
        # 订单对应车辆的时间
        print(order.days)
        price += order.cars.all()[0].price.day*order.days
    print(price)

    return Response(price, status=status.HTTP_200_OK)