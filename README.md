# TAREA1_LATEX

Miembros del grupo: Germán Llorente, Gonzalo Martínez, Carlos Puigserver, Álex Muñoz

El link al repositorio es el siguiente: https://github.com/Germiprogramer/TAREA1_LATEX.git

# INDUSTRIA 4.0

En la actualidad, el mundo se encuentra en el inicio de la "Cuarta Revolución Industrial", también llamada Industria 4.0. Esta revolución esta especialmente marcada por la digitalización de los entornos económicos, laborales, etc. ; dándose la aparación de nuevas tecnologías como la robotica, la analítica, la inteligencia artificial, las tecnologías cognitivas, la nanotecnología o el Internet of Things (IoT). La existencia de acceso a comunicación en tiempo real transforma el modo de llevar los negocios, tratando las empresas de invertir en las tecnologías que mayor ventaja les den de cara al resto.

# Como relacionamos nuestro trabajo con la Industria 4.0

Tal y como se ha explicado anteriormente, estamos hablando de un aumento masivo de la digitalización. Para ello, es clave el uso de distintos dispositivos electrónicos que nos permitan conectarnos a la nube. Pese a que en los países más desarrollados podemos decir que estamos adaptados a las tecnologías eléctricas, otros territorios menos afortunados todavía están en un proceso de descubrimiento de estas herramientas. Por ello, queremos enfocar nuestro trabajo de cara al aumento del uso de la electricidad en los distintos países del mundo.

