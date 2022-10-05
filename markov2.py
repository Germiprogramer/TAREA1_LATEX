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

print("La probabilidad de que el GDP de Germany sea mayor que el de China es", comparar("Germany", "China", 'GDP_annual_growth.csv'))
print("La probabilidad de que el GDP de Germany sea mayor que el de Spain es", comparar("Germany", "Spain", 'GDP_annual_growth.csv'))
print("La probabilidad de que el GDP de China sea mayor que el de Germany es", comparar("China", "Germany", 'GDP_annual_growth.csv'))
print("La probabilidad de que el GDP de China sea mayor que el de Spain es", comparar("China", "Spain", 'GDP_annual_growth.csv'))
print("La probabilidad de que el GDP de Spain sea mayor que el de Germany es", comparar("Spain", "Germany", 'GDP_annual_growth.csv'))
print("La probabilidad de que el GDP de Spain sea mayor que el de China es", comparar("Spain", "China", 'GDP_annual_growth.csv'))

matriz = [[[comparar("Germany", "Germany", 'GDP_annual_growth.csv')],[comparar("Germany", "China", 'GDP_annual_growth.csv')],[comparar("Germany", "Spain", 'GDP_annual_growth.csv')]],
        [[comparar("China", "Germany", 'GDP_annual_growth.csv')],[comparar("China", "China", 'GDP_annual_growth.csv')],[comparar("China", "Spain", 'GDP_annual_growth.csv')]],
        [[comparar("Spain", "Germany", 'GDP_annual_growth.csv')],[comparar("Spain", "China", 'GDP_annual_growth.csv')],[comparar("Spain", "Spain", 'GDP_annual_growth.csv')]]]

print("La matriz de transición es:")
print("       Germany  China   Spain")
print("Germany", matriz[0])
print("China", matriz[1])
print("Spain", matriz[2])