# Generated by Django 3.1 on 2020-09-10 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200910_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='pan1',
            field=models.CharField(default='AAA0000000', max_length=10),
        ),
    ]
