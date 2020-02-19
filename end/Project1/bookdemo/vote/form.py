from django import forms
from .models import User

class LoginForm(forms.Form):
    """
    定义一个登录表单用于生成html表单
    """
    username = forms.CharField(max_length=6, label="输入用户名",
                               min_length=1, help_text="最短6位，最长20位")
    password = forms.CharField(min_length=1, max_length=6,
                               widget=forms.PasswordInput, label="输入密码",
                               help_text="最短6位，最长20位")


class RegistForm(forms.ModelForm):
    """
        定义一个登录表单用于生成html表单
    """
    repassword = forms.CharField(min_length=1, max_length=150,
                               widget=forms.PasswordInput, label="重复密码",
                               help_text="最短6位，最长20位")
    class Meta:
        model = User
        fields = ["username","password"]
        labels = {
            "username":"用户名",
            "password":"密  码"
        }

        help_texts = {
            "username":"最短6位，最长20位",
            "password":"最短6位，最长20位",
        }
        widgets = {
            "password":forms.PasswordInput
        }


