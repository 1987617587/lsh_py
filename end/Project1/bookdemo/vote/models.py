from django.db import models

# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=30)
    source = models.CharField(max_length=10,default="凭空捏造")
    # create_date = models.DateTimeField(auto_now_add=True,related_name='创建时间')
    def __str__(self):
        return self.title
    class Mate:
        verbose_name = "投票表"
        verbose_name_plural = verbose_name
        # order_ing = ["create_date"]




class Option(models.Model):


    option= models.CharField(max_length=10,verbose_name="选项")
    votenums = models.PositiveIntegerField(verbose_name="票数",default=0)
    # create_date = models.DateTimeField(auto_now_add=True,related_name='创建时间')
    problem = models.ForeignKey('Problem',on_delete=models.CASCADE,related_name="problems",verbose_name="所属问题")

    def __str__(self):
        return self.option

    class Mate:
        verbose_name = "选项表"
        verbose_name_plural = verbose_name

        # order_ing = ["create_date"]