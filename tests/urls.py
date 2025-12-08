from django.urls import path
from . import views

app_name = "tests"

urlpatterns = [
    path('test/<int:pk>/', views.test_view, name='test_view'),
    path('test/<int:pk>/', views.question, name='question'),
]
