# Generated by Django 4.2.4 on 2023-09-06 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hms', '0024_appointment_datetime_remove_patient_date_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment_datetime',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
