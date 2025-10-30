# from django import forms
# from django.contrib.auth.models import User
# from .models import Uzytkownicy

# class RejestracjaForm(forms.ModelForm):
#     username = forms.CharField(max_length=150, label='Nazwa użytkownika')
#     password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
#     confirm_password = forms.CharField(widget=forms.PasswordInput, label="Potwierdź hasło")
#     imie = forms.CharField(max_length=50, label='Imię')
#     nazwisko = forms.CharField(max_length=60, label='Nazwisko')
#     email = forms.EmailField(label='Email')
#     status_uzytkownika = forms.CharField(max_length=20, label="Status użytkownika")

#     class Meta:
#         model = Uzytkownicy
#         fields = ['username', 'password', 'confirm_password', 'imie', 'nazwisko', 'email', 'status_uzytkownika']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Hasła nie są takie same")
#         return cleaned_data
    
#     def save(self, commit=True):
#         user = User.objects.create_user(
#             username=self.cleaned_data['username'],
#             password=self.cleaned_data['password'],
#             first_name=self.cleaned_data['imie'],
#             last_name=self.cleaned_data['nazwisko'],
#             email=self.cleaned_data['email']
#         )
#         uzytkownik = Uzytkownicy(
#             user = user,
#             imie=self.cleaned_data['imie'],
#             nazwisko=self.cleaned_data['nazwisko'],
#             email=self.cleaned_data['email'],
#             haslo=self.cleaned_data['password'],
#             status_uzytkownika=self.cleaned_data['status_uzytkownika']
#         )
#         if commit:
#             uzytkownik.save()
#         return uzytkownik
    