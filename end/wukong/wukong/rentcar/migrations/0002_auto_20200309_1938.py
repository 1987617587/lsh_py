# Generated by Django 3.0.4 on 2020-03-09 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='days',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='city',
            name='coordinate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='rentcar.Location', verbose_name='坐标'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='rentcar.City', verbose_name='所在城市'),
        ),
    ]
