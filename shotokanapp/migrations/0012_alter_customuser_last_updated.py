# Generated by Django 3.2.20 on 2023-08-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shotokanapp', '0011_customuser_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Update'),
        ),
    ]
