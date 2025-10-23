from django.urls import path
from . import views
from members import views
urlpatterns = [
    path('login/', views.login_user, name='login'),
]