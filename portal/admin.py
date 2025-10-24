from django.contrib import admin
from .models import Kursy, Testy, Pytania, Odpowiedzi, Uzytkownicy

admin.site.register(Kursy)
admin.site.register(Testy)
admin.site.register(Pytania)
admin.site.register(Odpowiedzi)
admin.site.register(Uzytkownicy)
