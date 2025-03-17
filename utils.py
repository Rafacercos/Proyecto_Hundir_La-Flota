import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, '_')

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Acertaste")
        tablero[casilla] = "X"
    else:
        print("Fallaste")
        tablero[casilla]  = "A"
    return tablero

def pedir_tamaño():
    while True:
        try:
            filas = int(input("Introduce el numero de filas que deseas para tu tablero (Debe ser un número exacto)"))
            columnas = int(input("Introduce el número de columnas que deseas para tu tablero. (Recuerda que debe ser igual al numero de filas)"))
            tamaño = ((filas),(columnas))
            if filas <= 0 or columnas <= 0:
                print("El número no puede ser 0 o menor, vuelve a introducir los valores")
                continue
            if filas != columnas:
                print("Las filas y columnas deben ser el mismo número. Prueba a introducir los valores otra vez")
                continue
            return tamaño
        except:
             print("Los números deben ser enteros. Prueba a introducirlos otra vez sin decimales")

#------------------------------------------FUNCIONES USUARIO----------------------------------------------------------

def pedir_datos_barco():
    while True:
        try:
            fila = int(input("Introduce un numero del 0 al 10"))
            columna = int(input("Introduce un número del 0 al 10"))
            eslora = int(input("Selecciona tu eslora entre 2 ,3 y 4"))
            orientacion = input("Introduce una orientacion entre horizontal/vertical")
            lista_barco = [eslora,fila,columna,orientacion]
            if fila < 0 or columna < 0:
                print("El número no puede  menor que 0, vuelve a introducir los valores")
                continue
            if eslora != 2 and eslora != 3 and eslora != 4 :
                print("La eslora debe ser un valor entre 2 y 4 (Ambos incluidos)")
                continue
            if orientacion.lower() != "horizontal" and orientacion.lower() != "vertical":
                print("La orientacion solo puede ser horizontal o vertical. Introduce una de las dos palabras")
                continue
            return lista_barco
        except:
             print("Ha ocurrido un error, vuelve a introducir los valores")


def ajustar_posicion_inicial(lista_barco):
    posicion_inicial = (lista_barco[1],lista_barco[2])
    if lista_barco [3].lower()== "horizontal" and lista_barco[2] >= 6:
        posicion_inicial = (lista_barco[1], lista_barco[2] - lista_barco[0])
        return posicion_inicial
    elif lista_barco [3].lower() == "vertical" and lista_barco[1]>= 6:
        posicion_inicial = (lista_barco[1] - lista_barco[0], lista_barco[2])
        return posicion_inicial
    else:
        posicion_inicial = (lista_barco[1],lista_barco[2])
        return posicion_inicial
    
def crear_barco(lista_barco):
    posicion_inicial= ajustar_posicion_inicial(lista_barco)
    if lista_barco[0] not in [2,3,4]:
        return "Error la eslora debe ser 2, 3 o 4"
    barco =[posicion_inicial]
    for i in range(1,lista_barco[0]):
        if lista_barco[3].lower()== "horizontal":
            barco.append((barco[0][0],barco [0][1]+ i))
        elif lista_barco[3].lower() == "vertical":
            barco.append((barco[0][0] + i,barco[0][1]))
        else:
            print("Ha habido un error")
    return barco
def generacion_barcos():
    tablero = crear_tablero()
    total_barcos = 0
    while total_barcos < 6:
        lista_barco = pedir_datos_barco()
        ajustar_posicion_inicial(lista_barco)
        barco = crear_barco(lista_barco)
        colocar_barco(barco, tablero)
        tablero = colocar_barco(barco, tablero)
        print(f"Asi queda tu tablero: \n {tablero}")
        total_barcos += 1
    return tablero

#-----------------------------------------------FUNCIONES MAQUINA--------------------------------------------------------

def datos_barco_maquina():
    fila_aleatoria = random.randint(0,9)
    columna_aleatoria = random.randint(0,9)
    valores_eslora = [2,3,4]
    frecuencia = [3,2,1]
    orientacion = random.choice(["horizontal", "vertical"])
    eslora = random.choices(valores_eslora, weights = frecuencia, k=1)[0]
    lista_barco_maquina = [eslora, fila_aleatoria,columna_aleatoria,orientacion]
    return lista_barco_maquina

