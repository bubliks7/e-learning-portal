from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Kursy
from django.contrib import messages
from .forms import RejestracjaForm

def home(request):
    new_courses = Kursy.objects.order_by('-data_utworzenia')[:3]
    return render(request, 'portal/index.html', {'new_courses': new_courses})

def course_list(request):
    courses = Kursy.objects.all()
    return render(request, 'portal/course_list.html', {'courses': courses})

# def course_detail(request, pk):
#     course = get_object_or_404(Kursy, pk=pk)
#     return render(request, 'portal/course_detail.html', {'course': course})

@login_required
def accound(request):
    user = request.user
    return render(request, 'portal/profile.html', {'user': user})

def register(request):
    if request.method == "POST":
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Utworzono konto")
            return redirect('/users/login/')
    else:
        form = RejestracjaForm()
    return render(request, 'portal/register.html', {'form': form})