from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Kursy
from portal.models import Uzytkownicy

def home(request):
    new_courses = Kursy.objects.order_by('-data_utworzenia')[:3]
    return render(request, 'portal/index.html', {'new_courses': new_courses})

def course_list(request):
    courses = Kursy.objects.all()
    return render(request, 'portal/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Kursy, pk=pk)
    return render(request, 'portal/course_detail.html', {'course': course})

@login_required
def profile(request):
    profil = Uzytkownicy.objects.get(user=request.user)
    return render(request, 'portal/profile.html', {'profil': profil})
