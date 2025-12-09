from django.shortcuts import get_object_or_404, render
from portal.models import Testy, Pytania, Odpowiedzi
# Create your views here.

def test_view(request, pk):
    test = get_object_or_404(Testy, pk=pk)
    pytanie = get_object_or_404(Pytania, pk=pk)
    odpowiedz = get_object_or_404(Odpowiedzi, pk=pk)
    return render(request, 'tests/test_view.html', {
        'test': test,
        'pytanie': pytanie,
        'odpowiedz': odpowiedz,
        })
