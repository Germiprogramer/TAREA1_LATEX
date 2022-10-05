import helpers
from carpeta_dtw.dtw import *
from carpeta_markov.markov1 import *
from carpeta_markov.markov2 import *

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
            dtw(str(input("Elija el primer año: ")), str(input("Elija el segundo año: ")))

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