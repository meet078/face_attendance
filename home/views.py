from datetime import datetime
from django.shortcuts import render, redirect
from account.models import student
from .models import video_upload
from student.models import attendance
from facereader.facedetection import facerecognition

def home(request):
    return render(request, "index.html")

def calendar(request):
    return render(request, "calendar.html")

def charts(request):
    return render(request, "charts.html")


def uploadvideo(request):
    if(request.method == "POST"):
        date = request.POST["date"]
        video = request.FILES["video"]
        attend = video_upload.objects.create(date=date, video=video)
        attend.save()
        date = datetime.strptime(date, "%Y-%m-%d").date()
        students = student.objects.all()
        for stud in students:
            if not attendance.objects.filter(student = stud.pk, month=date.month, year=date.year).exists() :
                attendance(student=stud, month=date.month, year=date.year ).save()
        facerecognition(str(attend.video.path), day=date.day, month=date.month, year=date.year)
    return redirect(home)