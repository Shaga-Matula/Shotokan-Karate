# Generated by Django 3.2.20 on 2023-09-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shotokanapp', '0018_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fname',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='level',
            field=models.CharField(max_length=20, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lname',
            field=models.CharField(max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Contact Number'),
        ),
    ]
