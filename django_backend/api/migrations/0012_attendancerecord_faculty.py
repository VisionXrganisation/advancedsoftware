# Generated by Django 4.2.10 on 2025-03-31 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_student_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancerecord',
            name='faculty',
            field=models.ForeignKey(limit_choices_to={'role': 'teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendance_records', to=settings.AUTH_USER_MODEL),
        ),
    ]
