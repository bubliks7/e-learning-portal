from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user', views.login_user, name="login"),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
]