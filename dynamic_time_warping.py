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
matriz = []
for i in range(len(array2)):
    matriz.append([])
    for j in range(len(array1)-1):
        matriz[i].append(None)

for i in range(len(array1)):
    for e in range(len(array2)):
        try:
            (matriz[e])[i] = distancia(array1[i],array2[e])
        except:
            pass

print(matriz)
def matriz_distancia(a,b):
    fig, ax =plt.subplots(1,1)
    data=matriz
    column_labels=a
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data,colLabels=column_labels, rowLabels=b,loc="center")
    
    plt.show()

matriz_distancia(array1, array2)