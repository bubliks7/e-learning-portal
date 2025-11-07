from django.db import models
from portal.models import Uzytkownicy, Kursy

class Enrollment(models.Model):
    uzytkownik = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE, related_name="enrollments")
    kurs = models.ForeignKey(Kursy, on_delete=models.CASCADE, related_name="enrollments")
    data_dolaczenia = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('uzytkownik', 'kurs')

    def __str__(self):
        return f"{self.uzytkownik.imie} zapisany na {self.kurs.tytul}"

class courseContent(models.Model):
    tytul = models.CharField(max_length=100)
    rozdzial = models.CharField(max_length=20)
    tresc = models.TextField()
