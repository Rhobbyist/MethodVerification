# Generated by Django 3.0.5 on 2022-12-01 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0200_reportflowchart_reportlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportlog',
            name='number',
        ),
    ]