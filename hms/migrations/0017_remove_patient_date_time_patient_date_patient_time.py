# Generated by Django 4.2.4 on 2023-09-01 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0016_remove_patient_date_remove_patient_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date_time',
        ),
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]