from django.shortcuts import render, redirect
from .models import *
from django.views import View


# Create your views here.

class HomeView(View):  #/home/
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                'bolimlar':Bolim.objects.all()[:7]
            }
            return render(request, 'page-index.html',content)

class HomeLoginsizView(View):  #//
    def get(self, request):
        return render(request, 'page-index-2.html')

class BolimlarView(View):  #/bolimlar/
    def get(self, request):
        content = {
            'bolimlar': Bolim.objects.all()
        }
        return render(request, 'page-category.html',content)

class BolimMahsulotlariView(View):  #//
    def get(self, request, son):
        natija = Mahsulot.objects.filter(bolim__id = son)
        kom = request.GET.get('k')
        dav = request.GET.get('d')
        min = request.GET.get('kichik')
        max = request.GET.get('katta')
        if kom:
            natija = natija.filter(brend=kom)
        if dav:
            natija = natija.filter(davlat=dav)
        if min and max:
            natija = natija.filter(narx__gt = max,narx__lt = min)
        content = {
            'mahsulotlar': natija
        }
        return render(request, 'page-listing-grid.html',content)

class ProductDetailView(View):
    def get(self, request, pk):
        chegirma_narx = Mahsulot.objects.get(id=pk).narx - (Mahsulot.objects.get(id=pk).narx * Mahsulot.objects.get(id=pk).chegirma)/100
        content = {
            'mahsulot':Mahsulot.objects.get(id=pk),
            'chegirma_narx':chegirma_narx,
            'izohlar':Izoh.objects.filter(mahsulot__id=pk)
        }
        return render(request, 'page-detail-product.html', content)

class TanlanganView(View):
    def get(self, request):
        content = {
            'tanlanganlar':Tanlangan.objects.filter(profil__user = request.user)
        }
        return render(request, 'page-profile-wishlist.html',content)

class DelTanlanganView(View):
    def get(self, request, son):
        Tanlangan.objects.get(id=son).delete()
        return redirect('/home/tanlangan/')