import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CPDB.settings")
django.setup()

from properties.models import *

f = open('pure_property.txt', 'r')
lines = f.readlines()
f.close()

for i in range(1, 619):
    
    a = lines[i].split('"')
    b = a[-1].split(',')
    del b[0]

    for j in range(len(b)):
        if b[j] != '' and b[j] != '\n':
            b[j] = float(b[j])
    
    data = [i, a[1], a[3]] + b
    
    property = Property()
    property.Formula = data[1]
    property.Name = data[2]
    property.Molwt = data[3]
    if data[4] != '':
        property.Tfp = data[4]
    if data[5] != '':
        property.Tb = data[5]
    if data[6] != '':
        property.Tc = data[6]
    if data[7] != '':
        property.Pc = data[7]
    if data[8] != '':
        property.Vc = data[8]
    if data[9] != '':
        property.Zc = data[9]
    if data[10] != '':
        property.Omega = data[10]
    if data[11] != '':
        property.Dipm = data[11]
    if data[12] != '':
        property.CpA = data[12]
    else: 
        property.CpA = 0
    if data[13] != '':
        property.CpB = data[13]
    else: 
        property.CpB = 0
    if data[14] != '':
        property.CpC = data[14]
    else: 
        property.CpC = 0
    if data[15] != '':
        property.CpD = data[15]
    else: 
        property.CpD = 0
    if data[16] != '':
        property.dHf = data[16]
    if data[17] != '':
        property.dGf = data[17]
    if data[18] != '':
        property.Eq = data[18]
    if data[19] != '':
        property.VpA = data[19]
    if data[20] != '':
        property.VpB = data[20]
    if data[21] != '':
        property.VpC = data[21]
    if data[22] != '':
        property.VpD = data[22]
    if data[23] != '':
        property.Tmin = data[23]
    if data[24] != '':
        property.Tmax = data[24]
    if data[25] != '':
        property.Lden = data[25]
    if data[26] != '' and data[26] != '\n':
        property.Tden = data[26]
    
    property.save()