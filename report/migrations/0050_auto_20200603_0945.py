# Generated by Django 3.0.5 on 2020-06-03 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0049_auto_20200603_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pnjmd',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='通用性参数设置'),
        ),
    ]