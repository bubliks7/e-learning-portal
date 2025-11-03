from django.urls import path
from . import views

app_name = 'saved_courses'

urlpatterns = [
    path('enroll/enroll/<int:kurs_id>/', views.enroll_course, name='enroll_course'),
    path('enrolls/', views.my_courses, name='my_courses'),
    path('course_sql/', views.view_course, name='view_course'),
]
