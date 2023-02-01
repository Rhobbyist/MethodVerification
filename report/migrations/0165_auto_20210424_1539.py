# Generated by Django 3.0.5 on 2021-04-24 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0164_auto_20210424_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amrspecialmethod',
            name='aMRspecial',
        ),
        migrations.RemoveField(
            model_name='amrspecialtexts',
            name='aMRspecial',
        ),
        migrations.RemoveField(
            model_name='carryoverspecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='carryoverspecialmethod',
            name='carryoverspecial',
        ),
        migrations.RemoveField(
            model_name='carryoverspecialtexts',
            name='carryoverspecial',
        ),
        migrations.RemoveField(
            model_name='crrspecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='crrspecialmethod',
            name='cRRspecial',
        ),
        migrations.RemoveField(
            model_name='crrspecialtexts',
            name='cRRspecial',
        ),
        migrations.RemoveField(
            model_name='interprecisionspecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='interprecisionspecialmethod',
            name='interprecisionspecial',
        ),
        migrations.RemoveField(
            model_name='interprecisionspecialtexts',
            name='interprecisionspecial',
        ),
        migrations.RemoveField(
            model_name='jcxspecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='jcxspecialtexts',
            name='jCXspecial',
        ),
        migrations.RemoveField(
            model_name='matrixeffectspecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='matrixeffectspecialmethod',
            name='matrixeffectspecial',
        ),
        migrations.RemoveField(
            model_name='matrixeffectspecialtexts',
            name='matrixeffectspecial',
        ),
        migrations.RemoveField(
            model_name='msspecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='msspecialtexts',
            name='mSspecial',
        ),
        migrations.RemoveField(
            model_name='ptspecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='ptspecialaccept',
            name='pTspecial',
        ),
        migrations.RemoveField(
            model_name='ptspecialmethod',
            name='pTspecial',
        ),
        migrations.RemoveField(
            model_name='ptspecialtexts',
            name='pTspecial',
        ),
        migrations.RemoveField(
            model_name='recyclespecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='recyclespecialmethod',
            name='recyclespecial',
        ),
        migrations.RemoveField(
            model_name='recyclespecialtexts',
            name='recyclespecial',
        ),
        migrations.RemoveField(
            model_name='repeatprecisionspecial',
            name='special',
        ),
        migrations.RemoveField(
            model_name='repeatprecisionspecialmethod',
            name='repeatprecisionspecial',
        ),
        migrations.RemoveField(
            model_name='repeatprecisionspecialtexts',
            name='repeatprecisionspecial',
        ),
        migrations.AlterField(
            model_name='amr',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='amrconsluion',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
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
            model_name='carryover2',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='crr',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='crr2',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='endconclusion',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='jmd',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='lod',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='lodpicture',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='matrixeffect',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='ms',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='pt',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='recycle',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.AlterField(
            model_name='validation_reason',
            name='reportinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportInfo'),
        ),
        migrations.DeleteModel(
            name='AMRspecial',
        ),
        migrations.DeleteModel(
            name='AMRspecialmethod',
        ),
        migrations.DeleteModel(
            name='AMRspecialtexts',
        ),
        migrations.DeleteModel(
            name='Carryoverspecial',
        ),
        migrations.DeleteModel(
            name='Carryoverspecialmethod',
        ),
        migrations.DeleteModel(
            name='Carryoverspecialtexts',
        ),
        migrations.DeleteModel(
            name='CRRspecial',
        ),
        migrations.DeleteModel(
            name='CRRspecialmethod',
        ),
        migrations.DeleteModel(
            name='CRRspecialtexts',
        ),
        migrations.DeleteModel(
            name='Interprecisionspecial',
        ),
        migrations.DeleteModel(
            name='Interprecisionspecialmethod',
        ),
        migrations.DeleteModel(
            name='Interprecisionspecialtexts',
        ),
        migrations.DeleteModel(
            name='JCXspecial',
        ),
        migrations.DeleteModel(
            name='JCXspecialtexts',
        ),
        migrations.DeleteModel(
            name='Matrixeffectspecial',
        ),
        migrations.DeleteModel(
            name='Matrixeffectspecialmethod',
        ),
        migrations.DeleteModel(
            name='Matrixeffectspecialtexts',
        ),
        migrations.DeleteModel(
            name='MSspecial',
        ),
        migrations.DeleteModel(
            name='MSspecialtexts',
        ),
        migrations.DeleteModel(
            name='PTspecial',
        ),
        migrations.DeleteModel(
            name='PTspecialaccept',
        ),
        migrations.DeleteModel(
            name='PTspecialmethod',
        ),
        migrations.DeleteModel(
            name='PTspecialtexts',
        ),
        migrations.DeleteModel(
            name='Recyclespecial',
        ),
        migrations.DeleteModel(
            name='Recyclespecialmethod',
        ),
        migrations.DeleteModel(
            name='Recyclespecialtexts',
        ),
        migrations.DeleteModel(
            name='Repeatprecisionspecial',
        ),
        migrations.DeleteModel(
            name='Repeatprecisionspecialmethod',
        ),
        migrations.DeleteModel(
            name='Repeatprecisionspecialtexts',
        ),
        migrations.DeleteModel(
            name='Special',
        ),
    ]