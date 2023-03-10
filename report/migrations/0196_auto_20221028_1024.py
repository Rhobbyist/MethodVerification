# Generated by Django 3.0.5 on 2022-10-28 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0195_auto_20220822_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validation_reason',
            name='reason',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Detectionplatform', models.CharField(blank=True, choices=[('内分泌检测平台', '内分泌检测平台'), ('遗传代谢病检测平台', '遗传代谢病检测平台'), ('微量营养素检测平台', '微量营养素检测平台'), ('治疗药物检测平台', '治疗药物检测平台'), ('研发与创新平台', '研发与创新平台')], max_length=16, verbose_name='检测平台')),
                ('Group', models.CharField(blank=True, choices=[('CAH组', 'CAH组'), ('IMD组', 'IMD组'), ('UOA组', 'UOA组'), ('VD组', 'VD组'), ('VAE组', 'VAE组'), ('IGF1组', 'IGF1组'), ('药物浓度组', '药物浓度组'), ('儿茶酚胺激素组', '儿茶酚胺激素组'), ('血儿茶酚胺组', '血儿茶酚胺组'), ('元素组', '元素组'), ('研发组', '研发组')], max_length=16, verbose_name='项目组')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '所属检测平台及项目组',
                'verbose_name_plural': '',
            },
        ),
    ]
