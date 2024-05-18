from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Users, AboutUs


# renderuje strone głowną po zalogowaniu
@login_required
def home(request):
    return render(request, "home.html", {})


# tworzy widok strony startowej
def start_page(request):
    return render(request, "start.html")


# tworzy widok strony logowania
def login(request):
    return render(request, "login.html")


# tworzy widok strony rejestracji
def signup(request):
    return render(request, "signup.html")


# tworzy widok strony uzytkownikow z aktywnym kontem
def users(request):
    context = {"users": Users}
    return render(request, "users.html", context)


# tworzy widok strony informującej
def aboutus(request):
    context = {"aboutus": AboutUs}
    return render(request, "aboutus.html", context)

# weryfikuje formularze oraz przekierowuje na konkretne adresy URL
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
