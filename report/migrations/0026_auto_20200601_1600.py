# Generated by Django 3.0.5 on 2020-06-01 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0025_auto_20200601_1558'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='textjmd',
            new_name='textPJjmd',
        ),
        migrations.CreateModel(
            name='textPNjmd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='描述性内容')),
                ('PNjmdbackstage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.PNjmdbackstage')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
    ]