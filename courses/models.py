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

class coursesContent(models.Model):
    tytul_1 = models.CharField(max_length=100, null=True, blank=True)
    tytul_2 = models.CharField(max_length=100, null=True, blank=True)
    tytul_3 = models.CharField(max_length=100, null=True, blank=True)
    tytul_4 = models.CharField(max_length=100, null=True, blank=True)
    rozdzial_1 = models.CharField(max_length=25, null=True, blank=True)
    rozdzial_2 = models.CharField(max_length=25, null=True, blank=True)
    rozdzial_3 = models.CharField(max_length=25, null=True, blank=True)
    rozdzial_4 = models.CharField(max_length=25, null=True, blank=True)
    strona_1 = models.TextField()
    strona_2 = models.TextField()
    strona_3 = models.TextField()
    strona_4 = models.TextField()
