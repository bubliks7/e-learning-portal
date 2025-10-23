from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainWeb, name="mainWeb"),
    path("", views.course_list, name="course_list"),
    path("<int:pk>/", views.course_detail, name="course_detail"),
]