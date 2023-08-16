from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.

class SavatView(View):
    def get(self, request):
        return render(request, 'page-shopping-cart.html')