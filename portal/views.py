from django.shortcuts import render, get_object_or_404
from .models import Kursy
from django.contrib.auth.decorators import login_required

def home(request):
    new_courses = Kursy.objects.order_by('-data_utworzenia')[:3]
    return render(request, 'portal/index.html', {'new_courses': new_courses})

def course_list(request):
    courses = Kursy.objects.all()
    return render(request, 'portal/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Kursy, pk=pk)
    return render(request, 'portal/course_detail.html', {'course': course})

# @login_required(login_url="/users/login/")
# def new_portal(request):
#     return render(request, 'portal/new_portal.html')