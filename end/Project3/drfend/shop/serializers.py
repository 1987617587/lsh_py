from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    """
    编写针对Category模型类的序列化类 继承serializers.ModelSerializer
    该类指明了Category的序列化细节
    在Meta类中 model指明序列化模型 fields指明序列化字段
    """

    class Meta:
        model = Category
        fields = "__all__"


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"
