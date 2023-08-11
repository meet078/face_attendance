# Generated by Django 4.0.4 on 2022-10-07 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_1', models.SmallIntegerField()),
                ('_2', models.SmallIntegerField()),
                ('_3', models.SmallIntegerField()),
                ('_4', models.SmallIntegerField()),
                ('_5', models.SmallIntegerField()),
                ('_6', models.SmallIntegerField()),
                ('_7', models.SmallIntegerField()),
                ('_8', models.SmallIntegerField()),
                ('_9', models.SmallIntegerField()),
                ('_10', models.SmallIntegerField()),
                ('_11', models.SmallIntegerField()),
                ('_12', models.SmallIntegerField()),
                ('_13', models.SmallIntegerField()),
                ('_14', models.SmallIntegerField()),
                ('_15', models.SmallIntegerField()),
                ('_16', models.SmallIntegerField()),
                ('_17', models.SmallIntegerField()),
                ('_18', models.SmallIntegerField()),
                ('_19', models.SmallIntegerField()),
                ('_20', models.SmallIntegerField()),
                ('_21', models.SmallIntegerField()),
                ('_22', models.SmallIntegerField()),
                ('_23', models.SmallIntegerField()),
                ('_24', models.SmallIntegerField()),
                ('_25', models.SmallIntegerField()),
                ('_26', models.SmallIntegerField()),
                ('_27', models.SmallIntegerField()),
                ('_28', models.SmallIntegerField()),
                ('_29', models.SmallIntegerField()),
                ('_30', models.SmallIntegerField()),
                ('_31', models.SmallIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.teacher')),
            ],
        ),
    ]