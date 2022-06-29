import numpy as np
import random as rd
from tools.constanta import *

#Fungsi cek jarak antar mpbil
def jarak_mobil(mobil):
    if (mobil == N-1):
        if(arr_mobil[mobil].xcor() > arr_mobil[0].xcor()):
           jarak = abs(M - (arr_mobil[mobil].xcor() - arr_mobil[0].xcor()))
        else:
            jarak = abs(arr_mobil[0].xcor() - arr_mobil[mobil].xcor())
    else:
        if (arr_mobil[mobil].xcor() < arr_mobil[mobil+1].xcor()):
            jarak = abs(arr_mobil[mobil+1].xcor() - arr_mobil[mobil].xcor())
        else:
            jarak = abs(M - (arr_mobil[mobil+1].xcor() - arr_mobil[mobil].xcor()))
    return jarak


def update_kecepatan(mobil):
    v[mobil] = min(v[mobil]+N, vmax)
    jarak = jarak_mobil(mobil)
    v[mobil] = min(v[mobil], jarak-N)
    x = np.random.uniform(0, 1)
    if (x >= p):
        v[mobil] = max(0, v[mobil]-N)
    return v[mobil]
