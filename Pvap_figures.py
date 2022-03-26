import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CPDB.settings")
django.setup()

from properties.models import Property
import numpy as np
import matplotlib.pyplot as plt
from math import*
from scipy.linalg import *
from scipy.optimize import fsolve

compounds = Property.objects.all()
fig = plt.figure()
for compound in compounds:
    if compound.Tmin:
        x = np.arange(compound.Tmin, compound.Tmax + 0.1, 5)
        if compound.Eq == 3:
            Y = np.exp(compound.VpA - compound.VpB/(x+compound.VpC))
            plt.plot(x, Y)
            plt.xlabel('Temperaute(K)')
            plt.ylabel('Pvap(bar)')
            plt.title(f'Vapor pressure of {compound.Name}')
            plt.grid(True)
            plt.savefig(f"properties/static/properties/Pvapfigures/{compound.Name}")
            plt.clf()
            #plt.close()
    
        elif compound.Eq == 2:
            result = []
            for n in x:
                def f(y):
                    return log(y)-compound.VpA + compound.VpB/n - compound.VpC*log(n) - compound.VpD*y/(n**2)
                y = fsolve(f, 0.000000000001)
                result.append(y.tolist())
            plt.plot(x, result)
            plt.xlabel('Temperaute(K)')
            plt.ylabel('Pvap(bar)')
            plt.title(f'Vapor pressure of {compound.Name}')
            plt.grid(True)
            plt.savefig(f"properties/static/properties/Pvapfigures/{compound.Name}")
            plt.clf()
        #     plt.close()

        elif compound.Eq == 1:
            z=(compound.VpA*(1-x/compound.Tc) + compound.VpB*(1-x/compound.Tc)**(3/2) + compound.VpC*(1-x/compound.Tc)**3 + compound.VpD*(1-x/compound.Tc)**6)/(1-(1-x/compound.Tc))
            q=compound.Pc*(np.exp(z))
            plt.plot(x,q)
            plt.xlabel('Temperature(K)')
            plt.ylabel('Pvap(bar)')
            plt.title(f'Vapor pressure of {compound.Name}')
            plt.grid(True)
            plt.savefig(f"properties/static/properties/Pvapfigures/{compound.Name}")
            plt.clf()
            #plt.close()