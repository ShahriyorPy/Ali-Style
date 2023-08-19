from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profil(models.Model):
    ism = models.CharField(max_length=50,null=True)
    jins = models.CharField(max_length=50)
    email = models.CharField(max_length=20,null=True)
    tel = models.CharField(max_length=30, null=True)
    shahar = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50)
    uy_manzili = models.CharField(max_length=50,null=True)
    rasm = models.FileField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.ism