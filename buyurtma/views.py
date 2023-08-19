from django.shortcuts import render, redirect
from django.views import View

from .models import *
from asosiy.models import Mahsulot, Tanlangan

from userapp.models import Profil


# Create your views here.

class SavatView(View):
    def get(self, request):
        natija = Savat.objects.filter(profil__user=request.user, arxivda = False)
        s = 0
        chegirma = 0
        for savat in natija:
            s += savat.mahsulot.narx * savat.miqdor
            t = (1-(savat.mahsulot.chegirma/100))*savat.mahsulot.narx*savat.miqdor
            chegirma+=t
        content = {
            "savatlar":natija,
            "sum":s,
            "chg":s-chegirma,
            "yakuniy":chegirma
        }
        return render(request, 'page-shopping-cart.html', content)

class MiqdorQoshView(View):
    def get(self, request, son):
        savat = Savat.objects.get(id=son)
        savat.miqdor+=1
        savat.save()
        return redirect('/buyurtma/savat/')

class MiqdorKamaytirView(View):
    def get(self, request, son):
        savat = Savat.objects.get(id=son)
        if savat.miqdor!=1:
            savat.miqdor-=1
        savat.save()
        return redirect('/buyurtma/savat/')


class BuyurtmaView(View):
    def get(self, request):
        content = {
            'buyurtmalar':Buyurtma.objects.filter(profil__user=request.user)
        }
        return render(request,'page-profile-orders.html',content)

class SavatOchirView(View):
    def get(self, request, son):
        Savat.objects.get(id=son).delete()
        return redirect('/buyurtma/savat/')

class TanlanganQoshView(View):
    def get(self,request, son):
        Tanlangan.objects.create(
            profil = Profil.objects.get(user=request.user),
            mahsulot = Mahsulot.objects.get(id=son)
        )
        return redirect('/home/tanlangan/')

class BuyurtmaQoshishView(View):
    def get(self, request):
        savatlari = Savat.objects.filter(profil__user=request.user,arxivda=False)
        buyurtma = Buyurtma.objects.create(
            manzil = "Shahrixon shahar,Gumbaz ko'chasi",
            zipcode = "1233212",
            profil = Profil.objects.get(user=request.user),
            summa=1200
        )
        s = 0
        for savat in savatlari:
            buyurtma.savatlar.add(savat)
            s+=savat.umumiy_summa
            savat.arxivda = True
            savat.save()
        buyurtma.summa=s
        buyurtma.save()
        return redirect('/buyurtma/')