# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:48:29 2021

@author: giuly

funzioni utili per misurazioni e creazione di relazioni
mettere questo file nella stessa cartella del proprio programma,
poi scrivere al suo interno
from strumenti_utili_v1 import *
"""
import numpy as np
from matplotlib import pyplot as plt


"""deviazione standard
Parametri
a: <array magico numpy> - i dati
m: scalare - la media
Restituisce
scalare
"""
def deviazione(a, m):
        t = a-m
        t**=2
        sc = np.sum(t)/(t.size-1)
        dev = np.sqrt(sc)
        return dev

"""retta
Parametri
x: <array magico numpy> - i dati
m: scalare - coefficiente angolare
q: scalare - l'intercetta'
Restituisce
<array magico>
"""
def line(x,m,q=0):
 y = m*x+q
 return y



"""crea una tabella .tex importabile tramite il comando
   \input{nomefile.tex}
Parametri
dati: array magico o lista - i dati
colonne: intero - il numero di colonne che deve avere la tabella
percorso: stringa - dove salvare il file. esepio: computed_data/tabella1.tex
template: stringa, opzionale - una stringa contenente il codice latex della tabella che
                               si vuole utilizzare. deve contenere un %d e un %s, che saranno
                               sostituiti con il numero di colonne e con i dati formattati.
                               Alternativamente, è possibile passare il nome di un template ,tra 
                               quelli definiti nella funzione. se non si passa nulla, il template
                               "semplice" verrà utilizzato
Restituisce
nulla
"""
def crea_tabella(dati, colonne, percorso, template="semplice"):
    #template per tabelle centrate, anche se molto lunghe che escono dal margine
    #richiede questo header \usepackage{graphicx}
    #https://tex.stackexchange.com/a/360788
    if(template=="centrata"):
        template = r"""
        \begin{figure}[!h]
            \makebox[1 \textwidth][c]{
                \begin{tabular}{*{%d}{c}}
                    \hline
                    \hline
                        %s
                    \hline
                    \hline
                \end{tabular}
            } 
        \end{figure}
        """
    #template per tabella semplice, utile se si vuole scrivere tutto il codice che circonda la tabella
    #dentro al documento latex
    if(template=="semplice"):
        template = r"""
        \begin{tabular}{*{%d}{c}}
            \hline
            \hline
                %s
            \hline
            \hline
        \end{tabular}
        """
    #formatta i dati
    content = ""
    for i in range(0, len(dati)):
        #se i è un multiplo di colonne, inserisci l'acapo
        if((i+1)%(colonne) == 0):
            content += r"""{} \\
            \hline
            """.format(dati[i])
        #altrimenti metti l'elemento nella stessa riga
        else:
            content += "{} & ".format(dati[i])
            if(i == len(dati)-1):
                content += r"\\"
    #crea il file
    fileOutput = template % (colonne, content)
    f = open(percorso, "w")
    f.write(fileOutput)
    f.close()




