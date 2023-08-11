from django.contrib import admin
from account.models import student, teacher

# Register your models here.
admin.site.register([student, teacher])