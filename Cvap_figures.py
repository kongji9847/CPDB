import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CPDB.settings")
django.setup()

from properties.models import Property
import numpy as np
import matplotlib.pyplot as plt


compounds = Property.objects.all()
fig = plt.figure()
for compound in compounds:

    if compound.Tmin:
        x = np.arange(compound.Tmin, compound.Tmax + 0.1, 5)
        y = compound.CpA + compound.CpB*(x) + compound.CpC*(x**2) + compound.CpD*(x**3)

        plt.plot(x,y)
        plt.xlabel('Temperature(K)')
        plt.ylabel('Cp(J/mol*K)')
        plt.title(f'Isobaric heat capacity of {compound.Name}')
        plt.grid(True)
        plt.savefig(f"properties/static/properties/Cpfigures/{compound.Name}.png")
        plt.clf()                 # figure끼리 중첩되어 저장되므로 close 필수!
