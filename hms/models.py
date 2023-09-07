from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



GENDER_CHOICES = (
    ('', 'Choose Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255, null=True, blank=True)
    specialty = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/doctor', null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    first_login = models.BooleanField(null=True, blank=True, default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='media/patient', null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    # appointment = models.ForeignKey(Appointment, null=True, blank=True, on_delete=models.CASCADE)
    first_login = models.BooleanField(null=True, blank=True, default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
    

class Medical_History(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.patient
    

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient}"


class Prescriptions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient}"