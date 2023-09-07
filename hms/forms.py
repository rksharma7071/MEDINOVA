from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control bg-white border-0', 'style': 'height: 55px;', 'placeholder': 'YYYY-MM-DD'}),input_formats=['%Y-%m-%d'])
    class Meta:
        model = Patient
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class':'form-control bg-white border-0','style':"height: 55px;", 'placeholder':"Enter Name"}),
            'gender': forms.Select(attrs={'class':'form-control bg-white border-0 datetimepicker-input', 'style':"height: 55px;"}),
            # 'dob': forms.DateInput(attrs={'type': 'date', 'class':'form-control bg-white border-0','style':"height: 55px;",}),
            
            # 'dob': forms.DateInput(attrs={'type': 'date', 'class':'form-control bg-white border-0','style':"height: 55px;",}),

            'email': forms.EmailInput(attrs={'type': 'email', 'class':'form-control bg-white border-0','style':"height: 55px;", 'placeholder':"Enter Email Id"}),
            'phone': forms.TextInput(attrs={'type': 'text', 'class':'form-control bg-white border-0','style':"height: 55px;", 'placeholder':"Enter Phone No"}),
            'address': forms.TextInput(attrs={'type': 'text', 'class':'form-control bg-white border-0','style':"height: 55px;", 'placeholder':"Enter Address"}),
            'photo': forms.FileInput(attrs={'type': 'file', 'class':'form-control bg-white border-0', 'style':"height: 55px;"}),
            'note': forms.TextInput(attrs={'type': 'text', 'class':'form-control bg-white border-0','style':"height: 55px;", 'placeholder':"Enter Notes"}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local',  'class':'form-control bg-white border-0 datetimepicker-input', 'style':"height: 55px;"})
        }
