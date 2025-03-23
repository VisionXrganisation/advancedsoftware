from django.urls import path
from .views import hod_views, student_views, admin_views, faculty_views

urlpatterns = [
    # Student endpoints
    path('login/', student_views.login_view, name='login'),
    path('verify-otp/', student_views.verify_otp, name='verify_otp'),
    path('resend-otp/', student_views.resend_otp, name='resend_otp'),
    path('forgot-password/', student_views.forgot_password, name='forgot_password'),
    path('reset-password/', student_views.reset_password, name='reset_password'),
    path('register/', student_views.register_student, name='register_student'),
    path('student-attendance/', student_views.get_student_attendance, name='get_student_attendance'),

    # Admin endpoints
    # Removed 'enroll/' from admin_views; moved to faculty_views below

    # Faculty endpoints
    path('take-attendance/', faculty_views.take_attendance, name='take_attendance'),
    path('enroll/', faculty_views.enroll, name='enroll_student'),
    path('generate-statistics/', faculty_views.generate_statistics, name='generate_statistics'),
    path('download-pdf/<str:filename>/', faculty_views.download_pdf, name='download_pdf'),  # Moved to faculty_views
    path('students/', faculty_views.get_students, name='get_students'),
    
    # HOD endpoints
    path('subjects/', hod_views.get_subjects, name='get_subjects'),
    path('attendance-files/', hod_views.get_attendance_files, name='get_attendance_files'),
    path('generate-statistics/', hod_views.generate_statistics, name='generate_statistics'),
    path('download/<str:filename>/', hod_views.download_file, name='download_file'),
]