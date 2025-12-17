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
