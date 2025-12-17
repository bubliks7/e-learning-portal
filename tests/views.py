from django.shortcuts import get_object_or_404, render
from portal.models import Testy, Pytania, Odpowiedzi
# Create your views here.

def test_view(request, pk):
    test = get_object_or_404(Testy, pk=pk)

    pytania = Pytania.objects.filter(test=test).prefetch_related('odpowiedzi')

    if not pytania.exists():
        return render(request, 'tests/test_view.html', {
            'test': test,
            'error': 'Brak pytań w teście'
        })

    return render(request, 'tests/test_view.html', {
        'test': test,
        'pytania': pytania,
        })

def test_result(request, pk):
    test = get_object_or_404(Testy, pk=pk)
    pytania = Pytania.objects.filter(test=test).prefetch_related('odpowiedzi')

    wszystkie = 0
    poprawne = 0

    for pytanie in pytania:
        odp = pytanie.odpowiedzi.all()
        wszystkie += odp.count()
        poprawne += odp.filter(poprawna=True).count()

    procent = round((poprawne / wszystkie) * 100, 2) if wszystkie > 0 else 0
    zaliczony = procent >= 50

    return render(request, 'tests/test_result.html', {
        'test': test,
        'wszystkie': wszystkie,
        'poprawne': poprawne,
        'procent': procent,
        'zaliczony': zaliczony,
    })