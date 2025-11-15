"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from courses import views as course_views

urlpatterns = [
    path('', include('portal.urls')),
    path('courses/', include('portal.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accound/', include('portal.urls')),
    path('register/', include('portal.urls')),
    path('enroll/', include(('courses.urls', 'portal'), namespace='portal')),
    path('saved_courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('course_view/<int:pk>/', course_views.view_course, name='view_course'),
    path('test/<int:pk>/', include('tests.urls')),
]
