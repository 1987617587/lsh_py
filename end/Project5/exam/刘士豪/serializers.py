from .models import *
from rest_framework import serializers


class DepartmentSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
    }, help_text="请输入部门名称", label="部门名称")

    def create(self, validated_data):
        instance = Department.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class WorkersSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最长不能超过20个字",
        "min_length": "最短不能小于2个字",
    }, help_text="请输入员工姓名", label="员工姓名")
    wages = serializers.IntegerField(label='本月工资')
    department = DepartmentSerializers(label="所属部门")

    def validate_department(self, department):

        print(department)
        try:

            Department.objects.get(name=department["name"])
        except:
            raise serializers.ValidationError("输入的部门不存在")
        return department

    def validate(self, attrs):
        print("收到的数据", attrs)
        try:
            # 为了拿到分类名，我们需要以下操作
            d = Department.objects.get(name=attrs["department"]["name"])
        except:
            # 如果分类不存在 创建分类
            d = Department.objects.create(name=attrs["department"]["name"])

        attrs["department"] = d
        return attrs

    def create(self, validated_data):
        instance = Workers.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("-----")
        print(instance)
        print(validated_data)
        instance.name = validated_data.get("name", instance.name)
        # 取到新的department实例就赋值，取不到赋给原来的分类实例
        instance.department = validated_data.get("department", instance.department)
        instance.save()
        return instance
