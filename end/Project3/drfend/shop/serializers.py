from rest_framework import serializers
from .models import *


class GoodSerializer(serializers.ModelSerializer):
    # 可以在序列化时指定字段  在多方 使用source = 模型名.字段名  read_only = True 表示不能更改
    # category_super = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('name', 'desc', 'category')
        # fields = ('name', 'desc', 'category_super')


class CustomSerializer(serializers.RelatedField):
    """
    自定义序列化类
    """

    def to_representation(self, value):
        return str(value.id) + '++' + value.name + "--" + value.desc


class CategorySerializer(serializers.ModelSerializer):
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
        fields = ('name', 'goods')
