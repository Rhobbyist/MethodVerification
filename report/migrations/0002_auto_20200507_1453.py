# Generated by Django 3.0.5 on 2020-05-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('project', models.CharField(max_length=32)),
                ('verifytime', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
