from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# from django.contrib.auth.views import LoginView
# from .forms import loginForm

# Create your views here.
# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             login(request, form.save())
#             return redirect("/")
#     else:
#         form = UserCreationForm()
#     return render(request, "users/register.html", { "form": form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, 'users/warning.html')

# class loginForm(LoginView):
#     template = 'users/register.html'
#     authentication_form = loginForm
    