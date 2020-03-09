from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# 地址坐标
class Location(models.Model):
    lng = models.FloatField(verbose_name="经度")
    lat = models.FloatField(verbose_name="维度")


# 城市
class City(models.Model):
    name = models.CharField(max_length=6, verbose_name="城市")
    coordinate = models.OneToOneField(Location, on_delete=models.CASCADE, verbose_name='坐标', related_name='location')


class shop(models.Model):
    name = models.CharField(max_length=20, verbose_name="门店名称")
    address = models.CharField(max_length=20, verbose_name="门店地址")
    phone = models.CharField(max_length=20, verbose_name="座机电话")
    site_phone = models.CharField(max_length=20, verbose_name="移动电话")
    from_time = models.TimeField(verbose_name="上班时间")
    to_time = models.TimeField(verbose_name="下班时间")
    city = models.ForeignKey(City, models.CASCADE, verbose_name="所在城市", related_name="city")


# 类型 MVP SUV ..
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name


#  价格
class Prices(models.Model):
    hour = models.PositiveIntegerField(verbose_name="元/小时")
    day = models.PositiveIntegerField(verbose_name="元/天")
    week = models.PositiveIntegerField(verbose_name="元/周")
    month = models.PositiveIntegerField(verbose_name="元/月")
    avg = models.PositiveIntegerField(verbose_name="元/日均")
    minimum = models.PositiveIntegerField(verbose_name="最短起租时间")


# 车辆
class Car(models.Model):
    name = models.CharField(max_length=20, verbose_name="汽车名称")
    group_id = models.CharField(max_length=10, verbose_name="汽车车牌")
    displacement = models.CharField(max_length=10, verbose_name="排放量")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类", related_name='cars')
    transmission_name = models.CharField(max_length=10, verbose_name="驾驶方式")
    price = models.ManyToManyField(Prices, verbose_name="价格")


# 车辆图片
class Carimgs(models.Model):
    img = models.ImageField(upload_to="carimgs")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='所属车辆', related_name="imgs")


# 用户类
class User(AbstractUser):
    tel = models.CharField(max_length=11, verbose_name="手机号")


# 订单类
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="用户")
    cars = models.ManyToManyField(Car, related_name="所租车辆")

    def __str__(self):
        return self.user.username + "的订单"
