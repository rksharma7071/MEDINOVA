from django.contrib import admin
from .models import *

admin.site.site_header  =  "MEDINOVA LOGIN"  
admin.site.site_title  =  "MEDINOVA"
admin.site.index_title  =  "MEDINOVA MODELS"



@admin.register(Department)
class DepartmentAdminModel(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Doctor)
class DoctorAdminModel(admin.ModelAdmin):
    list_display = ['user', 'name', 'gender','dob','email','phone','address', 'specialty','note', 'created_date', 'photo']


@admin.register(Appointment)
class AppointmentAdminModel(admin.ModelAdmin):
    list_display = ['patient','department', 'doctor', 'datetime']


@admin.register(Patient)
class PatientAdminModel(admin.ModelAdmin):
    list_display = ['user', 'name', 'gender','dob','email','phone','address','note', 'created_date', 'photo']

