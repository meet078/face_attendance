from django.db import models

# Create your models here.
class video_upload(models.Model):
    date = models.DateField()
    video = models.FileField(upload_to="static/sample")