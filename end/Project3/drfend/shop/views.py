from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from .models import *
from .serializers import *
from . import permissions as mypermissions


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

    # 用户未登录 不显示分类列表 优先级高于全局配置
    # permission_classes = [permissions.IsAdminUser]

    # 超级管理员才能创建分类 普通用户只能查看
    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or \
                self.action == "destory":
            return [permissions.IsAdminUser()]  # 必须是超级管理员
            # return [permissions.IsAuthenticatedOrReadOnly()]  # 未登录只读，登陆后可修改
            # return [mypermissions.CategoryPermission()]  # 使用自定义权限类
        else:
            return [permissions.IsAuthenticated()]


class GoodViewsSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()

    serializer_class = GoodSerializer


class GoodImgsViewsSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer


# class UserViewsSets(viewsets.ModelViewSet):
class UserViewsSets1(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    """
    声明用户操作 获取 更新 删除
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 添加自定义注册路由
    @action(methods=['POST'], detail=False)
    def register(self, request):
        seria = UserRegisterSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        # return Response("创建成功")
        return Response(seria.data, status=status.HTTP_201_CREATED)


class UserViewsSets(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
    声明用户操作 获取 更新 删除
    此处更新的用户密码是没有加密的
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        print("", self.action)
        if self.action == "create":
            return UserRegisterSerializer
        return UserSerializer


class OrderViewsSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [permissions.OrdersPermission]

    def get_permissions(self):
        print("当前http方法为", self.action)
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or \
                self.action == 'retrieve' or self.action == "destroy":
            return [mypermissions.OrdersPermission()]
        else:
            return [permissions.IsAdminUser()]


