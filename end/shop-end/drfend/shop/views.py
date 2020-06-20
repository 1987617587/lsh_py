from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse

# 通过api_view装饰器可以将基于函数的视图转换成APIView基于类的视图
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from rest_framework import permissions
from . import permissions as mypermissions

from rest_framework import throttling
from .throttling import MyAnon,MyUser

from .pagination import MyPagination

# 引入django过滤类
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CategoryListView2(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class CategoryDetailView2(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def patch(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.delete(request,pk)

class CategoryListView1(APIView):
    """
    1继承Django自带的View类需要重写对应的http方法
    2继承DRF自带的APIView类即可完成请求响应的封装  APIView继承封装了Django的View
    """
    def get(self,request):
        # instance从数据库取
        seria = CategorySerizlizer(instance=Category.objects.all(),many=True)
        return Response(seria.data,status=status.HTTP_200_OK)

    def post(self,request):
        # data从请求中取
        seria = CategorySerizlizer(data=request.data)
        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data,status=status.HTTP_201_CREATED)
        # else:
        #     return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)

        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data,status=status.HTTP_201_CREATED)

class CategoryDetailView1(APIView):
    def get(self,request,cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category,pk=cid))
        return Response(seria.data,status=status.HTTP_200_OK)
    def put(self,request,cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category,pk=cid),data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_200_OK)
        else:
            return Response(seria.errors,status=status.HTTP_200_OK)
    def patch(self,request,cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_200_OK)
    def delete(self,request,cid):
        get_object_or_404(Category,pk=cid).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def categoryList(request):
    if request.method == "GET":
        # instance 为需要序列化的对象 来源于数据库
        seria = CategorySerizlizer(instance=Category.objects.all(),many=True)
        return Response(seria.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        # data  为序列化对象  来源于请求中提取的数据
        seria = CategorySerizlizer(data=request.data)
        # 从请求中提取的数据序列化之前需要进行校验
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def categoryDetail(request,cid):
    model = get_object_or_404(Category,pk=cid)
    if request.method == "GET":
        seria = CategorySerizlizer(instance=model)
        return Response(seria.data,status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        #  更新就是从请求中提取参数 替换掉数据库中取出的数据
        seria = CategorySerizlizer(instance=model,data=request.data)
        # 验证是否合法
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_200_OK)
        else:
            return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse("当前路由不允许"+request.method+"操作")

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer


class CategoryViewSets2(viewsets.ModelViewSet):
    """
    如果返回的内容就是模型列表 用queryset方便
    如果需要处理  可以使用base_name 结合get_queryset
    """

    queryset = Category.objects.all()

    # def get_queryset(self):
    #     return Category.objects.all()[:3]


    # serializer_class = CategorySerizlizer
    def get_serializer_class(self):
        return CategorySerizlizer

    @action(methods=['GET'],detail=False)
    def getlatestcategory(self,request):
        seria = CategorySerizlizer(instance=Category.objects.all()[:3],many=True)
        return Response(data=seria.data,status=status.HTTP_200_OK)



class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET POST PUT PATCH DELETE等HTTP动词操作
    queryset 指明 需要操作的模型列表
    serializer_class 指明序列化类
    """
    queryset = Category.objects.all()
    # 1通过属性指明
    serializer_class = CategorySerizlizer
    # 2通过方法指明
    # def get_serializer_class(self):
    #     return CategorySerizlizer

    # 用户未登录不显示 分类列表  优先级别高于全局配置
    # permission_classes = [permissions.IsAdminUser]

    # 授权的前提是认证  登录过（认证过）之后可以进行权限判断


    # 超级管理员可以创建分类  普通用户可以查看分类
    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []

    throttle_classes = [MyAnon,MyUser]

    pagination_class = MyPagination



    # 局部过滤配置
    filter_backends = [DjangoFilterBackend,  filters.SearchFilter ,filters.OrderingFilter]

    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["id"]



class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

    filterset_fields = ["name"]


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer

class UserViewSets1(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    """
    声明用户资源类 用户操作： 获取个人信息  更新个人信息   删除账户
    扩展出action路由   用户操作：  创建账户
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 使用action扩展资源的http方法
    @action(methods=["POST"],detail=False)
    def regist(self,request):
        seria = UserRegistSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data,status=status.HTTP_201_CREATED)

class UserViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    """
    声明用户资源类 用户操作： 获取个人信息  更新个人信息   删除账户
    扩展出action路由   用户操作：  创建账户
    """
    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        print("action代表http方法",self.action)
        if self.action == "create":
            return UserRegistSerializer
        return UserSerializer

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    # permission_classes = [permissions.OrdersPermission]

    def get_permissions(self):
        """
        超级管理员只可以展示所有订单
        普通用户 可以创建修改订单 不可以操作其他用户的订单
        :return:
        """
        print("http方法为",self.action)
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            return [mypermissions.OrdersPermission()]
        else:
            return [permissions.IsAdminUser()]


# http方法                          混合类关键字                   action关键字
# GET列表                           List                          get
# POST创建对象                       Create                       create
# GET 单个对象                       Retrieve                     retrieve
# PUT 修改对象提供全属性              Update                       update
# PATCH 修改对象提供部分属性          Update                       partial_update
# DELETE 删除对象                    Destroy                      destroy









