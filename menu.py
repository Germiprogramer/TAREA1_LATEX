import helpers
from dtw import *
from markov import *
import pandas as pd


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Elige que quieres ver  ")
        print("========================")
        print("[1] Algoritmo DTW ")
        print("[2] Algoritmo Cadenas de Markov ")

        opcion = input("> ")

        if opcion == '1':
            dtw(primeros_paises_primeraño, primeros_paises_ultimoaño)

        if opcion == '2':
            print("Elige un país de los siguientes: Nigeria, Spain, Kyrgyz Republic, Italy, Germany, China")

            pais = input("> ")

            if pais == "Nigeria":
                listas_concretas('Nigeria')
            
            if pais == "Spain":
                listas_concretas('Spain')

            if pais == "Kyrgyz Republic":
                listas_concretas('Kyrgyz Republic')

            if pais == "Italy":
                listas_concretas('Italy')

            if pais == "Germany":
                listas_concretas('Germany')

            if pais == "China":
                listas_concretas('China')

        break