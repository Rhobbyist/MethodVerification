# Generated by Django 3.2.8 on 2022-03-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0191_instrumentcompare'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportinfo',
            name='verifyoccasion',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]