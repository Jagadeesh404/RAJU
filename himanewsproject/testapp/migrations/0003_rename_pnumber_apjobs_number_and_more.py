# Generated by Django 4.1 on 2023-12-11 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_apjobs_kajobs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apjobs',
            old_name='pnumber',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='hydjobs',
            old_name='pnumber',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='kajobs',
            old_name='pnumber',
            new_name='number',
        ),
    ]
