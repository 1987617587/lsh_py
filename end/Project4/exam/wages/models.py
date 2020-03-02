from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=10, verbose_name="部门名称")

    def __str__(self):
        return self.name


class Workers(models.Model):
    name = models.CharField(max_length=20, verbose_name="员工名")
    wages = models.PositiveIntegerField(max_length=10, verbose_name='本月工资')
    # job_number = models.PositiveIntegerField(max_length=10, verbose_name='工号')
    department = models.ForeignKey(Department, on_delete=models.CASCADE,verbose_name="所属部门")

    def __str__(self):
        return self.name
