from django.db import models

# Create your models here.
class Book(models.Model):
    """
    book继承了Model类  应为Model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")

    def __str__(self):
        return self.title

class Hero(models.Model):
    """
    hero继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=( ('male','男'),('female','女') ), default='male')
    content = models.CharField(max_length=100)
    # book  是一对多中的外键 on_delete代表删除主表数据时如何做
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.name