from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from .models import Uzytkownicy, Kursy

def index(request):
    latest_users = Uzytkownicy.objects.order_by("-id")[:5]
    context = {"latest_users": latest_users}
    return render(request, "polls/index.html", context)

def detail(request, uzytkownik_id):
    uzytkownik = get_object_or_404(Uzytkownicy, pk=uzytkownik_id)
    return render(request, "polls/detail.html", {"uzytkownik": uzytkownik})

def vote(request, uzytkownik_id):
    uzytkownik = get_object_or_404(Uzytkownicy, pk=uzytkownik_id)
    try:
        selected_course = uzytkownik.kursy_set.get(pk=request.POST["kurs"])
    except (KeyError, Kursy.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "uzytkownik": uzytkownik,
                "error_message": "Nie wybrałeś kursu.",
            },
        )
    else:
        selected_course.votes = F("votes") + 1
        selected_course.save()
        return HttpResponseRedirect(reverse("polls:detail", args=(uzytkownik.id,)))
