# Generated by Django 3.2.8 on 2022-03-21 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0184_prepared_sample_stability_special_prepared_sample_stability_special_method_prepared_sample_stability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yx_method',
            name='Mobile_phaseA',
            field=models.CharField(blank=True, max_length=200, verbose_name='流动相A(水相)'),
        ),
        migrations.AlterField(
            model_name='yx_method',
            name='Mobile_phaseB',
            field=models.CharField(blank=True, max_length=200, verbose_name='流动相B(有机相)'),
        ),
        migrations.DeleteModel(
            name='endconclusion',
        ),
    ]
