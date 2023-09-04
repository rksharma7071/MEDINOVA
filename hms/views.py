from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.shortcuts import render, HttpResponse
from .models import Department, Doctor, Patient
from django.contrib.auth.models import User, Group, Permission
import random
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required



def view_home(request):
    return render(request,'hms/home.html', locals())


def view_about(request):
    return render(request, 'hms/about.html', locals())


def view_service(request):
    return render(request, 'hms/service.html', locals())


def view_pricing(request):
    return render(request, 'hms/price.html', locals())


def view_blog(request):
    return render(request, 'hms/blog.html', locals())


def view_detail(request):
    return render(request, 'hms/detail.html', locals())


def view_team(request):
    return render(request, 'hms/team.html', locals())


def view_testimonial(request):
    return render(request, 'hms/testimonial.html', locals())


def view_search(request):
    return render(request, 'hms/search.html', locals())


def view_contact(request):
    return render(request, 'hms/contact.html', locals())


def view_login(request):
    if request.user.is_authenticated:
        g = request.user.groups.all()
        if g[0].name == 'PatientGroup':
            return redirect('dashboard_patient')
        elif g[0].name == 'DoctorGroup':
            return redirect('dashboard_doctor')
        elif g[0].name == 'StaffGroup':
            return redirect('dashboard_staff')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('change_password')
        else:
            msg = 'Invalid username and password. Please try again.'
            return render(request, 'hms/login.html', locals())
    else:
        return render(request, 'hms/login.html', locals())


@login_required(login_url='login')
def view_change_password(request):
    new_user = False
    try:
        patient = Patient.objects.get(user = request.user)
        new_user = patient
        print(patient, "-------------------------------------------------------------------")
    except:
        doctor = Doctor.objects.get(user = request.user)
        new_user = doctor
        print(doctor, "-------------------------------------------------------------------")


    if request.method == "POST":
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = User.objects.get(username = request.user)

        if password1 == password2:
            user.set_password(password1)
            user.save()
            new_user.first_login = True
            new_user.save()
            msg = 'Password Update Successfully.'
            g = request.user.groups.all()
            if g[0].name == 'DoctorGroup':
                return redirect('dashboard_doctor')
            elif g[0].name == 'PatientGroup':
                return redirect('dashboard_patient')
            elif g[0].name == 'StaffGroup':
                return redirect('dashboard_staff')
        else:
            error = 'Password does not match, Please try again.'
        return render(request, 'hms/change_password.html', locals())
    
    else:
        if new_user.first_login:
            g = request.user.groups.all()
            if g[0].name == 'DoctorGroup':
                return redirect('dashboard_doctor')
            elif g[0].name == 'PatientGroup':
                return redirect('dashboard_patient')
            elif g[0].name == 'StaffGroup':
                return redirect('dashboard_staff')
        else:
            return render(request, 'hms/change_password.html', locals())
            

@login_required(login_url='login')
def view_dashboard_doctor(request):
    return render(request, 'hms/dashboard_doctor.html', locals())


@login_required(login_url='login')
def view_dashboard_patient(request):    
    patient = Patient.objects.get(user = request.user)
    return render(request, 'hms/dashboard_patient.html', locals())


@login_required(login_url='login')
def view_dashboard_staff(request):
    return render(request, 'hms/dashboard_staff.html', locals())


def view_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def view_appointment(request):
    depart = Department.objects.all()
    doc = Doctor.objects.all()
    patients = Patient.objects.all().order_by('date_time')
    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            id = str(patient.id)
            if len(id) < 6:
                id = id.zfill(6)

            username = f"MEDI{id}"
            password = 'MEDINOVA@123'
            
            user = User.objects.create_user(username=username, password=password)
            user.is_staff = True
            g1 = Group.objects.get(id=1)
            user.groups.add(g1)
            user.save()

            patient.user = user
            patient.save()
            msg = f"Patient Registration No: {username} Password: {password}"
            print(msg)
            return render(request, 'hms/appointment.html', locals())
    else:
        form = PatientForm()
    return render(request, 'hms/appointment.html', locals())


