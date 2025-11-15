from django.shortcuts import get_object_or_404, render
from portal.models import Testy
# Create your views here.

def test_view(request, pk):
    test = get_object_or_404(Testy, pk=pk)
    return render(request, 'tests/test_view.html', {'test': test})
