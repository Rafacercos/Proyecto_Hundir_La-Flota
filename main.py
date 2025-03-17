from utils import *
tamaño = pedir_tamaño() 
tablero = crear_tablero(tamaño)    
tablero_usuario = generacion_barcos()
print("Tu tablero ya esta ahora danos un momento para generar el tablero del oponente")
tablero_maquina = generacion_barcos_maquina()
tablero_visual = crear_tablero()
print(f"Este es tu tablero:\n {tablero_usuario} \n y este es el tablero del contrincante: \n {tablero_visual}")
disparar_general(tablero_maquina)
    

