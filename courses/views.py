from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Enrollment
from portal.models import Kursy, Uzytkownicy

@login_required
def enroll_course(request, kurs_id):
    kurs = get_object_or_404(Kursy, id=kurs_id)
    uzytkownik = get_object_or_404(Uzytkownicy, email=request.user.email)
    Enrollment.objects.get_or_create(uzytkownik=uzytkownik, kurs=kurs)
    # return redirect('course_detail', pk=kurs.id)
    return render(request, 'portal/zapisano.html', {'kurs': kurs})

def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'portal/zapisane_kursy.html', {'enrollments': enrollments})
