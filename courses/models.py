from django.db import models
from portal.models import Uzytkownicy
# Create your models here.

class Kursy(models.Model):
    id = models.AutoField(primary_key=True)
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    autor = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE, related_name='kursy')
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tytul
    
class Enrollment(models.Model):
    uzytkownik = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE, related_name="enrollment")
    kurs = models.ForeignKey(Kursy, on_delete=models.CASCADE, related_name="enrollment")
    data_dolaczenia = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('uzytkownik', 'kurs')

    def __str__(self):
        return f"{self.Uzytkownicy.imie} zapisany na {self.Kursy.tytul}"

