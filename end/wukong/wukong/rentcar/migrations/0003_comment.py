# Generated by Django 3.0.4 on 2020-03-12 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar', '0002_auto_20200309_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='评论人昵称')),
                ('url', models.URLField(default='http://www.zzy.com', verbose_name='个人主页')),
                ('email', models.EmailField(default='1862655@qq.com', max_length=254, verbose_name='个人邮箱')),
                ('body', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
        ),
    ]
