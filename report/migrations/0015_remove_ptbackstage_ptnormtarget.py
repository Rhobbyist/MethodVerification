# Generated by Django 3.0.5 on 2020-05-27 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0014_ptbackstage_ptnormtarget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ptbackstage',
            name='PTnormtarget',
        ),
    ]