from django.contrib.auth import hashers
from rest_framework import serializers
from .models import *


class GoodSerializer2(serializers.ModelSerializer):
    # 可以在序列化时指定字段  在多方 使用source = 模型名.字段名
    # read_only = True 表示不能更改(GET显示 POST不显示)
    # write_only = True 表示只能更改(GET显示 POST不显示)
    # 不可以同时为True
    category_super = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        # fields = "__all__"
        # fields = ('name', 'desc', 'category')
        fields = ('id', 'name', 'desc', 'category', 'category_super')


class CustomSerializer(serializers.RelatedField):
    """
    自定义序列化类
    """

    def to_representation(self, value):
        return str(value.id) + '++' + value.name + "--" + value.desc


class CategorySerializer(serializers.Serializer):
    """
    序列化类决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=2, error_messages={
        "max_length": '最多10个字',
        "min_length": '最少2个字',
    }, label="分类名称", help_text="请输入分类名")

    def create(self, validated_data):
        """
        通过重写create方法。来定义模型创建方式
        :param validated_data: 参数字典
        :return: 对象实例
        """
        instance = Category.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update 来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 修改后的参数字典
        :return:修改后的实例
        """
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class CategorySerializer1(serializers.ModelSerializer):
    """
    编写针对Category模型类的序列化类 继承serializers.ModelSerializer
    该类指明了Category的序列化细节
    在Meta类中 model指明序列化模型 fields指明序列化字段
    """
    # goods 一定要和模型类定义的关联字段related_name保持一致
    # StringRelatedField()  可以显示关联模型中的__str__返回值  many=True 代表多个对象
    # goods = serializers.StringRelatedField(many=True)
    #  PrimaryKeyRelatedField() 返回主键  read_only=True代表只读
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # SlugRelatedField() 返回自定义字段值
    # goods = serializers.SlugRelatedField(slug_field='name',many=True,read_only=True)
    # HyperlinkedRelatedField() 返回主键对应的详情路由
    # goods = serializers.HyperlinkedRelatedField(view_name='good-detail',many=True,read_only=True)
    # goods = serializers.HyperlinkedIdentityField(view_name='good-detail',many=True,read_only=True)
    # 使用自定义序列化类
    goods = CustomSerializer(many=True, read_only=True)

    # 使用模型序列化类
    # goods = GoodSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        # fields指明序列化字段 __all__指明所有
        # fields = "__all__"
        fields = ('id', 'name', 'goods')


class GoodImgsSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    #
    # def validate_good(self, good):
    #     try:
    #         # Good.objects.get(name=good["name"])
    #         print('当前商品',good)
    #         Good.objects.get(name=good)
    #         good = Good.objects.get(name=good)
    #         print('转换之后',good)
    #
    #     except:
    #         raise serializers.ValidationError("输入的分类名不存在，请先联系管理员添加分类")
    #     return good

    def validate(self, attrs):
        print("收到的数据", attrs)
        try:
            # 为了拿到分类名，我们需要以下操作
            g = Good.objects.get(name=attrs["good"]["name"])
        except:
            # 如果分类不存在 创建分类
            g = Good.objects.create(name=attrs["good"]["name"])

        attrs["good"] = g
        return attrs

    def create(self, validated_data):
        instance = GoodImgs.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("-----")
        print(instance)
        print(validated_data)

        instance.name = validated_data.get("name", instance.name)
        # 取到新的category分类实例就赋值，取不到赋给原来的分类实例
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
    }, help_text="请输入商品名", label="商品名称")
    category = CategorySerializer(label="所属分类")
    imgs = GoodImgsSerializer(label="包含图片", read_only=True, many=True)

    def validate_category(self, category):
        """
        处理category 分类名不存在，停止操作
        :param category: 处理的原始值
        :return: 返回新值
        """
        try:
            Category.objects.get(name=category["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在，请先联系管理员添加分类")
        return category

    def validate(self, attrs):
        print("收到的数据", attrs)
        try:
            # 为了拿到分类名，我们需要以下操作
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            # 如果分类不存在 创建分类
            c = Category.objects.create(name=attrs["category"]["name"])

        attrs["category"] = c
        return attrs

    def create(self, validated_data):
        instance = Good.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("-----")
        print(instance)
        print(validated_data)
        # -----
        # mibook
        # {'name': 'mibook12', 'category': <Category: 笔记本电脑>}
        instance.name = validated_data.get("name", instance.name)
        # 取到新的category分类实例就赋值，取不到赋给原来的分类实例
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
        "required": "用户名不能为空"
    }, help_text="请输入用户名", label="用户名")
    password = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
        "required": "密码不能为空"

    }, help_text="请输入密码", label="密码")
    email = serializers.CharField(max_length=20, min_length=2, required=False, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于9个字",
        "required": "邮箱可以不填"

    }, help_text="请输入邮箱", label="邮箱")

    class Meta:
        model = User
        # fields = ('','','')
        # 在fields写入想要显示的字段
        fields = ('username', 'password', 'email')
        # 在exclude写入不需要显示的字段
        # exclude =['','']

    def validate(self, attrs):
        if attrs.get("password"):
            attrs["password"] = hashers.make_password(attrs["password"])
        return attrs


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
    }, help_text="请输入用户名", label="用户名")
    password = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
    }, help_text="请输入密码", label="用户名", write_only=True)
    password2 = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
    }, help_text="请重复输入密码", label="重复密码", write_only=True)

    # 校检函数 此时data = password2
    def validate_password2(self, data):
        # 此时self内存储的password。。数据还不可以使用  所以此处无法验证重复密码
        # 想使用需要用 self.initial_data['password']
        # print(data,self.data.get('password'),"++++")
        print(data, self.initial_data['password'], "++++")
        if data != self.initial_data['password']:
            raise serializers.ValidationError('密码不一致')
        else:
            print("密码一致")
            return data

    def validate(self, attrs):
        print("等待校检的数据", attrs)
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError('密码不一致')
        else:

            del attrs["password2"]
        return attrs

    def create(self, validated_data):
        print("准备注册的数据", validated_data)
        # 普通创建用户 密码不可加密
        # return User.objects.create(**validated_data)
        return User.objects.create_user(username=validated_data.get("username"),
                                        email=validated_data.get("email"),
                                        password=validated_data.get("password"))
