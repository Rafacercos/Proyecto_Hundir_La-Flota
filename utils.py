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

def crear_barco_aleatorio(eslora):
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    orientacion = random.choice(["Horizontal", "Vertical"])
    if orientacion == "Horizontal":
        columna = random.randint (0,9 - eslora)
        fila = random.randint(0,9)
    elif orientacion == "Vertical" :
        fila = random.randint (0,9 - eslora)
        columna = random.randint(0,9)
    barco_aleatorio = [(fila, columna)]
    while len(barco_aleatorio) < eslora:
        if orientacion == "Horizontal":
            columna = columna + 1
            barco_aleatorio.append((fila, columna))
        else:
            fila = fila + 1
            barco_aleatorio.append((fila, columna))
    return barco_aleatorio

def crear_lista_barcos(lista_esloras=[2,2,2,3,3,4]):
    lista_barcos = []
    for i in lista_esloras:
        lista_barcos.append(crear_barco_aleatorio(i))
    return lista_barcos

def colocar_barcos_random(tablero):
    lista_barcos=crear_lista_barcos()
    for barco in lista_barcos:
        colocar_barco(barco,tablero)
    return(tablero)

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

def elegir_posicion(tablero):
    while True:
        try:
            colocar_barcos_random(tablero)
            print(tablero)
            mensaje= input("¿Te gusta como están colocados tus barcos?, recuerda que no pueden superponerse, si es asi escribe `no´")
            if mensaje.lower() == "no":
                limpiar_tablero(tablero)
                print("Ahora recolocamos tus barcos")
                continue
            elif mensaje.lower() == "si":
                print("La colocación de tus barcos es:")
                print (tablero)
                return tablero
            else:
                print("respuesta no valida. Responde Si o No")
        except Exception as e:
            print ("ha habido un error, vuelve a generar tus barcos")


def limpiar_tablero(tablero):
    for i in range(len(tablero)):
        for x in range(len(tablero[i])):
            if tablero [i][x] == "O":
                tablero[i][x]= "_"
    return tablero

def pedir_datos_barco():
    while True:
        try:
            fila = int(input("Introduce un numero del 0 al 10"))
            columna = int(input("Introduce un número del 0 al 10"))
            eslora = int(input("Selecciona tu eslora entre 2 ,3 y 4"))
            orientacion = input("Introduce una orientacion entre horizontal/vertical")
            lista_barco = [eslora,fila,columna,orientacion]
            if fila <= 0 or columna <= 0:
                print("El número no puede ser 0 o menor, vuelve a introducir los valores")
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
    elif lista_barco [3].lower() == "vertical" and lista_barco[0]>= 6:
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
