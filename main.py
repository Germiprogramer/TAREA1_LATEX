# Dynamic time warping

from string import octdigits
from winreg import HKEY_LOCAL_MACHINE
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

electricidad = pd.read_csv("Access_to_electricity.csv")
#limpieza de datos
electricidad = electricidad.fillna(0)

primer_año = list(electricidad["2010"])
ultimo_año = list(electricidad["2013"])

primeros_paises_primeraño = []
primeros_paises_ultimoaño = []

for i in range(5):
    primeros_paises_primeraño.append(primer_año[i])
for j in range(7):
    primeros_paises_ultimoaño.append(ultimo_año[j])

for i in range(len(primeros_paises_primeraño)):
    primeros_paises_primeraño[i] = round(primeros_paises_primeraño[i],2)
for i in range(len(primeros_paises_ultimoaño)):
    primeros_paises_ultimoaño[i] = round(primeros_paises_ultimoaño[i],2)


#Funcion para calcular la distancia
def distancia(x,y):
  """
  Test de distancia 
  >>> distancia(2,1)
  1
  """
  distancia = x-y
    if distancia < 0:
        distancia = - distancia
    else:
        pass
    return distancia

#creamos la matriz distancia




def matriz_distancia(a,b):
  """  
  Test de matriz_distancia
  >>> matriz_distancia(2,2)
  [,
   ,]
  """
  #elaborar la matriz
    matriz = []
    for i in range(len(b)):
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(None)
    
    for i in range(len(a)):
        for e in range(len(b)):
            try:
                (matriz[e])[i] = distancia(a[i],b[e])
            except:
                pass

    #graficar la matriz
    fig, ax =plt.subplots(1,1)
    data=matriz
    column_labels=a
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data,colLabels=column_labels, rowLabels=b,loc="center")
    
    plt.show()
    return matriz

matriz_distancia(primeros_paises_primeraño, primeros_paises_ultimoaño)

def matriz_distancia_acumulada(a,b):
    #repetimos el proceso anterior

    matriz = []
    for i in range(len(b)):
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(None)
    
    for i in range(len(a)):
        for e in range(len(b)):
            try:
                (matriz[e])[i] = distancia(a[i],b[e])
            except:
                pass
    #añadimos
    
    for i in range(len(a)):
        for e in range(len(b)):
            try:
                (matriz[e])[i+1] = (matriz[e])[i+1] + (matriz[e])[i]
            except:
                pass

    fig, ax =plt.subplots(1,1)
    data=matriz
    column_labels=a
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data,colLabels=column_labels, rowLabels=b,loc="center")
    
    plt.show()
    return matriz

def warping_path(a,b):
    z = matriz_distancia_acumulada(a,b)
    resultado = (z[0])[0]
    i=0
    j=0
    total=1
    
    while i<=(len(b)+1) or j<=(len(a)+1):
        print("El camino pasa por la posición ({},{})".format(i,j))
        try:
            if (z[i+1])[j]<(z[i+1])[j+1] and (z[i+1])[j]<(z[i])[j+1]:
                resultado=resultado+(z[i+1])[j]
                i=i+1
                j=j
                total=total+1
            elif (z[i])[j+1]<(z[i+1])[j+1] and (z[i])[j+1]<(z[i+1])[j]:
                resultado=resultado+(z[i])[j+1]
                i=i
                j=j+1
                total=total+1
            elif (z[i+1])[j+1]<=(z[i])[j+1] and (z[i+1])[j+1]<=(z[i+1])[j]:
                resultado=resultado+(z[i+1])[j+1]
                i=i+1
                j=j+1
                total=total+1
            else:
                resultado=resultado+(z[i+1])[j+1]
                i=i+1
                j=j+1
                total=total+1
        except:
            break
    else:
        pass

    if i < (len(b)-1):
        resultado=resultado+(z[i+1])[j]
        total=total+1
    if j < (len(a)-1):
        resultado=resultado+(z[i])[j+1]
        total=total+1

    distancia_entre_funciones = resultado/total
    print("La distancia entre las dos muestras de datos es {}".format(distancia_entre_funciones))

    plt.show()
  
warping_path(primeros_paises_primeraño,primeros_paises_ultimoaño)

if __name__ == "__main__":
  import doctest
  doctest.testmode()  
