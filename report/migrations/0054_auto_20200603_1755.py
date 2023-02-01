# Generated by Django 3.0.5 on 2020-06-03 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0053_auto_20200603_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='PJjmd2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='子验证指标')),
            ],
            options={
                'verbose_name': '中间精密度',
                'verbose_name_plural': '中间精密度',
            },
        ),
        migrations.CreateModel(
            name='PNjmd2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='子验证指标')),
            ],
            options={
                'verbose_name': '重复性精密度',
                'verbose_name_plural': '重复性精密度',
            },
        ),
        migrations.CreateModel(
            name='PTback2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='子验证指标')),
            ],
            options={
                'verbose_name': 'PT',
                'verbose_name_plural': 'PT',
            },
        ),
        migrations.CreateModel(
            name='Recycleback2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='子验证指标')),
            ],
            options={
                'verbose_name': '加标回收率',
                'verbose_name_plural': '加标回收率',
            },
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=32, verbose_name='项目')),
            ],
            options={
                'verbose_name': '特殊参数设置',
                'verbose_name_plural': '特殊参数设置',
            },
        ),
        migrations.AlterModelOptions(
            name='pjjmd',
            options={'verbose_name': '中间精密度', 'verbose_name_plural': '中间精密度'},
        ),
        migrations.AlterModelOptions(
            name='pnjmd',
            options={'verbose_name': '重复性精密度', 'verbose_name_plural': '重复性精密度'},
        ),
        migrations.AlterField(
            model_name='pjjmd',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='通用性参数设置'),
        ),
        migrations.AlterField(
            model_name='pjjmdmethod',
            name='pJjmd',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.PJjmd', verbose_name='中间精密度'),
        ),
        migrations.AlterField(
            model_name='pjjmdtexts',
            name='pJjmd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.PJjmd', verbose_name='中间精密度'),
        ),
        migrations.AlterField(
            model_name='pnjmd',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='通用性参数设置'),
        ),
        migrations.AlterField(
            model_name='pnjmdmethod',
            name='pNjmd',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.PNjmd', verbose_name='重复性精密度'),
        ),
        migrations.AlterField(
            model_name='pnjmdtexts',
            name='pNjmd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.PNjmd', verbose_name='重复性精密度'),
        ),
        migrations.AlterField(
            model_name='ptback',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='通用性参数设置'),
        ),
        migrations.AlterField(
            model_name='recycleback',
            name='general',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.General', verbose_name='通用性参数设置'),
        ),
        migrations.CreateModel(
            name='Recycleback2texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='描述性内容')),
                ('recycleback2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Recycleback2', verbose_name='加标回收率')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.CreateModel(
            name='Recycleback2Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lowvalue', models.FloatField(blank=True, verbose_name='回收率下限(%)')),
                ('upvalue', models.FloatField(blank=True, verbose_name='回收率上限(%)')),
                ('recycleback2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.Recycleback2', verbose_name='加标回收率')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.AddField(
            model_name='recycleback2',
            name='special',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Special', verbose_name='特殊参数设置'),
        ),
        migrations.CreateModel(
            name='PTback2texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='描述性内容')),
                ('pTback2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.PTback2', verbose_name='PT')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.CreateModel(
            name='PTback2Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minSample', models.FloatField(verbose_name='所需最小样本数')),
                ('minPass', models.FloatField(verbose_name='最低通过率CV(%)')),
                ('pTback2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.PTback2', verbose_name='PT')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.AddField(
            model_name='ptback2',
            name='special',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Special', verbose_name='特殊参数设置'),
        ),
        migrations.CreateModel(
            name='PNjmd2texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='描述性内容')),
                ('pNjmd2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.PNjmd2', verbose_name='重复性精密度')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.CreateModel(
            name='PNjmd2Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minSample', models.FloatField(verbose_name='所需最小样本数')),
                ('maxCV', models.FloatField(verbose_name='最大允许CV(%)')),
                ('pNjmd2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.PNjmd2', verbose_name='重复性精密度')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.AddField(
            model_name='pnjmd2',
            name='special',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Special', verbose_name='特殊参数设置'),
        ),
        migrations.CreateModel(
            name='PJjmd2texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='描述性内容')),
                ('pJjmd2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.PJjmd2', verbose_name='中间精密度')),
            ],
            options={
                'verbose_name': '描述性内容',
                'verbose_name_plural': '描述性内容',
            },
        ),
        migrations.CreateModel(
            name='PJjmd2Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minSample', models.FloatField(verbose_name='所需最小样本数')),
                ('maxCV', models.FloatField(verbose_name='最大允许CV(%)')),
                ('pJjmd2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.PJjmd2', verbose_name='中间精密度')),
            ],
            options={
                'verbose_name': '基本参数',
                'verbose_name_plural': '基本参数',
            },
        ),
        migrations.AddField(
            model_name='pjjmd2',
            name='special',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Special', verbose_name='特殊参数设置'),
        ),
    ]
