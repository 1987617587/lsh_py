from django.contrib.auth import hashers

from .models import *
from rest_framework import serializers


class CitySerializers(serializers.ModelSerializer):
    class Meta():
        model = City
        # fields = ["title","pub_time","url"]
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta():
        model = Category
        # fields = ["title","pub_time","url"]
        fields = '__all__'


class ShopSerializers(serializers.ModelSerializer):
    class Meta():
        model = Shop
        # fields = ["title","pub_time","url"]
        fields = '__all__'


class PriceSerializers(serializers.ModelSerializer):
    class Meta():
        model = Prices
        # fields = ["title","pub_time","url"]
        fields = '__all__'


class CarImagesSerializers(serializers.ModelSerializer):
    class Meta():
        model = Carimgs
        fields = '__all__'


class CarSerializers(serializers.ModelSerializer):
    imgs = CarImagesSerializers(many=True, read_only=True, )

    class Meta():
        model = Car
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
        "required": "密码不能为空"

    }, help_text="请输入密码", label="密码")

    class Meta:
        model = User
        # fields = ('','','')
        # fields = ('username', 'password', 'email')
        exclude = ["user_permissions", "groups"]

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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = ('','','')
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ('','','')
        fields = "__all__"