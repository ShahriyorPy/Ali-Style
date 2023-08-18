from django.urls import path
from .views import *

urlpatterns = [
    path('savat/',SavatView.as_view()),
    path('savat_q/<int:son>/',MiqdorQoshView.as_view()),
    path('savat_k/<int:son>/',MiqdorKamaytirView.as_view()),
    path('del_savat/<int:son>/',SavatOchirView.as_view()),
    path('tanlangan_qosh/<int:son>/',TanlanganQoshView.as_view()),
    path('',BuyurtmaView.as_view())
]