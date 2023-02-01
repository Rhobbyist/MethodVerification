# Generated by Django 3.0.5 on 2022-07-19 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0192_reportinfo_verifyoccasion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReagentsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Col1', models.CharField(blank=True, max_length=200, verbose_name='第1列')),
                ('Col2', models.CharField(blank=True, max_length=200, verbose_name='第2列')),
                ('Col3', models.CharField(blank=True, max_length=200, verbose_name='第3列')),
                ('Col4', models.CharField(blank=True, max_length=200, verbose_name='第4列')),
                ('Col5', models.CharField(blank=True, max_length=200, verbose_name='第5列')),
                ('Col6', models.CharField(blank=True, max_length=200, verbose_name='第6列')),
                ('Col7', models.CharField(blank=True, max_length=200, verbose_name='第7列')),
                ('Col8', models.CharField(blank=True, max_length=200, verbose_name='第8列')),
                ('reagents_Consumables', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Reagents_Consumables', verbose_name='主要试剂')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '主要试剂表格（依据实际情况选择是否填写）',
            },
        ),
    ]