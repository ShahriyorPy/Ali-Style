from django.urls import path
from .views import *

urlpatterns = [
    path('login/',LoginView.as_view()),
    path('logout/',logoutview),
    path('profil/',ProfilView.as_view()),
    path('register/',RegisterView.as_view())
]