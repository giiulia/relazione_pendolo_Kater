import numpy as np
from matplotlib import pyplot as plt
import dati
from sympy import *
from strumenti_utili_v2 import *


#risultati della raccolta dati
dist_mB = np.array([
    np.mean(dati.d1),
    np.mean(dati.d2),
    np.mean(dati.d3),
    np.mean(dati.d4),
    np.mean(dati.d5),
    np.mean(dati.d6)
])
print("in media, le distanze da mB dal coltello 2 sono: {}".format(dist_mB))

s_dist_mB = np.array([
    deviazione(dati.d1, np.mean(dati.d1)),
    deviazione(dati.d2, np.mean(dati.d2)),
    deviazione(dati.d3, np.mean(dati.d3)),
    deviazione(dati.d4, np.mean(dati.d4)),
    deviazione(dati.d5, np.mean(dati.d5)),
    deviazione(dati.d6, np.mean(dati.d6))
])/np.sqrt(dati.T11.size)
print("incertezze dist mB {}".format(s_dist_mB))


dist_mA = np.mean(dati.dist_mA)
print(dist_mA)
T1 = np.array([
    np.mean(dati.T11),
    np.mean(dati.T12),
    np.mean(dati.T13),
    np.mean(dati.T14),
    np.mean(dati.T15),
    np.mean(dati.T16)
])
print("le medie dei periodi relativi al primo coltello: {}".format(T1))

T2 = np.array([
    np.mean(dati.T21),
    np.mean(dati.T22),
    np.mean(dati.T23),
    np.mean(dati.T24),
    np.mean(dati.T25),
    np.mean(dati.T26)
])
print("le medie dei periodi relativi al secondo coltello: {}".format(T2))

s_T1 = np.array([
    deviazione(dati.T11, np.mean(dati.T11)),
    deviazione(dati.T12, np.mean(dati.T12)),
    deviazione(dati.T13, np.mean(dati.T13)),
    deviazione(dati.T14, np.mean(dati.T14)),
    deviazione(dati.T15, np.mean(dati.T15)),
    deviazione(dati.T16, np.mean(dati.T16))
])/np.sqrt(dati.T11.size)
print("incertezze T1 {}".format(s_T1))

s_T2 = np.array([
    deviazione(dati.T21, np.mean(dati.T21)),
    deviazione(dati.T22, np.mean(dati.T22)),
    deviazione(dati.T23, np.mean(dati.T23)),
    deviazione(dati.T24, np.mean(dati.T24)),
    deviazione(dati.T25, np.mean(dati.T25)),
    deviazione(dati.T26, np.mean(dati.T26))
])/np.sqrt(dati.T21.size)
print("incertezze T2{}".format(s_T2))

#grafico dei punti
plt.errorbar(dist_mB, T1, s_T1, fmt='o', ls='none', label='dataT1', color= "DarkSlateBlue") #parametri: array_x, array_y, errore_y, errore_x 
plt.errorbar(dist_mB, T2, s_T2, fmt='o', ls='none', label='dataT2', color= "Coral") 

plt.scatter(dist_mB, T1)
plt.plot(dist_mB, T1, color= "CornflowerBlue")

plt.scatter(dist_mB, T2)
plt.plot(dist_mB, T2, color= "SandyBrown")

plt.xlim(0.0, 1.0)
plt.ylim(1.8, 2.2)


plt.xlabel('distanza di mB dal coltello2 (m)', fontsize=15)
plt.ylabel('periodo di oscillazione (s)', fontsize=15) 

plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/punti.png')
plt.show()

#calcolo g e sigma g
T = ( (T2[3]*T1[4]) - (T1[3]*T2[4]) )/(T1[4]-T2[4]-T1[3]+T2[3])
g = 4*np.power(np.pi, 2)*0.994/np.power(T, 2)

_T23, _T24, _T13, _T14 = symbols('_T23 _T24 _T13 _T14', real=True) #raggio sferette
formula_funzione = ( (_T23*_T14) - (_T13*_T24) )/( _T14 - _T24 - _T13 + _T23 )

#genera uno scalare a partire dalla formula simbolica scritta sopra
def genera_derivata(incognita):
    formula_derivata = diff(formula_funzione, incognita)
    derivata = formula_derivata.subs([(_T23, T2[3]), (_T24, T2[4]), (_T13, T1[3]), (_T14, T1[4])])
    return derivata

