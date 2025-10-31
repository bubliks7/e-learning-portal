from django.db import models
from portal.models import Uzytkownicy
from portal.models import Kursy
# Create your models here.

class Enrollment(models.Model):
    uzytkownik = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE, related_name="enrollment")
    kurs = models.ForeignKey(Kursy, on_delete=models.CASCADE, related_name="enrollment")
    data_dolaczenia = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('uzytkownik', 'kurs')

    def __str__(self):
        return f"{self.Uzytkownicy.imie} zapisany na {self.Kursy.tytul}"

