from django.urls import path, include
from .views import authView, home, start_page, Users, AboutUs
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("home/aboutus/", AboutUs, name="aboutus"),
    path("home/users/", Users, name="users"),
    path("start/", start_page, name="start"),
    path("home/", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL)
