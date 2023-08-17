from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.

class SavatView(View):
    def get(self, request):
        content = {
            "savatlar":Savat.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-shopping-cart.html', content)