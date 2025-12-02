from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Uzytkownicy(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=60)
    email = models.CharField(max_length=100, unique=True)
    haslo = models.CharField(max_length=255)
    status_uzytkownika = models.CharField(max_length=20)
    data_rejestracji = models.DateTimeField(auto_now_add=True)
    potwierdzony_email = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.email})"

class Kursy(models.Model):
    id = models.AutoField(primary_key=True)
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    dluzszyOpis = models.TextField(null=True, blank=True)
    tresc_kursu = models.TextField(null=True, blank=True)
    autor = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE, related_name='kursy')
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tytul

class Uprawnienia(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=50)
    opis = models.TextField()
    def __str__(self):
        return self.nazwa

class UprawnieniaUzytkownika(models.Model):
    uzytkownik = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE, related_name='uprawnienia_uzytkownika')
    uprawnienia = models.ForeignKey(Uprawnienia, on_delete=models.CASCADE, related_name='uprawnienia')

class Kursanci(models.Model):
    id = models.AutoField(primary_key=True)
    uzytkownik = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE, related_name='kursanci')
    kurs = models.ForeignKey(Kursy, on_delete=models.CASCADE, related_name='kursanci')
    postep = models.DecimalField(max_digits=5, decimal_places=2)

class Testy(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=200)
    prog_zdawalnosci = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    kurs = models.ForeignKey(Kursy, on_delete=models.CASCADE, related_name='testy')
    def __str__(self):
        return self.nazwa

class OcenyKursow(models.Model):
    id = models.AutoField(primary_key=True)
    uzytkownik = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE, related_name='oceny_kursow')
    kurs = models.ForeignKey(Kursy, on_delete=models.CASCADE, related_name='oceny_kursow')
    gwiazdki = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    komentarz = models.TextField()

class Pytania(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(Testy, on_delete=models.CASCADE, related_name='pytania')
    tresc = models.TextField()
    typ = models.CharField(max_length=50)
    punkty = models.IntegerField()

class Odpowiedzi(models.Model):
    id = models.AutoField(primary_key=True)
    pytanie = models.ForeignKey(Pytania, on_delete=models.CASCADE, related_name='odpowiedzi')
    tresc = models.TextField()
    poprawna = models.BooleanField(default=False)
