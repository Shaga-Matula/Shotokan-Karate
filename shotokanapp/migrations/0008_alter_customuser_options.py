# Generated by Django 3.2.20 on 2023-08-16 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shotokanapp', '0007_alter_studentlevelmod_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Shotokan Membrers', 'verbose_name_plural': 'Shotokan Membrers'},
        ),
    ]