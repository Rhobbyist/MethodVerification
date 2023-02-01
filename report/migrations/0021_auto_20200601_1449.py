# Generated by Django 3.0.5 on 2020-06-01 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0020_parametersetting'),
    ]

    operations = [
        migrations.DeleteModel(
            name='jmdbackstage',
        ),
        migrations.RemoveField(
            model_name='ptbackstage',
            name='PTmain',
        ),
        migrations.RemoveField(
            model_name='texts',
            name='main',
        ),
        migrations.AlterField(
            model_name='parametersetting',
            name='text',
            field=models.TextField(max_length=200, verbose_name='描述性内容'),
        ),
        migrations.AlterField(
            model_name='subindex',
            name='general',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.general', verbose_name='通用性参数设置'),
        ),
        migrations.DeleteModel(
            name='main',
        ),
        migrations.DeleteModel(
            name='PTbackstage',
        ),
        migrations.DeleteModel(
            name='PTmain',
        ),
        migrations.DeleteModel(
            name='texts',
        ),
    ]
