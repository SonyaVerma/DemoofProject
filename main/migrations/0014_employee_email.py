# Generated by Django 3.1 on 2020-09-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='x', max_length=254),
        ),
    ]