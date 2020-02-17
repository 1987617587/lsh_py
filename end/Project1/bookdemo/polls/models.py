from django.db import models

# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=30)
    source = models.CharField(max_length=10,default="凭空捏造")
    # create_date = models.DateTimeField(auto_now_add=True,related_name='创建时间')
    # def __str__(self):
    #     return self.title
    # class Mate:
    #     order_ing = ["create_date"]
    #
    option1_votes = models.IntegerField(default=0,verbose_name="选项1票数")
    option2_votes = models.IntegerField(default=0,verbose_name="选项2票数")
    option3_votes = models.IntegerField(null=True, blank=True,verbose_name="选项3票数")
    option4_votes = models.IntegerField(null=True, blank=True,verbose_name="选项4票数")
    # answer = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Option(models.Model):
    option1 = models.CharField(max_length=10,default="支持", unique=True)
    option2 = models.CharField(max_length=10, default="反对", unique=True)
    option3 = models.CharField(max_length=10, null=True, blank=True,unique=True)
    option4 = models.CharField(max_length=10, null=True, blank=True,unique=True)
    option2 = models.IntegerField(max_length=10,default=0,verbose_name="反对")

    # option= models.CharField(max_length=10,verbose_name="选项")
    # votenums = models.PositiveIntegerField(verbose_name="票数")
    # create_date = models.DateTimeField(auto_now_add=True,related_name='创建时间')
    problem = models.ForeignKey('Problem',on_delete=models.CASCADE,related_name="problems")

    def __str__(self):
        return self.option1,self.option2