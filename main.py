from utils import *
tamaño = pedir_tamaño() 
tablero = crear_tablero(tamaño)    
print(f"Este es tu tablero:\n{tablero}")
print("Ahora vamos a crear tu primer barco")
lista_barco = pedir_datos_barco()
ajustar_posicion_inicial(lista_barco)
barco = crear_barco(lista_barco)
print (colocar_barco(barco, tablero))
tablero = colocar_barco(barco, tablero)
print("Vamos a por tu segundo barco, recuerda que tienes que crear 3 barcos de eslora 2, 2 barcos de eslora 3 y 1 barco de eslora 4")
lista_barco_2 = pedir_datos_barco()
ajustar_posicion_inicial(lista_barco_2)
barco_2 = crear_barco(lista_barco_2)
print (colocar_barco(barco_2,tablero))



