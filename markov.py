import pandas as pd

def markov(PAIS):
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