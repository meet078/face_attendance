# Generated by Django 4.0.4 on 2022-10-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_video_upload_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_upload',
            name='video',
            field=models.FileField(upload_to='static/sample'),
        ),
    ]
