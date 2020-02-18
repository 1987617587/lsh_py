# Generated by Django 3.0.3 on 2020-02-16 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('source', models.CharField(default='凭空捏造', max_length=10)),
                ('option1_votes', models.IntegerField(default=0, verbose_name='选项1票数')),
                ('option2_votes', models.IntegerField(default=0, verbose_name='选项2票数')),
                ('option3_votes', models.IntegerField(blank=True, null=True, verbose_name='选项3票数')),
                ('option4_votes', models.IntegerField(blank=True, null=True, verbose_name='选项4票数')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.CharField(default='支持', max_length=10, unique=True)),
                ('option2', models.CharField(default='反对', max_length=10, unique=True)),
                ('option3', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('option4', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='polls.Problem')),
            ],
        ),
    ]