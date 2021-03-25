import numpy as np
from matplotlib import pyplot as plt
import dati
from strumenti_utili_v2 import *


#risultati della raccolta dati
dist_mB = np.array([
    np.mean(dati.d3),
    np.mean(dati.d2),
    np.mean(dati.d1),
    np.mean(dati.d4),
    np.mean(dati.d5),
    np.mean(dati.d6)
])
print("in media, le distanze da mB al centro sono: {}".format(dist_mB))

dist_mA = np.mean(dati.dist_mA)

T1 = np.array([
    np.mean(dati.T13),
    np.mean(dati.T12),
    np.mean(dati.T11),
    np.mean(dati.T14),
    np.mean(dati.T15),
    np.mean(dati.T16)
])
print("le medie dei periodi relativi al primo coltello: {}".format(T1))


T2 = np.array([
    np.mean(dati.T23),
    np.mean(dati.T22),
    np.mean(dati.T21),
    np.mean(dati.T24),
    np.mean(dati.T25),
    np.mean(dati.T26)
])
print("le medie dei periodi relativi al secondo coltello: {}".format(T2))

s_T1 = np.array([
    deviazione(dati.T13, np.mean(dati.T13)),
    deviazione(dati.T12, np.mean(dati.T12)),
    deviazione(dati.T11, np.mean(dati.T11)),
    deviazione(dati.T14, np.mean(dati.T14)),
    deviazione(dati.T15, np.mean(dati.T15)),
    deviazione(dati.T16, np.mean(dati.T16))
])/np.sqrt(dati.T11.size)

s_T2 = np.array([
    deviazione(dati.T23, np.mean(dati.T23)),
    deviazione(dati.T22, np.mean(dati.T22)),
    deviazione(dati.T21, np.mean(dati.T21)),
    deviazione(dati.T24, np.mean(dati.T24)),
    deviazione(dati.T25, np.mean(dati.T25)),
    deviazione(dati.T26, np.mean(dati.T26))
])/np.sqrt(dati.T21.size)

#grafico dei punti
plt.errorbar(dist_mB, T1, s_T1, fmt='o', ls='none', label='dataT1', color= "DarkSlateBlue") #parametri: array_x, array_y, errore_y, errore_x 
plt.errorbar(dist_mB, T2, s_T2, fmt='o', ls='none', label='dataT2', color= "Coral") 

plt.scatter(dist_mB, T1)
plt.plot(dist_mB, T1)

plt.scatter(dist_mB, T2)
plt.plot(dist_mB, T2)

plt.xlim(0.15, 0.5)
plt.ylim(1.7, 2.2)


plt.xlabel('distanza di mB dal centro (m)')
plt.ylabel('periodo di oscillazione (s)') 

plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/punti.png')
plt.show()