def ajustar_posicion_inicial_maquina(lista_barco_maquina):
    posicion_inicial_maquina = (lista_barco_maquina[1],lista_barco_maquina[2])
    if lista_barco_maquina [3].lower()== "horizontal" and lista_barco_maquina[2] >= 6:
        posicion_inicial_maquina = (lista_barco_maquina[1], lista_barco_maquina[2] - lista_barco_maquina[0])
        return posicion_inicial_maquina
    elif lista_barco_maquina [3].lower() == "vertical" and lista_barco_maquina[1]>= 6:
        posicion_inicial_maquina = (lista_barco_maquina[1] - lista_barco_maquina[0], lista_barco_maquina[2])
        return posicion_inicial_maquina
    else:
        posicion_inicial_maquina = (lista_barco_maquina[1],lista_barco_maquina[2])
        return posicion_inicial_maquina

def generacion_barcos_maquina():
    tablero_maquina = crear_tablero()
    total_barcos = 0
    while total_barcos < 6:
        lista_barco_maquina = datos_barco_maquina()
        ajustar_posicion_inicial_maquina(lista_barco_maquina)
        barco = crear_barco(lista_barco_maquina)
        colocar_barco(barco, tablero_maquina)
        tablero_maquina = colocar_barco(barco, tablero_maquina)
        total_barcos += 1
    return tablero_maquina
#--------------------------------------DISPAROS USUARIO---------------------------------------------------------------

def pedir_coordenadas():
    fila = int(input("En qué fila (0-9) quieres disparar?"))
    columna = int(input("En que columna (0-9) quieres disparar?"))
    coordenada = (fila,columna)
    return coordenada
tablero_visual = crear_tablero()
def disparar_usuario(tablero_maquina):
    coordenada = pedir_coordenadas()
    if tablero_maquina[coordenada] == "O":
        print("Acertaste")
        tablero_visual[coordenada] = "X"
        print(tablero_visual)
        resultado = "X"
    else:
        print("Fallaste")
        tablero_visual[coordenada]  = "A"
        print(tablero_visual)
        resultado = "A"
    return tablero_visual,resultado
#----------------------------------DISPAROS MAQUINA-----------------------------------------------------------
def pedir_coordenadas_maquina():
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    coordenada = (fila,columna)
    return coordenada

def disparar_maquina(tablero_usuario,tablero_maquina):
    coordenada = pedir_coordenadas_maquina()
    if tablero_usuario[coordenada] == "O":
        print("Acertaste")
        tablero_usuario[coordenada] = "X"
        print(tablero_usuario)
        return disparar_maquina(tablero_usuario,tablero_maquina),tablero_usuario
    else:
        print("Fallaste")
        tablero_usuario[coordenada]  = "A"
        print(tablero_usuario)
        return disparar_general(tablero_maquina,tablero_usuario), tablero_usuario
    
    
#------------------------------------------DISPAROS GENERAL----------------------------------------------------
def disparar_general(tablero_maquina,tablero_usuario):
    coordenada = pedir_coordenadas()
    if tablero_maquina[coordenada] == "O":
        print("Acertaste")
        tablero_visual[coordenada] = "X"
        print(tablero_visual)
        resultado = "X"
    else:
        print("Fallaste")
        tablero_visual[coordenada]  = "A"
        print(tablero_visual)
        resultado = "A"
    juego_terminado(tablero_maquina,tablero_usuario)
    if resultado == "X":
        return disparar_general(tablero_maquina,tablero_usuario)
    elif resultado == "A":
        return disparar_maquina(tablero_usuario,tablero_maquina)
    return tablero_visual,resultado


def juego_terminado(tablero_maquina,tablero_usuario):
    for fila in tablero_maquina:
        if "O" in fila:
            break
    else:
        print("¡Felicidades!¡Ganaste!")
        exit() 

    for fila in tablero_usuario:
        if "O" in fila:
            break
    else:
        print("¡Perdiste!")
        exit()

def iniciar_juego():
    tamaño = pedir_tamaño()
    tablero_usuario = crear_tablero(tamaño)
    tablero_maquina = crear_tablero(tamaño)
    tablero_visual = crear_tablero()  
    print("Crea tu flota:")
    tablero_usuario = generacion_barcos()
    print("La máquina está generando su flota...")
    tablero_maquina = generacion_barcos_maquina()
    print("\nEste es tu tablero:")
    print(tablero_usuario)
    print("\nEste es el tablero de la máquina (sin revelar barcos):")
    print(tablero_visual)
    print("Comienza a disparar")
    return tablero_usuario,tablero_maquina,tablero_visual
 