# Generated by Django 3.2.20 on 2023-08-15 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shotokanapp', '0005_alter_customuser_student_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='shotokanapp.studentlevelmod', verbose_name='Kyu To Achieve'),
        ),
    ]
