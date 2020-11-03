# Generated by Django 3.1 on 2020-09-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200911_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.TextField(choices=[('M', 'Married'), ('D', 'Divorced'), ('S', 'Separated'), ('SN', 'Single')], null=True),
        ),
        migrations.DeleteModel(
            name='MaritalStatus',
        ),
    ]
