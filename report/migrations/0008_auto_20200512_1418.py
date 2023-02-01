# Generated by Django 3.0.5 on 2020-05-12 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_pnjmd_norm'),
    ]

    operations = [
        migrations.CreateModel(
            name='jmd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Experimentnum', models.CharField(max_length=32)),
                ('norm', models.CharField(max_length=32)),
                ('namejmd', models.CharField(max_length=32)),
                ('low', models.FloatField()),
                ('median', models.FloatField()),
                ('high', models.FloatField()),
                ('reportinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.reportInfo')),
            ],
        ),
        migrations.DeleteModel(
            name='PNjmd',
        ),
    ]
