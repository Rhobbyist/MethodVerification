# Generated by Django 3.2.8 on 2022-02-14 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0181_auto_20220214_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matrixeffect_testspecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='基质效应测试', editable=False, max_length=32, verbose_name='验证指标')),
                ('special', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.special', verbose_name='特殊参数设置')),
            ],
            options={
                'verbose_name': '基质效应测试',
                'verbose_name_plural': '基质效应测试',
            },
        ),
        migrations.CreateModel(
            name='Matrixeffect_testspecialtexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='描述性内容')),
                ('matrixeffect_testspecial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.matrixeffect_testspecial', verbose_name='基质效应测试')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.CreateModel(
            name='Matrixeffect_testspecialmethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bias', models.FloatField(blank=True, verbose_name='最大允许偏差(%)')),
                ('matrixeffect_testspecial', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.matrixeffect_testspecial', verbose_name='基质效应测试')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
    ]