from django.db import models
from django.forms import ImageField
from django_matplotlib import MatplotlibFigureField

# Create your models here.
class Property(models.Model):
    Formula = models.CharField(max_length=20)
    Name = models.CharField(max_length=30)
    Molwt = models.FloatField(null = True)
    Tfp = models.FloatField(null = True)
    Tb = models.FloatField(null = True)
    Tc = models.FloatField(null = True)
    Pc = models.FloatField(null = True)
    Vc = models.FloatField(null = True)
    Zc = models.FloatField(null = True)
    Omega = models.FloatField(null = True)
    Dipm = models.FloatField(null = True)
    CpA = models.FloatField(null = True)
    CpB = models.FloatField(null = True)
    CpC = models.FloatField(null = True)
    CpD = models.FloatField(null = True)
    dHf = models.FloatField(null = True)
    dGf = models.FloatField(null = True)
    Eq = models.IntegerField(null = True)
    VpA = models.FloatField(null = True)
    VpB = models.FloatField(null = True)
    VpC = models.FloatField(null = True)
    VpD = models.FloatField(null = True)
    Tmin = models.FloatField(null = True)
    Tmax = models.FloatField(null = True)
    Lden = models.FloatField(null = True)
    Tden = models.FloatField(null = True)