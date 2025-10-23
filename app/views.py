from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Kurs

def course_list(request):
    courses = Kurs.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Kurs, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})
