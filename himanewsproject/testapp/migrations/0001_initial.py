# Generated by Django 4.1 on 2023-12-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hydjobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('pnumber', models.BigIntegerField()),
            ],
        ),
    ]
