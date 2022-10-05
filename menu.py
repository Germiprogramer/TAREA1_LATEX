import helpers
from dtw import *
from markov1 import *
from markov2 import *
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
            while True:
                helpers.limpiar_pantalla()

                print("================================================================")
                print("  Elige para que quieres usar el algoritmo de markov prefieres  ")
                print("================================================================")
                print("[1] Probabilidad de que crezca o decrezca el GDP de un pais")
                print("[2] Comparar el GDP de distintos paises")
                opcion = input("> ")

                if opcion == '1':
                    markov1(input("Elija el pais que quiera analizar: "))
                
                if opcion =='2':
                    markov2(input("Elija el primer pais: "), input("Elija el segundo pais: "), input("Elija el tercer pais: "))
                break
        break