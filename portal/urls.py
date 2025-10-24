from django.urls import path
from . import views

app_name = "portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('new-portal/', views.new_portal, name="new-portal"),
]