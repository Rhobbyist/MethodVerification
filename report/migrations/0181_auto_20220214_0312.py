# Generated by Django 3.2.8 on 2022-02-14 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0180_alter_stabilityspecial_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stabilityspecialmethod',
            name='stabilityspecial',
        ),
        migrations.RemoveField(
            model_name='stabilityspecialtexts',
            name='stabilityspecial',
        ),
        migrations.DeleteModel(
            name='Stabilityspecial',
        ),
        migrations.DeleteModel(
            name='Stabilityspecialmethod',
        ),
        migrations.DeleteModel(
            name='Stabilityspecialtexts',
        ),
    ]
