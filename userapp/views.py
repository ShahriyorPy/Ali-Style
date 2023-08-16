from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from asosiy.models import Bolim, Media, Mahsulot
from django.views import View
from django.contrib.auth import authenticate,login,logout

from userapp.models import Profil


# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request,'page-user-login.html')
    def post(self, request):
        user = authenticate(
            username = request.POST.get('u'),
            password = request.POST.get('p')
        )
        if user is not None:
            login(request, user)
            return redirect('/home/')
        return redirect('/user/login/')

def logoutview(request):
    logout(request)
    return redirect('/user/login/')

class RegisterView(View):
    def get(self, request):
        return render(request,'page-user-register.html')
    def post(self, request):
        if request.POST.get('f_password') == request.POST.get('l_password'):
            user = User.objects.create_user(
                username=request.POST.get('u_name'),
                password=request.POST.get('f_password')
            )
            Profil.objects.create(
                ism=request.POST.get('full_name'),
                jins = request.POST.get('jins'),
                shahar = request.POST.get('shahar'),
                davlat = request.POST.get('davlat'),
                user = user
            )
            return redirect('/home/')


class ProfilView(View):
    def get(self, request):
        content = {
            'profil':Profil.objects.get(user=request.user)
        }
        return render(request,'page-profile-main.html',content)