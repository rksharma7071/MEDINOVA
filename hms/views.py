from django.shortcuts import render, redirect, get_object_or_404
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
            msg = {
                'icon' : 'error',
                'title' : 'Oops!',
                'text' : 'Invalid username and password. Please try again.'
            }
            return render(request, 'hms/login.html', locals())
    else:
        return render(request, 'hms/login.html', locals())


@login_required(login_url='login')
def view_change_password(request):
    new_user = False

    g = request.user.groups.all()
    if g[0].name == 'StaffGroup':
        return redirect('dashboard_staff')


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

            msg = {
                'icon' : 'success',
                'title' : 'Congratulation!',
                'text' : 'Password Update Successfully.'
            }

            
            if g[0].name == 'DoctorGroup':
                return redirect('dashboard_doctor')
            elif g[0].name == 'PatientGroup':
                return redirect('dashboard_patient')
        else:
            msg = {
                'icon' : 'error',
                'title' : 'Oops!',
                'text' : 'Password does not match, Please try again.'
            }
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


def view_patient_registration(request):
    depart = Department.objects.all()
    doc = Doctor.objects.all()
    patients = Patient.objects.all().order_by('-created_date')
    if request.method == "POST":
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
            form = PatientForm()

            msg = {
                'icon' : 'success',
                'title' : 'Congratulation!',
                'text' : f"Dear member you have successfully registered as Patient Registration No: {username} and Password: {password}"
            }

        return render(request, 'hms/registration.html', locals())

    else:
        form = PatientForm()
        return render(request, 'hms/registration.html', locals())


def view_patient_update(request, pid):
    patients = Patient.objects.all()
    patient = Patient.objects.get(id=pid)
    user = patient.user
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = user
            patient.save()
            msg = {
                'icon' : 'success',
                'title' : 'Congratulation!',
                'text' : 'Patient Update Successfully.'
            }
            return render(request, 'hms/registration.html', locals())
        else:
            msg = {
                'icon' : 'error',
                'title' : 'Oops!',
                'text' : 'Something went wrong. Please try again.'
            }
    else:
        form = PatientForm(instance=patient)

    return render(request, 'hms/patient_update.html', locals())



def view_patient_delete(request, pid):
    patient = Patient.objects.get(id=pid)
    
    msg = {
        'icon' : 'success',
        'title' : 'Congratulation!',
        'text' : f'Are you sure to delete the patient {patient.user}, {patient.name}'
    }

    patient.delete()
    return render(request, 'hms/registration.html', locals())



@login_required(login_url='login')
def view_appointment(request):
    departments = Department.objects.all()
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.all() 

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        user = request.POST.get('user')
        department_id = request.POST.get('department')
        doctor_id = request.POST.get('doctor')

        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            msg = {
                'icon' : 'error',
                'title' : 'Oops!',
                'text' : "Patient Registration No. does not exist. Please enter the valid registration no."
            }
            return render(request, 'hms/appointment.html', locals())

        
        patient = Patient.objects.get(user=user)

        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.department = Department.objects.get(id = department_id)
            appointment.doctor = Doctor.objects.get(id = doctor_id)
            appointment.patient = patient
            appointment.save()
            
            msg = {
                'icon' : 'success',
                'title' : 'Thanks You!',
                'text' : f"Patient Appointment Book Successfully."
            }
            return render(request, 'hms/appointment.html', locals())
            
    else:
        appointment_form = AppointmentForm()
        form = PatientForm()
    return render(request, 'hms/appointment.html', locals())


