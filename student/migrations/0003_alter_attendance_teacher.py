# Generated by Django 4.0.4 on 2022-10-07 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_student_profile'),
        ('student', '0002_attendance_month_attendance_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.teacher'),
        ),
    ]
