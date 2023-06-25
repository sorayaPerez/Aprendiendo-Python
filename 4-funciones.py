# FUNCIONES EN PYTHON: Sintaxis básica

""" Ejercicio 1 (introducción): La universidad desea un programa que permita mostrar a través 
de una función un mensaje que permita darle la bienvenida a los alumnos, similar al 
siguiente:

======================================
Bienvenidos a la Universidad de Python!
=======================================

Además, se requiere mostrar los números de aulas disponibles de los 5 pisos con los que 
cuenta uno de los edificios. Las aulas se numeran desde el número 100 y hay 10 por piso. 
Mostrar de la siguiente manera:

Piso   Aulas
1 100 a 110
2 200 a 210
3 300 a 310
4 400 a 410
5 500 a 510

"""


def imprimir_mensaje(): #No resive parametro, la llamas  y hace lo que le diste de instruccion
    print("=======================================")
    print("Bienvenidos a la Universidad de Python!")
    print("=======================================")

def imprimir_aulas():
    print("Piso\tAulas") #/t tabulacion
    for i in range(1,6):    # empieza en 1, termina en 6    
        print(i, end='\t') # El end te pega una linea al lado de la otra
        inicio = i*100
        fin = inicio+10
        print(f'{inicio} a {fin}')
        
# Programa principal
imprimir_mensaje()
print()
imprimir_aulas()





# FUNCIONES CON PARÁMETROS
# Parámetros: Al definir la función
# Argumentos: Al llamarla


"""Ejercicio 2:  Mostrar a través de una función un mensaje de bienvenida a los 
alumnos, pero indicando el cuatrimestre y el año. Validar en el programa principal que se 
haya ingresado un valor en ambos parámetros. El mensaje será similar al siguiente: 

Bienvenidos estudiantes!
1er cuatrimestre 2023

Además, desarrollar una función que permita calcular el valor de un curso dependiendo de 
la forma de pago. El importe y la forma de pago (contado, débito o crédito) se ingresan por 
teclado.
• Si la forma de pago es contado se hace un descuento del 10%
• Si la forma de pago es débito no se hace descuento
• Si la forma de pago es crédito el interés por pagar en 3 cuotas es del 15% y se van 
agregando 15% para 6, 9 o 12 cuotas. 
• Si la forma de pago no es correcta se deberá informar a través de un mensaje.
Calcular el valor de la cuota y el total financiado y mostrar lo siguiente, según el caso:

Ingrese un importe: 12000
Ingrese una forma de pago: Contado, Débito, Crédito: Contado
Forma de pago: Contado. Valor: 10800.0

Ingrese un importe: 12000
Ingrese una forma de pago: Contado, Débito, Crédito: Débito
Forma de pago: Débito. Valor: 12000

Ingrese un importe: 12000
Ingrese una forma de pago: Contado, Débito, Crédito: Crédito
Forma de pago: Crédito.

Cuotas Valor cuota Total financiado
3 4600.0 13800.0
6 2600.0 15600.0
9 1933.33 17399.97
12 1600.0 19200.0

Ingrese un importe: 12000
Ingrese una forma de pago: Contado, Débito, Crédito: Otro
Forma de pago errónea


"""


def imprimir_bienvenida(cuat, anio):
    print("Bienvenidos estudiantes!")
    print(f'{cuat} cuatrimestre {anio}')

def mostrar_cuotas_curso(importe, fpago):
    fpago = fpago.upper()
    if fpago == "CONTADO":
        print(f'Forma de pago: Contado. Valor: {importe-(importe*0.1)}')
    elif fpago == "DÉBITO" or fpago == "DEBITO":
        print(f'Forma de pago: Débito. Valor: {importe}')
    elif fpago == "CRÉDITO" or fpago == "CREDITO":
        print("Forma de pago: Crédito.")
        print("Cuotas\tValor cuota\tTotal financiado")
        interes = 1.15
        for i in range(3,13,3): #incremento de 3 en tres
            valor_cuota = round(importe*(interes)/i,2)
            total_financiado = valor_cuota * i
            print(f'{i}\t{valor_cuota}\t\t{total_financiado}')
            interes = interes + 0.15
    else:
        print("Forma de pago errónea")




#Programa principal

cuat = input("Escriba un cuatrimestre: 1er o 2do: ")
while len(cuat)==0: #Validamos que se haya escrito un nombre
    print("Debes escribir un valor")
    cuat = input("Escriba un cuatrimestre: 1er o 2do: ")