derivata_T23 = genera_derivata(_T23)
derivata_T24 = genera_derivata(_T24)
derivata_T13 = genera_derivata(_T13)
derivata_T14 = genera_derivata(_T14)

#sigma_T = np.sqrt(s_T2[3]**2 + s_T2[4]**2 + s_T1[3]**2 + s_T1[4]**2)
sigma_T = np.power(derivata_T23*s_T2[3], 2)+ np.power(derivata_T24*s_T2[4], 2) + np.power(derivata_T13*s_T1[3], 2) + np.power(derivata_T14*s_T1[4], 2)
sigma_T = np.array(sigma_T, dtype=np.float64) 
sigma_T = np.sqrt(sigma_T)
print(sigma_T)


_T= symbols('_T', real=True) #raggio sferette
formula_funzione2 = 4*np.power(np.pi, 2)*0.994/np.power(_T, 2)

#genera uno scalare a partire dalla formula simbolica scritta sopra
def genera_derivata(incognita):
    formula_derivata = diff(formula_funzione2, incognita)
    print(formula_derivata)
    derivata = formula_derivata.subs([(_T, T)])
    return derivata

derivata_T = genera_derivata(_T)
sigma_g = derivata_T*sigma_T

print("accelerazione di gravita: {}±{}".format(g, sigma_g))

#approssimazione angolo infinitesimo
_T, _teta= symbols('_T _teta', real=True) #raggio sferette
formula_funzione2 = 4*np.power(np.pi, 2)*0.994*np.power(1+(_teta**2/16), 2)/np.power(_T, 2)

#genera uno scalare a partire dalla formula simbolica scritta sopra
teta = np.arcsin(dati.b/dati.a)
sigma_teta = 0.0008 #rad
print(teta)
def genera_derivata(incognita):
    formula_derivata = diff(formula_funzione2, incognita)
    print(formula_derivata)
    derivata = formula_derivata.subs([(_T, T), (_teta, teta)])
    return derivata

derivata_T = genera_derivata(_T)
derivata_teta = genera_derivata(_teta)

sigma_g = np.power(derivata_T*sigma_T, 2)+np.power(derivata_teta*sigma_teta, 2)
sigma_g = np.array(sigma_g, dtype=np.float64) 
sigma_g_casuale = np.sqrt(sigma_g)
print(sigma_g_casuale)

g_nuova = 4*np.power(np.pi, 2)*0.994*((1+(np.power(teta, 2)/16))**2) / (T**2)
g_precisissima = 4*np.power(np.pi, 2)*0.994*((1+(np.power(teta, 2)/16)+(9*np.power(teta, 4)/1024)+(25*np.power(teta, 6)/16384))**2) / (T**2)
Errore_sist = g_precisissima-g_nuova #su g nuova
print("l'errore sistematico sulla g nuova è: {}".format(Errore_sist))

sigma_g_tot = sigma_g_casuale**2 + Errore_sist**2
sigma_g_tot= np.sqrt(sigma_g_tot)
print("accelerazione di gravita NUOVA: {}±{}".format(g_nuova, sigma_g_tot))

#=======================    generazione tabelle   =======================

#tabelle distanze
crea_tabella(dati.d6, 6, "computed_data/tableDistances.tex")

#tabelle periodo 1
crea_tabella(dati.T11, 11, "computed_data/tablePeriod11.tex")
crea_tabella(dati.T12, 11, "computed_data/tablePeriod12.tex")
crea_tabella(dati.T13, 11, "computed_data/tablePeriod13.tex")
crea_tabella(dati.T14, 11, "computed_data/tablePeriod14.tex")
crea_tabella(dati.T15, 11, "computed_data/tablePeriod15.tex")
crea_tabella(dati.T16, 11, "computed_data/tablePeriod16.tex")

#tabelle periodo 2
crea_tabella(dati.T21, 11, "computed_data/tablePeriod21.tex")
crea_tabella(dati.T22, 11, "computed_data/tablePeriod22.tex")
crea_tabella(dati.T23, 11, "computed_data/tablePeriod23.tex")
crea_tabella(dati.T24, 11, "computed_data/tablePeriod24.tex")
crea_tabella(dati.T25, 11, "computed_data/tablePeriod25.tex")
crea_tabella(dati.T26, 11, "computed_data/tablePeriod26.tex")
