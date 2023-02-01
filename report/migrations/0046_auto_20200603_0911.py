# Generated by Django 3.0.5 on 2020-06-03 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0045_auto_20200603_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pnjmdmethod',
            old_name='PNjmd',
            new_name='pNjmd',
        ),
        migrations.RenameField(
            model_name='pnjmdtexts',
            old_name='PNjmd',
            new_name='pNjmd',
        ),
        migrations.AlterField(
            model_name='pnjmd',
            name='general',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='通用性参数设置'),
        ),
    ]