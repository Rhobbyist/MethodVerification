# Generated by Django 3.0.5 on 2020-06-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0034_auto_20200602_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseparameterpnjmd',
            name='PNjmdbackstage',
        ),
        migrations.RemoveField(
            model_name='pjjmdbackstage',
            name='jmdbackstage',
        ),
        migrations.RemoveField(
            model_name='pnjmdbackstage',
            name='jmdbackstage',
        ),
        migrations.RemoveField(
            model_name='textpjjmd',
            name='PJjmdbackstage',
        ),
        migrations.RemoveField(
            model_name='textpnjmd',
            name='PNjmdbackstage',
        ),
        migrations.RemoveField(
            model_name='jmdbackstage',
            name='index',
        ),
        migrations.AddField(
            model_name='jmdbackstage',
            name='baseparameter',
            field=models.CharField(default='', max_length=32, verbose_name='基本参数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jmdbackstage',
            name='text',
            field=models.TextField(default='', max_length=200, verbose_name='描述性内容'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='baseparameterPJjmd',
        ),
        migrations.DeleteModel(
            name='baseparameterPNjmd',
        ),
        migrations.DeleteModel(
            name='PJjmdbackstage',
        ),
        migrations.DeleteModel(
            name='PNjmdbackstage',
        ),
        migrations.DeleteModel(
            name='textPJjmd',
        ),
        migrations.DeleteModel(
            name='textPNjmd',
        ),
    ]