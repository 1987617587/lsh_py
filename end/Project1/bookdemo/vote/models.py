from django.db import models
# 使用django自带的用户类
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    用户类继承原有类

    """

    telephone = models.CharField(max_length=11,verbose_name="手机号")
    # 一个问题可以被多个用户投票  关系字段写在多方
    problems = models.ForeignKey('Problem',on_delete=models.CASCADE)

class Problem(models.Model):
    title = models.CharField(max_length=30)
    source = models.CharField(max_length=10, default="凭空捏造")
    # create_date = models.DateTimeField(auto_now_add=True,related_name='创建时间')
    def __str__(self):
        return self.title

    class Mate:
        verbose_name = "投票表"
        verbose_name_plural = verbose_name
        # order_ing = ["create_date"]


class Option(models.Model):
    option = models.CharField(max_length=10, verbose_name="选项")
    votenums = models.PositiveIntegerField(verbose_name="票数", default=0)
    # create_date = models.DateTimeField(auto_now_add=True,related_name='创建时间')
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name="problems", verbose_name="所属问题")

    def __str__(self):
        return self.option

    class Mate:
        verbose_name = "选项表"
        verbose_name_plural = verbose_name

        # order_ing = ["create_date"]
