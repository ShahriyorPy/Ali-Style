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

    def save(self, *args,**kwargs):
        self.umumiy_summa = int(self.miqdor) * float(self.mahsulot.narx)
        super(Savat, self).save(*args, **kwargs)


    def __str__(self):
        return f"Savat - {self.profil.ism}:{self.mahsulot.nom}"

