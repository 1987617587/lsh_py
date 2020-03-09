# 实现自定义认证类（登录内容是什么）
from django.contrib.auth import backends
from django.db.models import Q

from .models import User


class MyLoginBackend(backends.BaseBackend):
    def authenticate(self, request, **kwargs):
        """

        :param request:
        :param kwargs:认证参数
        :return: 如果认证成功返回认证，失败返回None
        """
        print(kwargs)
        username = kwargs['username']
        password = kwargs['password']
        # user = User.objects.filter(username=username).first()
        # if not user:
        #     user = User.objects.filter(email=username).first()
        #     if not user:
        #         user = User.objects.filter(tel=username).first()
        # 可以使用Q
        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(tel=username)).first()
        if user:
            b = user.check_password(password)
            if b:
                return user
            return None
        return None
