# Generated by Django 4.2.4 on 2023-09-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0021_alter_patient_department_alter_patient_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='first_login',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