anio = int(input("¿Qué año es?: "))
while anio<2000: #Validamos que no se ingresen valores menores que 2000
    print("Dato no válido! Debe ser mayor o igual a 2000")
    anio = int(input("¿Qué año es?: "))

# anio = input("Ingresa el año: ")
# while not anio.isnumeric() or int(anio) <= 2000:
#     anio = input("Ingresa un año válido (mayor a 2000): ")

imprimir_bienvenida(cuat, anio)




importe = int(input("Ingrese un importe: "))
forma_pago = input("Ingrese una forma de pago: Contado, Débito, Crédito: ")

mostrar_cuotas_curso(importe, forma_pago)




print("-"*40)
# Parámetros opcionales y parámetros posicionales



"""Ejercicio 3: : La universidad requiere una 
función que permita registrar datos de los alumnos. Esta función recibe su nombre 
completo, la sede y el año de ingreso. Dado que la mayoría de los alumnos son de la sede 
“Buenos Aires” y el año de ingreso es el actual considerar estos valores por defecto, además 
mostrar el nombre con la primera letra de cada palabra en mayúsculas. Mostrar los datos 
de la siguiente manera: """

# registrar_datos("agustina gonzález","Córdoba",2021)
# registrar_datos("diego lópez","Misiones")
# registrar_datos("ANA FERNÁNDEZ")

# Se ha inscripto a Agustina González en la sede Córdoba para el año 
# 2021
# Se ha inscripto a Diego López en la sede Misiones para el año 
# 2023Se ha inscripto a Ana Fernández en la sede Buenos Aires para el 
# año 2023 


"""
Además crear una función que reciba y muestre los siguientes datos de la sede: dirección, 
ciudad y provincia, considerando como valor por defecto “Buenos Aires”.
Realizar llamadas a la función indicando una posición distinta en los parámetros, por 
ejemplo:
"""
#datos_sede("Av. Las Heras 3456", "Godoy Cruz", "Mendoza")
#datos_sede(provincia='Chubut', ciudad='Rawson', direccion='Belgrano 312')
#datos_sede(ciudad='Mar del plata', direccion='Av. Moreno 56')

""" La salida por pantalla esperada es similar a esta: """
#Universidad de Python - Av. Las Heras 3456 - Godoy Cruz - Mendoza
#Universidad de Python - Belgrano 312 - Rawson - Chubut
#Universidad de Python - Av. Moreno 56 - Mar del plata - Buenos Aires





def registrar_datos(nomcomp, sede='Buenos Aires', anio=2023):
    print(f'Se ha inscripto a {nomcomp.title()} en la sede {sede} para el año {anio}')

def datos_sede(direccion, ciudad, provincia = 'Buenos Aires'):
    print(f'Universidad de Python - {direccion} - {ciudad} - {provincia}')

# Programa principal

# Parámetros opcionales
registrar_datos("agustina gonzález","Córdoba",2021)
registrar_datos("diego lópez","Misiones")
registrar_datos("ANA FERNÁNDEZ")

# Parámetros posicionales
datos_sede("Av. Las Heras 3456", "Godoy Cruz", "Mendoza")
datos_sede(provincia='Chubut', ciudad='Rawson', direccion='Belgrano 312')
datos_sede(ciudad='Mar del plata', direccion='Av. Moreno 56')




# Funciones que retornan valores




"""Ejercicio 4 : La universidad requiere una función que reciba el valor 
de la cuota y un porcentaje de aumento (número entero). La función debe devolver la cuota 
con el aumento aplicado. Solicitar en el programa principal la cuota y el porcentaje y mostrar 
en el programa principal estos dos valores más la cuota aumentada, de la siguiente manera:
"""

# Cuota $ 25000 
# Aum 15%
# Total $ 28750.0

"""Además se requiere una función que valide si un alumno es mayor de edad. Recibe la edad 
y devuelve True o False.
En el programa principal ingresar la edad y llamar a la función hasta que la edad ingresada 
sea mayor a 18, luego mostrar la edad y el valor retornado por la función (debe ser True). 
Ejemplo:"""

# Ingrese la edad del estudiante: 12
# Debe ser mayor o igual a 18. Ingrese la edad del estudiante: 16
# Debe ser mayor o igual a 18. Ingrese la edad del estudiante: 17
# Debe ser mayor o igual a 18. Ingrese la edad del estudiante: 19
# Edad: 19. Es mayor? True

"""Desarrollar una función que reciba el valor de un curso retorne tres valores: pagado en 3
cuotas sin interés, en 6 cuotas con un 25% de interés o en 9 cuotas con un 50% de interés.
En el programa principal se debe mostrar el valor del curso y las tres opciones de 
financiación (recordar desempaquetar), como el ejemplo:"""