![1990](https://user-images.githubusercontent.com/91720991/190913648-11d2a935-a271-45bf-a212-5f591e010ea1.png)

![2018](https://user-images.githubusercontent.com/91720991/190913659-b4a6e9f7-937e-4784-a929-68fadb5230ad.png)

Los gráficos mostrados representan el primer año y el último año registrado en nuestro dataset. A primera vista, se ve como en una diferencia de 28 años, el número de países en los que prácticamente todos los habitantes tienen electricidad (un porcentaje de 90% o más) ha subido a más del doble.

# Algoritmo Dynamic Time Warping

Uno de los algoritmos a desarrollar en este trabajo es el "Dynamic Time Warping", "Deformación Dinámica del Tiempo" traducido al español. Este algoritmo se usa para medir la similitud de dos muestras de distinto tiempo, sin importar que estas tengan un número distinto de elementos.

Para mostrar el funcionamiento del algoritmo, compararemos los datos de los 5 primeros países del dataset en 2010, y los 7 primeros de 2013. Tendría más sentido pillar los mismos países, pero como queremos mostrar que el DTW funciona para muestras de distinto número de elementos, añadimos dos países más al año 2013. No podemos usar el dataset entero porque se crashea el programa.

Para empezar a programar el algoritmo, es preciso definir una distancia entre dos puntos. Nosotros usaremos la distancia euclídea.

    def distancia(x,y):
        distancia = x-y
        if distancia < 0:
            distancia = - distancia
        else:
            pass
        return distancia
        
En base a dicha distancia, lo siguiente que se hará es calcular la distancia de cada uno de los elementos del primer grupo con cada uno de los del segundo grupo. Todo ello lo expondremos en una tabla, dado que esta será importante más adelante para elaborar el "Warping Path". Para crear la tabla se ha utilizado la función distancia anteriormente definida y bucles for, mientras que para graficarla hemos usado la librería matplotlib.

    def matriz_distancia(a,b):
        #elaborar la matriz
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

        #graficar la matriz
        fig, ax =plt.subplots(1,1)
        data=matriz
        column_labels=a
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=data,colLabels=column_labels, rowLabels=b,loc="center")

        plt.show()
        return matriz
        
![dtw 1](https://user-images.githubusercontent.com/91720991/191383080-83e6bb15-0a33-46eb-9f02-1c84e9a24d72.png)
 
 El siguiente paso es calcular la matriz de distancia acumulada, que será a partir de la cual realicemos el "Warping Path", para ello reutilizaremos el código de la función anterior, y después usaremos otro bucle for para que se vaya sumando el elemento anterior de cada fila al siguiente. 
 
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
            
![dtw 2](https://user-images.githubusercontent.com/91720991/191382981-b729afd6-143a-434b-aa18-da355ed346da.png)

Ahora viene la parte interesante del algoritmo. Hasta ahora nos hemos dedicado a graficar tablas, y ahora debemos usar esas mismas tablas para calcular la "distancia" entre las dos distribuciones. El objetivo es crear un camino que nos lleve desde la posición de arriba a las izquierda de la tabla a la de abajo a la derecha. A este camino lo llamaremos "Warping Path". La condición es que solo podremos movernos como si fuesemos el rey de un tablero de ajedrez, con total libertad de dirección pero únicamente pudiendo desplazarnos una casilla. Entendiendo que la posición de arriba a la izquierda es la (0,0), las posiciones a las que nos podemos mover son la (1,0), (0,1) o la (1,1). En definitiva, para cualquier par (i,j), las casillas a desplazarse serán (i+1,j), (i,j+1) y (i+1,j+1). De estas, elegiremos aquella que tenga el menor valor, y así hasta llegar a la casilla final. Además, crearemos una variable resultado, a la cual le sumaremos los valores de las casillas por las que pasemos. Dividiendo el resultado entre el número de casillas obtendremos la distancia.

        def warping_path(a,b):
            z = matriz_distancia_acumulada(a,b)
            resultado = (z[0])[0]
            i=0
            j=0
            total=1

            while i<=(len(array2)+1) or j<=(len(array1)+1):
                print((i,j))
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

A la hora de interpretar los resultados, lo más importante a tener en cuenta es la relación entre la distancia y la semejanza entre ambas muestras. A mayor distancia, menos se parecen las dos listas de datos; por lo que se ha cumplido el objetivo del algoritmo: analizar la semejanza entre dos muestras.

# Modelos ocultos de Markov

Para complementar los puntos 4 y 5, decidimos elegir un dataset en el que aparecía el producto interior bruto (GDP) de cada país desde el 1960 hasta el 2020. De esta manera podemos realizar un estudio a través de las cadenas de Markov, para ver cuando crecía y decrecia el GDP de cada país.

En primer lugar, creamos una función que creaba una lista en la que poníamos "c" o "d" dependiendo de si crecía o decrecía, y luego otra función que contaba las veces que crecía o decrecía después de cada una, es decir, por cada "c" que hubiera en la lista mirábamos si la siguiente era otra "c" o una "d", y lo mismo para las "d", de esta forma creábamos una lista para lo inmedietamente posterior al crecimiento y otra para lo inmediatamente posterior al decrecimiento. Así sólo teníamos que contar el número de "c" y "d" que había en cada lista y teníamos una aproximación de como iba a evolucionar dependiendo de si había crecido o no.

El código de esto es:
```
import pandas as pd

#creamos una lista que apunte el crecimiento y decrecimiento de cada pais
def lista_total(PAIS):
    df = pd.read_csv('GDP_annual_growth.csv')
    df = df.fillna(0)
    pais = df.loc[df['Country Name'] == PAIS]
    evolucion = []
    for i in range(4,65):
        estado_actual = float(pais.iloc[:,i])
        if i < 65:
            estado_siguiente = float(pais.iloc[:, i+1])
            if estado_actual != 0 and estado_siguiente != 0:
                if estado_actual > estado_siguiente:
                    evolucion.append('d')
                elif estado_actual < estado_siguiente:
                    evolucion.append('c')
    return(evolucion)
    
#creamos lista_c y lista_d para ver que ocurre inmediatamente después de que crezca o decrezca respectivamente
def listas_concretas(PAIS):
    pais = lista_total(PAIS)
    lista_c = []
    lista_d = []

    for i in range(0,len(pais)):
        if i < len(pais)-1:
            if pais[i] == 'c':
                lista_c.append(pais[i+1])
            elif pais[i] == 'd':
                lista_d.append(pais[i+1])

    c_en_c = lista_c.count('c')
    d_en_d = lista_d.count('d')

    print("Cuando el GDP de", PAIS, "crece, hay un", round((c_en_c/len(lista_c)) * 100, 2), "% de que crezca otra vez, y un", round(100 - (c_en_c/len(lista_c)) * 100, 2), "% de que decrezca")
    print("Cuando el GDP de", PAIS, "decrece, hay un", round((d_en_d/len(lista_c)) * 100, 2), "% de que decrezca otra vez, y un", round(100 - (d_en_d/len(lista_c)) * 100, 2), "% de que crezca")

listas_concretas('Nigeria')
listas_concretas('Spain')
listas_concretas('Kyrgyz Republic')
listas_concretas('Italy')
listas_concretas('Germany')
listas_concretas('China')
```

Una vez hecho esto, creamos unos gráficos en los que aparecían las cadenas de Markov de algunos paises.

## Nigeria
![nigeria](https://user-images.githubusercontent.com/91721237/191485672-d6375630-4777-4c96-acf9-d8cb22de222b.png)

## Spain


## Kyrgyz Republic
![Kyrgyz Republic](https://user-images.githubusercontent.com/91721237/191485681-7e6bdc47-abd4-4e63-99b7-7fcc9ff20c44.png)

## Italy
![italy](https://user-images.githubusercontent.com/91721237/191485684-32e7f66d-b795-4e34-a4f2-8660f752d3e2.png)

## Germany
![germany](https://user-images.githubusercontent.com/91721237/191485686-e151b9b6-82f9-4e15-bf57-f69f85c8672a.png)

## China
![china](https://user-images.githubusercontent.com/91721237/191485687-096063b2-6b80-430d-811d-2e66f24cf88b.png)
