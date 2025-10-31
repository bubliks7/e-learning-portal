from django.urls import path
from . import views

urlpatterns = [
    path('/<int:kurs_id>/', views.enroll_course, name='enroll_course'),
]
