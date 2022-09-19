from winreg import HKEY_LOCAL_MACHINE
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

a = pd.read_csv("Access_to_electricity.csv")

import array as arr

a = arr.array("b", [1,2,3])

b = arr.array("b", [2,4,5])

array1 = [1, 2, 3, 4, 4, 4, 3, 2, 1]
array2 = [1, 3, 4, 4, 2, 1]


#Funcion para calcular la distancia
def distancia(x,y):
    distancia = x-y
    if distancia < 0:
        distancia = - distancia
    else:
        pass
    return distancia

#creamos la matriz distancia




def matriz_distancia(a,b):
    
    matriz = []
    for i in range(len(b)):
        matriz.append([])
        for j in range(len(a)-1):
            matriz[i].append(None)
    
    for i in range(len(a)):
        for e in range(len(b)):
            try:
                (matriz[e])[i] = distancia(a[i],b[e])
            except:
                pass
    print(matriz)

    fig, ax =plt.subplots(1,1)
    data=matriz
    column_labels=a
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data,colLabels=column_labels, rowLabels=b,loc="center")
    
    plt.show()
    return matriz

matriz_distancia(array1, array2)

def matriz_distancia_acumulada(a,b):
    #repetimos el proceso anterior

    matriz = []
    for i in range(len(b)):
        matriz.append([])
        for j in range(len(a)-1):
            matriz[i].append(None)
    
    for i in range(len(a)):
        for e in range(len(b)):
            try:
                (matriz[e])[i] = distancia(a[i],b[e])
            except:
                pass
    print(matriz)
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

z = matriz_distancia_acumulada(array1,array2)

resultado = (z[0])[0]
posicion = (z[0])[0]
for i in range(len(b)):
    for j in range(len(a)):
        try:
            if (z[i+1])[j]<(z[i+1])[j+1] and (z[i+1])[j]<(z[i])[j+1]:
                resultado=resultado+(z[i+1])[j]
                posicion= (i+1,j)
            elif (z[i])[j+1]<(z[i+1])[j+1] and (z[i+1])[j]<(z[i+1])[j]:
                resultado=resultado+(z[i])[j+1]
                posicion = (i,j+1)
            elif (z[i+1])[j+1]<=(z[i])[j+1] and (z[i+1])[j+1]<=(z[i+1])[j]:
                resultado=resultado+(z[i+1])[j+1]
                posicion = (i+1,j+1)
            else:
                resultado=resultado+(z[i+1])[j+1]
                posicion = (i+1,j+1)
            print(resultado)
            print(posicion)
            

        except:
            pass
print(resultado)