# Ingrese el costo del curso: 10000
# Costo del curso $ 10000
# - Tres cuotas de $ 3333.33
# - Seis cuotas de $ 2083.33
# - Nueve cuotas de $ 1666.67

"""Finalmente la universidad desea una función que permita ingresar las materias que se dictan 
en un cuatrimestre. Recibe la cantidad de materias que se van a ingresar y devuelve una lista 
con las materias ingresadas.
En el programa principal mostrar cada uno de los elementos de la lista, como el ejemplo:
"""

# Listado de materias:
# 1- Sistemas Operativos
# 2- Programación I
# 3- Algoritmos
# 4- Robótica




def aumentar_cuota(cuota, aumento):
    cuota_aumentada = cuota + cuota * aumento/100
    return cuota_aumentada

def es_mayor(edad):
    if edad >= 18:
        return True
    else:
        return False

def calcular_cuotas(importe):
    tres_cuotas = round(importe / 3, 2)
    seis_cuotas = round(importe * 1.25 / 6, 2)
    nueve_cuotas = round(importe * 1.50 / 9, 2)
    return tres_cuotas, seis_cuotas, nueve_cuotas

def cargar_materias(cantidad):
    materias = [] #hace una lista
    for i in range(cantidad):
        materia = input("Ingrese la materia: ")
        materias.append(materia) #agrega el valor que escibre el usuario
    return materias

#Programa principal
cta = int(input("Ingrese el valor de la cuota: "))
aum = int(input("Ingrese el porcentaje de aumento (número entero): "))
cta_aum = aumentar_cuota(cta, aum)
print(f'Cuota \t$ {cta} \nAum \t{aum}%\nTotal \t$ {cta_aum}')




edad = int(input("Ingrese la edad del estudiante: "))
while es_mayor(edad) != True:
    edad = int(input("Debe ser mayor o igual a 18. Ingrese la edad del estudiante: "))
print(f'Edad: {edad}. Es mayor? {es_mayor(edad)}')






imp = int(input("Ingrese el costo del curso: "))
tres, seis, nueve = calcular_cuotas(imp)
print(f'Costo del curso $ {imp}\n - Tres cuotas de $ {tres}\n - Seis cuotas de $ {seis}\n - Nueve cuotas de $ {nueve}')





lista_materias = cargar_materias(4)
print("Listado de materias:")
for i in range(len(lista_materias)):
    print(f'{i+1}- {lista_materias[i]}')






"""Ejercicio 5:: La universidad requiere un sistema que realice 
varias tareas:
• Debe permitir la carga de N notas en una lista hasta que se ingrese -1. No recibe 
parámetros y devuelve la lista.
• Debe validar que las notas ingresadas sean números entre 1 y 10 (considerar la 
excepción del -1).
• Obtendrá la cantidad de notas ingresadas y el promedio. Mostrará esos datos en 
pantalla, como el ejemplo:
"""
# Ingrese una nota: 8
# Ingrese una nota: -2
# Dato no válido! Ingrese una nota: -9
# Dato no válido! Ingrese una nota: 11
# Dato no válido! Ingrese una nota: 15
# Dato no válido! Ingrese una nota: 6
# Ingrese una nota: 5
# Ingrese una nota: 10
# Ingrese una nota: -1
# Cantidad de notas: 4. Promedio: 7.25



#Función que valida el rango entre 1 y 10 y el corte -1
def ingresar_positivo():
    nota = int(input("Ingrese una nota: "))
    while (nota < 1 or nota > 10) and nota != -1:
        nota= int(input("Dato no válido! Ingrese una nota: "))
    return nota

#Función que crea la lista con las notas validadas
def crear_lista():
    lista = [] #Lista vacía
    nota = ingresar_positivo() #Llama a la f ingresar positivo para validar
    while nota != -1:
        lista.append(nota) #Agrega la nota a la lista
        nota = ingresar_positivo()
    return lista

#Función que va a calcular el promedio recorriendo la lista y sumando las notas
def obtener_datos(lista):
    suma = 0
    cantidad_notas = len(lista)
    for i in range(cantidad_notas):
        suma = suma + lista[i]
    promedio = round(suma / cantidad_notas, 2)
    return promedio, cantidad_notas

# Programa principal
lista_notas = crear_lista()
prom, cant = obtener_datos(lista_notas) #La f devuelve el promedio a prom y la cantidad de notas a cant
print(f'Cantidad de notas: {cant}. Promedio: {prom} ')



