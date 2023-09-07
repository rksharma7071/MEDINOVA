from django.urls import path
from .views import *

#BASE URL =>>  # http://127.0.0.1:8000/hmsapp/

urlpatterns = [
    path('',view_home, name='home'), 
    path('about/', view_about, name='about'),   
    path('service/', view_service, name='service'),
    path('pricing/', view_pricing, name='pricing'),
    path('blog/', view_blog, name='blog'),
    path('detail/',view_detail, name='detail'),
    path('team/', view_team, name='team'),
    path('testimonial/', view_testimonial, name='testimonial'),
    path('search/', view_search, name='search'),
    path('contact/', view_contact, name='contact'),
    path('appointment/', view_appointment, name='appointment'),
    path('registration/', view_patient_registration, name='registration'),
    path('patient_update/<int:pid>', view_patient_update, name='patient_update'),
    path('patient_delete/<int:pid>', view_patient_delete, name='patient_delete'),
    path('change_password/', view_change_password, name='change_password'),
    path('login/', view_login, name='login'),
    path('dashboard_doctor/', view_dashboard_doctor, name='dashboard_doctor'),    
    path('dashboard_patient/', view_dashboard_patient, name='dashboard_patient'),    
    path('dashboard_staff/', view_dashboard_staff, name='dashboard_staff'), 
    path('logout/', view_logout, name='logout')
]


