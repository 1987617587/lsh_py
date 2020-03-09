from .models import *
from rest_framework import serializers


class ShopSerializers(serializers.ModelSerializer):
    class Meta():
        model = Shop
        # fields = ["title","pub_time","url"]
        fields = '__all__'


class CarImagesSerializers(serializers.ModelSerializer):
    class Meta():
        model = Carimgs
        fields = '__all__'


class CarSerializers(serializers.ModelSerializer):
    imgs = CarImagesSerializers(many=True, read_only=True)

    class Meta():
        model = Car
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('','','')
        fields = ('username', 'password', 'email')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = ('','','')
        fields = "__all__"
