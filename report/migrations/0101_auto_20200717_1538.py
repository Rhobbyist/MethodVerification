# Generated by Django 3.0.5 on 2020-07-17 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0100_auto_20200717_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Agilent_LC_MS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='项目名称')),
                ('agilent_LC_MS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Agilent_LC_MS', verbose_name='Agilent')),
            ],
            options={
                'verbose_name': '项目名称',
                'verbose_name_plural': '项目名称',
            },
        ),
        migrations.AlterField(
            model_name='amr',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='amrgeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.AlterField(
            model_name='amrpicture',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='carryover',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='carryovergeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.AlterField(
            model_name='crr',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='crrgeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.AlterField(
            model_name='interprecisiongeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.AlterField(
            model_name='jmd',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='matrixeffect',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='matrixeffectgeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.AlterField(
            model_name='ms',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='msgeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.AlterField(
            model_name='pt',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='ptgeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.AlterField(
            model_name='recycle',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='recyclegeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.AlterField(
            model_name='repeatprecisiongeneral',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='方法学报告性能验证指标'),
        ),
        migrations.CreateModel(
            name='ZP_Project_Agilent_LC_MS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('norm', models.CharField(blank=True, max_length=32, verbose_name='待测物')),
                ('precursor_ion', models.CharField(blank=True, max_length=32, verbose_name='母离子')),
                ('product_ion', models.CharField(blank=True, max_length=32, verbose_name='子离子')),
                ('Collision_Energy', models.CharField(blank=True, max_length=32, verbose_name='Collision_Energy')),
                ('Collision_Cell_Exit_Potential', models.CharField(blank=True, max_length=32, verbose_name='Collision_Cell_Exit_Potential')),
                ('project_Agilent_LC_MS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Project_Agilent_LC_MS', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '质谱方法',
                'verbose_name_plural': '质谱方法',
            },
        ),
        migrations.CreateModel(
            name='YX_Project_Agilent_LC_MS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=32, verbose_name='时间')),
                ('Organic_comparison', models.CharField(blank=True, max_length=32, verbose_name='有机相比例')),
                ('Flowrate', models.CharField(blank=True, max_length=32, verbose_name='流速')),
                ('project_Agilent_LC_MS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Project_Agilent_LC_MS', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '液相方法',
                'verbose_name_plural': '液相方法',
            },
        ),
    ]
