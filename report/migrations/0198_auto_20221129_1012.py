# Generated by Django 3.0.5 on 2022-11-29 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0197_auto_20221028_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Detectionplatform',
            field=models.CharField(blank=True, choices=[('内分泌检测平台', '内分泌检测平台'), ('遗传代谢病检测平台', '遗传代谢病检测平台'), ('微量营养素检测平台', '微量营养素检测平台'), ('治疗药物检测平台', '治疗药物检测平台'), ('研发与创新平台', '研发与创新平台'), ('内分泌检测平台&研发与创新平台', '内分泌检测平台&研发与创新平台'), ('临床服务一部', '临床服务一部'), ('临床服务二部', '临床服务二部'), ('中心负责人 ', '中心负责人 ')], max_length=16, verbose_name='检测平台'),
        ),
        migrations.CreateModel(
            name='ReportLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('operation', models.CharField(max_length=32)),
                ('operator', models.CharField(max_length=32)),
                ('time', models.CharField(max_length=32)),
                ('reportinfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo')),
            ],
        ),
        migrations.CreateModel(
            name='ReportFlowChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('operation', models.CharField(max_length=32)),
                ('operator', models.CharField(max_length=32)),
                ('time', models.CharField(max_length=32)),
                ('receiver', models.CharField(max_length=32)),
                ('reportinfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo')),
            ],
        ),
    ]
