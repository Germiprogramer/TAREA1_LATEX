import matplotlib.pyplot as plt
import pandas as pd

a = pd.read_csv("Access_to_electricity.csv")

b = a[["Country Name", "1990"]]
c = a[["Country Name", "2018"]]

def grafico(dataset, tipo_grafico, titulografico, nombregrafico):
    fig, ax = plt.subplots()
 
    dataset.plot(kind=tipo_grafico, ax = ax, color = "green")
    ax.set_title(str(titulografico), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:orange'})
    ax.set_xlabel("Porcentaje de usuarios de electricidad", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel('Número de países')

    plt.savefig('{}.png'.format(nombregrafico), bbox_inches='tight')

    plt.show()

grafico(b, "hist", "Porcentaje Electricidad 1990", "1990")

grafico(c, "hist", "Porcentaje Electricidad 2018", "2018")