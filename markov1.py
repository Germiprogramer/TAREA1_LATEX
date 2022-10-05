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

def markov1(PAIS):
    listas_concretas(PAIS)