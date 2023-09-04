from django.contrib import admin
from .models import *


@admin.register(Department)
class DepartmentAdminModel(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Doctor)
class DoctorAdminModel(admin.ModelAdmin):
    list_display = ['user', 'name', 'gender','dob','email','phone','address', 'specialty','note', 'created_date', 'photo']


@admin.register(Patient)
class PatientAdminModel(admin.ModelAdmin):
    list_display = ['user', 'name', 'gender','dob','email','phone','address','note', 'department', 'doctor', 'date_time' , 'created_date', 'photo']

