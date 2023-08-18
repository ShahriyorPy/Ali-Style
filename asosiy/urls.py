from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view()),
    path('bolimlar/',BolimlarView.as_view()),
    path('bolim/<int:son>/',BolimMahsulotlariView.as_view()),
    path('tanlangan/',TanlanganView.as_view()),
    path('del_tanlangan/<int:son>/',DelTanlanganView.as_view()),
    path('product/<int:pk>/',ProductDetailView.as_view())
]