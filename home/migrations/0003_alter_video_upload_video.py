# Generated by Django 4.0.4 on 2022-10-07 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_video_upload_delete_student_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_upload',
            name='video',
            field=models.FileField(upload_to='face_attendance/static/sample'),
        ),
    ]
