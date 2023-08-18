from django.db import models
from django.db.models.functions import datetime

from userapp.models import Profil
from asosiy.models import Mahsulot


# Create your models here.

class Savat(models.Model):
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, null=True)
    miqdor = models.PositiveSmallIntegerField()
    umumiy_summa = models.FloatField()
    vaqt = models.DateTimeField(default=datetime.datetime.now())
    arxivda = models.BooleanField(default=False)

    def save(self, *args,**kwargs):
        narxi =(1 - (self.mahsulot.chegirma/100))*self.mahsulot.narx
        self.umumiy_summa = int(self.miqdor) * float(narxi)
        super(Savat, self).save(*args, **kwargs)


    def __str__(self):
        return f"Savat - {self.profil.ism}:{self.mahsulot.nom}"

class Buyurtma(models.Model):
    savatlar = models.ManyToManyField(Savat)
    sana = models.DateField(auto_now_add=True)
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)
    manzil = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=7)
    summa = models.IntegerField()

    # def save(self, *args,**kwargs):
    #     s = 0
    #     for savat in self.savatlar.all():
    #         s+=savat.umumiy_summa
    #     self.summa = s
    #     super(Buyurtma, self).save(*args, **kwargs)


    def __str__(self):
        return f"Buyurtma - {self.profil.ism}dan"