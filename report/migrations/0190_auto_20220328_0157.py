# Generated by Django 3.2.8 on 2022-03-28 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0189_auto_20220325_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='pt',
            name='accept1',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pt',
            name='accept2',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pt',
            name='templates',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
