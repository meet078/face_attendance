import os
import shutil
from django.shortcuts import render, redirect
from account.models import student
from face_attendance.settings import BASE_DIR
from student.models import attendance as attend

# Create your views here.
def register(request):
    return render(request, "student_register.html")

def attendance(request):
    return render(request, "student_attendance.html", {"attendances" : attend.objects.filter(month=10, year=2022)})

def view(request):
    students = student.objects.all()
    return render(request, "student_view.html", {"students": students})

def new(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        rollno = request.POST["rollno"]
        contact = request.POST["contact"]
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        pincode = request.POST["pincode"]
        photo = request.FILES["photo"]
        stud = student.objects.create(first_name=first_name, last_name=last_name, rollno=rollno, contact=contact, email=email, address=address, city=city, state=state, pincode=pincode, profile=photo)
        stud.save()
        id = stud.pk
        dir_path = "static/known/"+str(id)+'/'
        filename = os.path.basename(str(stud.profile.path))
        path = os.path.join(BASE_DIR, dir_path)
        os.mkdir(path)
        shutil.copyfile(str(stud.profile.path),  str(path)+filename)
        os.remove(str(stud.profile.path))
        student.objects.filter(id=id).update(profile=dir_path+filename)
    return redirect(view)
