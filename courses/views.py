from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Enrollment
from portal.models import Kursy, Uzytkownicy, Lekcja

@login_required
def enroll_course(request, kurs_id):
    kurs = get_object_or_404(Kursy, id=kurs_id)
    uzytkownik = get_object_or_404(Uzytkownicy, email=request.user.email)
    Enrollment.objects.get_or_create(uzytkownik=uzytkownik, kurs=kurs)
    return render(request, 'portal/zapisano.html', {'kurs': kurs})

@login_required
def my_courses(request):
    uzytkownik = get_object_or_404(Uzytkownicy, email=request.user.email)
    enrollments = Enrollment.objects.filter(uzytkownik=uzytkownik)
    return render(request, 'portal/zapisane_kursy.html', {'enrollments': enrollments})

def view_course(request, pk):
    course = get_object_or_404(Kursy, pk=pk)
    test = course.testy.first()
    lessons = Lekcja.objects.filter(kurs=course).order_by("order")
    return render(request, 'courses/view_course.html', {
        'course': course,
        'test': test,
        'lessons': lessons,
    })

