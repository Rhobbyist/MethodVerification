# Generated by Django 3.0.5 on 2020-06-18 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0070_auto_20200617_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interprecisiongeneralmethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minSample', models.FloatField(verbose_name='所需最小样本数')),
                ('maxCV', models.FloatField(verbose_name='最大允许CV(%)')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.CreateModel(
            name='Interprecisiongeneraltexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=200, verbose_name='描述性内容')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.CreateModel(
            name='Interprecisionspecialmethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minSample', models.FloatField(verbose_name='所需最小样本数')),
                ('maxCV', models.FloatField(verbose_name='最大允许CV(%)')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.CreateModel(
            name='PTgeneralmethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minSample', models.FloatField(blank=True, verbose_name='所需最小样本数')),
                ('minPass', models.FloatField(blank=True, verbose_name='最低通过率CV(%)')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.CreateModel(
            name='PTgeneraltexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='描述性内容')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.CreateModel(
            name='Recyclegeneralmethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lowvalue', models.FloatField(blank=True, verbose_name='回收率下限(%)')),
                ('upvalue', models.FloatField(blank=True, verbose_name='回收率上限(%)')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.CreateModel(
            name='Recyclegeneraltexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='描述性内容')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.CreateModel(
            name='Repeatprecisiongeneralmethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minSample', models.FloatField(verbose_name='所需最小样本数')),
                ('maxCV', models.FloatField(verbose_name='最大允许CV(%)')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.CreateModel(
            name='Repeatprecisiongeneraltexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=200, verbose_name='描述性内容')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.RenameModel(
            old_name='PJjmd2texts',
            new_name='Interprecisionspecialtexts',
        ),
        migrations.RenameModel(
            old_name='PTback2',
            new_name='PTspecial',
        ),
        migrations.RenameModel(
            old_name='PTback2accept',
            new_name='PTspecialaccept',
        ),
        migrations.RenameModel(
            old_name='PTback2Method',
            new_name='PTspecialmethod',
        ),
        migrations.RenameModel(
            old_name='PTback2texts',
            new_name='PTspecialtexts',
        ),
        migrations.RenameModel(
            old_name='PTback2unit',
            new_name='PTspecialunit',
        ),
        migrations.RenameModel(
            old_name='Recycleback2',
            new_name='Recyclespecial',
        ),
        migrations.RenameModel(
            old_name='Recycleback2Method',
            new_name='Recyclespecialmethod',
        ),
        migrations.RenameModel(
            old_name='Recycleback2texts',
            new_name='Recyclespecialtexts',
        ),
        migrations.RemoveField(
            model_name='pjjmdmethod',
            name='PJJMD_key',
        ),
        migrations.RemoveField(
            model_name='pjjmdtexts',
            name='PJJMD_key',
        ),
        migrations.RemoveField(
            model_name='pnjmdmethod',
            name='PNJMD_key',
        ),
        migrations.RemoveField(
            model_name='pnjmdtexts',
            name='PNJMD_key',
        ),
        migrations.RemoveField(
            model_name='ptbackmethod',
            name='PTback_key',
        ),
        migrations.RemoveField(
            model_name='ptbacktexts',
            name='PTback_key',
        ),
        migrations.RemoveField(
            model_name='recyclebackmethod',
            name='RECYCLEback_key',
        ),
        migrations.RemoveField(
            model_name='recyclebacktexts',
            name='RECYCLEback_key',
        ),
        migrations.RenameField(
            model_name='interprecisionspecialtexts',
            old_name='pJjmd2',
            new_name='interprecisionspecial',
        ),
        migrations.RenameField(
            model_name='ptspecialaccept',
            old_name='pTback2',
            new_name='pTspecial',
        ),
        migrations.RenameField(
            model_name='ptspecialmethod',
            old_name='pTback2',
            new_name='pTspecial',
        ),
        migrations.RenameField(
            model_name='ptspecialtexts',
            old_name='pTback2',
            new_name='pTspecial',
        ),
        migrations.RenameField(
            model_name='ptspecialunit',
            old_name='pTback2',
            new_name='pTspecial',
        ),
        migrations.RenameField(
            model_name='recyclespecialmethod',
            old_name='recycleback2',
            new_name='recyclespecial',
        ),
        migrations.RenameField(
            model_name='recyclespecialtexts',
            old_name='recycleback2',
            new_name='recyclespecial',
        ),
        migrations.RenameModel(
            old_name='PJjmd',
            new_name='Interprecisiongeneral',
        ),
        migrations.RenameModel(
            old_name='PJjmd2',
            new_name='Interprecisionspecial',
        ),
        migrations.RenameModel(
            old_name='PTback',
            new_name='PTgeneral',
        ),
        migrations.RenameModel(
            old_name='Recycleback',
            new_name='Recyclegeneral',
        ),
        migrations.RenameModel(
            old_name='PNjmd',
            new_name='Repeatprecisiongeneral',
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
        
        
        migrations.DeleteModel(
            name='PJjmd2Method',
        ),
        migrations.DeleteModel(
            name='PJjmdMethod',
        ),
        migrations.DeleteModel(
            name='PJjmdtexts',
        ),
        migrations.DeleteModel(
            name='PNjmdMethod',
        ),
        migrations.DeleteModel(
            name='PNjmdtexts',
        ),
        migrations.DeleteModel(
            name='PTbackMethod',
        ),
        migrations.DeleteModel(
            name='PTbacktexts',
        ),
        migrations.DeleteModel(
            name='RecyclebackMethod',
        ),
        migrations.DeleteModel(
            name='Recyclebacktexts',
        ),
        migrations.AddField(
            model_name='repeatprecisiongeneraltexts',
            name='repeatprecisiongeneral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Repeatprecisiongeneral', verbose_name='重复性精密度'),
        ),
        migrations.AddField(
            model_name='repeatprecisiongeneralmethod',
            name='repeatprecisiongeneral',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.Repeatprecisiongeneral', verbose_name='重复性精密度'),
        ),
        migrations.AddField(
            model_name='recyclegeneraltexts',
            name='recyclegeneral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Recyclegeneral', verbose_name='加标回收率'),
        ),
        migrations.AddField(
            model_name='recyclegeneralmethod',
            name='recyclegeneral',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.Recyclegeneral', verbose_name='加标回收率'),
        ),
        migrations.AddField(
            model_name='ptgeneraltexts',
            name='pTgeneral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.PTgeneral', verbose_name='PT'),
        ),
        migrations.AddField(
            model_name='ptgeneralmethod',
            name='pTgeneral',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.PTgeneral', verbose_name='PT'),
        ),
        migrations.AddField(
            model_name='interprecisionspecialmethod',
            name='interprecisionspecial',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.Interprecisionspecial', verbose_name='中间精密度'),
        ),
        migrations.AddField(
            model_name='interprecisiongeneraltexts',
            name='interprecisiongeneral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Interprecisiongeneral', verbose_name='中间精密度'),
        ),
        migrations.AddField(
            model_name='interprecisiongeneralmethod',
            name='interprecisiongeneral',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.Interprecisiongeneral', verbose_name='中间精密度'),
        ),
    ]