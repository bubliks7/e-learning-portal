from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Kursy

# Create your views here.

def course_detail(request, pk):
    course = get_object_or_404(Kursy, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})