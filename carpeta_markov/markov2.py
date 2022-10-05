import pandas as pd

def comparar(PAIS1, PAIS2, dataset):
    df = pd.read_csv(dataset)
    df = df.fillna(0)
    pais1 = df.loc[df['Country Name'] == PAIS1]
    pais2 = df.loc[df['Country Name'] == PAIS2]
    pais1mayor = []
    pais2mayor = []
    for i in range(4, 65):
        if float(pais1.iloc[:,i]) > float(pais2.iloc[:,i]):
            pais1mayor.append(True)
        elif float(pais1.iloc[:,i]) < float(pais2.iloc[:,i]):
            pais2mayor.append(True)
    if pais1mayor == [] and pais2mayor == []:
        porcentaje_1m = 0
    else:
        porcentaje_1m = len(pais1mayor)/((len(pais1mayor)+len(pais2mayor)))
    return round(porcentaje_1m,2)

def markov2(PAIS1, PAIS2, PAIS3):
    print("La probabilidad de que el GDP de", PAIS1, "sea mayor que el de", PAIS2, "es", comparar(PAIS1, PAIS2, 'GDP_annual_growth.csv'))
    print("La probabilidad de que el GDP de", PAIS1, "sea mayor que el de", PAIS3, "es", comparar(PAIS1, PAIS3, 'GDP_annual_growth.csv'))
    print("La probabilidad de que el GDP de", PAIS2, "sea mayor que el de", PAIS1, "es", comparar(PAIS2, PAIS1, 'GDP_annual_growth.csv'))
    print("La probabilidad de que el GDP de", PAIS2, "sea mayor que el de", PAIS3, "es", comparar(PAIS2, PAIS3, 'GDP_annual_growth.csv'))
    print("La probabilidad de que el GDP de", PAIS3, "sea mayor que el de", PAIS1, "es", comparar(PAIS3, PAIS1, 'GDP_annual_growth.csv'))
    print("La probabilidad de que el GDP de", PAIS3, "sea mayor que el de", PAIS2, "es", comparar(PAIS3, PAIS2, 'GDP_annual_growth.csv'))
    

    matriz = [[[comparar(PAIS1, PAIS1, 'GDP_annual_growth.csv')],[comparar(PAIS1, PAIS2, 'GDP_annual_growth.csv')],[comparar(PAIS1, PAIS3, 'GDP_annual_growth.csv')]],
            [[comparar(PAIS2, PAIS1, 'GDP_annual_growth.csv')],[comparar(PAIS2, PAIS2, 'GDP_annual_growth.csv')],[comparar(PAIS2, PAIS3, 'GDP_annual_growth.csv')]],
            [[comparar(PAIS3, PAIS1, 'GDP_annual_growth.csv')],[comparar(PAIS3, PAIS2, 'GDP_annual_growth.csv')],[comparar(PAIS3, PAIS3, 'GDP_annual_growth.csv')]]]

    print("Esta es la matriz")
    for i in range(0, len(matriz)):
        print(matriz[i])