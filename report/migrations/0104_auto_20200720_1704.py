# Generated by Django 3.0.5 on 2020-07-20 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0103_auto_20200720_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer_LC_MS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='仪器厂家')),
                ('lC_MS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.LC_MS', verbose_name='液相色谱串联质谱平台')),
            ],
            options={
                'verbose_name': '仪器厂家',
                'verbose_name_plural': '仪器厂家',
            },
        ),
        migrations.CreateModel(
            name='Project_Manufacturer_LC_MS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='项目名称')),
                ('manufacturer_LC_MS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Manufacturer_LC_MS', verbose_name='仪器厂家')),
            ],
            options={
                'verbose_name': '项目名称',
                'verbose_name_plural': '项目名称',
            },
        ),
        migrations.CreateModel(
            name='YX_Project_Manufacturer_LC_MS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=32, verbose_name='时间')),
                ('Organic_comparison', models.CharField(blank=True, max_length=32, verbose_name='有机相比例')),
                ('Flowrate', models.CharField(blank=True, max_length=32, verbose_name='流速')),
                ('project_Manufacturer_LC_MS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Project_Manufacturer_LC_MS', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '液相方法',
                'verbose_name_plural': '液相方法',
            },
        ),
        migrations.CreateModel(
            name='ZP_Project_Manufacturer_LC_MS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('norm', models.CharField(blank=True, max_length=32, verbose_name='待测物')),
                ('precursor_ion', models.CharField(blank=True, max_length=32, verbose_name='母离子')),
                ('product_ion', models.CharField(blank=True, max_length=32, verbose_name='子离子')),
                ('Collision_Energy', models.CharField(blank=True, max_length=32, verbose_name='Collision_Energy')),
                ('Collision_Cell_Exit_Potential', models.CharField(blank=True, max_length=32, verbose_name='Collision_Cell_Exit_Potential')),
                ('project_Manufacturer_LC_MS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Project_Manufacturer_LC_MS', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '质谱方法',
                'verbose_name_plural': '质谱方法',
            },
        ),
        migrations.RemoveField(
            model_name='agilent_lc_ms',
            name='lC_MS',
        ),
        migrations.RemoveField(
            model_name='project_ab_lc_ms',
            name='aB_LC_MS',
        ),
        migrations.RemoveField(
            model_name='project_agilent_lc_ms',
            name='agilent_LC_MS',
        ),
        migrations.RemoveField(
            model_name='project_shimadzu_lc_ms',
            name='shimadzu_LC_MS',
        ),
        migrations.RemoveField(
            model_name='shimadzu_lc_ms',
            name='lC_MS',
        ),
        migrations.RemoveField(
            model_name='yx_project_ab_lc_ms',
            name='project_AB_LC_MS',
        ),
        migrations.RemoveField(
            model_name='yx_project_agilent_lc_ms',
            name='project_Agilent_LC_MS',
        ),
        migrations.RemoveField(
            model_name='yx_project_shimadzu_lc_ms',
            name='project_Shimadzu_LC_MS',
        ),
        migrations.RemoveField(
            model_name='zp_project_ab_lc_ms',
            name='project_AB_LC_MS',
        ),
        migrations.RemoveField(
            model_name='zp_project_agilent_lc_ms',
            name='project_Agilent_LC_MS',
        ),
        migrations.RemoveField(
            model_name='zp_project_shimadzu_lc_ms',
            name='project_Shimadzu_LC_MS',
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
        migrations.AlterField(
            model_name='validation_reason',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.DeleteModel(
            name='AB_LC_MS',
        ),
        migrations.DeleteModel(
            name='Agilent_LC_MS',
        ),
        migrations.DeleteModel(
            name='Project_AB_LC_MS',
        ),
        migrations.DeleteModel(
            name='Project_Agilent_LC_MS',
        ),
        migrations.DeleteModel(
            name='Project_Shimadzu_LC_MS',
        ),
        migrations.DeleteModel(
            name='Shimadzu_LC_MS',
        ),
        migrations.DeleteModel(
            name='YX_Project_AB_LC_MS',
        ),
        migrations.DeleteModel(
            name='YX_Project_Agilent_LC_MS',
        ),
        migrations.DeleteModel(
            name='YX_Project_Shimadzu_LC_MS',
        ),
        migrations.DeleteModel(
            name='ZP_Project_AB_LC_MS',
        ),
        migrations.DeleteModel(
            name='ZP_Project_Agilent_LC_MS',
        ),
        migrations.DeleteModel(
            name='ZP_Project_Shimadzu_LC_MS',
        ),
    ]
