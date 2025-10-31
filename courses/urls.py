from django.urls import path
from . import views

app_name = 'saved_courses'

urlpatterns = [
    path('enroll/enroll/<int:kurs_id>/', views.enroll_course, name='enroll_course'),
    path('enrolls/', views.enroll_view, name='enroll_view'),
]
