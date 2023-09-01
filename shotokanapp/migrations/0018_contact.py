# Generated by Django 3.2.20 on 2023-09-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shotokanapp', '0017_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('msg', models.TextField()),
                ('level', models.CharField(max_length=20)),
            ],
        ),
    ]