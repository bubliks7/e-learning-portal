from django.contrib import admin
from .models import Kurs, Test, Pytanie, Odpowiedz

admin.site.register(Kurs)
admin.site.register(Test)
admin.site.register(Pytanie)
admin.site.register(Odpowiedz)