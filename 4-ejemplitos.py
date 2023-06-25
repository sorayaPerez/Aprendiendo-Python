#Docstrings


def cuad(x):
    """Dado un nro x, calcula x²"""
    return x * x 
def modulo_vector(x, y):
    """Calcula el modulo de un vector 2D.
    Argumentos:
        x: (float|int) coordenada de las abscisas
        y: (float|int) coordenada de las ordenadas
    Devuelve: (float) el modulo del vector
    """
    return (x ** 2 + y ** 2) ** 0.5

print(help(cuad))
print()
print(help(modulo_vector))


# FUNCIONES EN PYTHON: Sintaxis básica

def imprimir_mensaje():
    print("Hola soy una función")

def imprimir_mensaje_cinco_veces():
    for i in range(5):       
        print("Mensaje " + str(i))
        #imprimir_mensaje()
    
# Programa principal
imprimir_mensaje()
imprimir_mensaje_cinco_veces()


# FUNCIONES LAMBDA


# ---------------------------------
def alCubo(x): #definición de función común
    return x*x*x

cubo = lambda x: x*x*x # la misma función escrita 
# como función lambda, no tiene nombre,
# es anónima (ojo: cubo es el nombre de la variable, no de la función)

#Programa principal
print(alCubo(3)) #27
print(cubo(5)) #125
print()

# ---------------------------------
# Usamos una función lambda en combinación con map()
enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros)) # map(función, lista)
print(cuadrados) # [1, 4, 16, 49]
print()

# ---------------------------------
# Ejemplo: en lugar de pasar una lista de valores, pasamos como segundo parámetro una lista de funciones
enteros = [1, 2, 4, 7]
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3

funciones = [cuadrado, cubo] #lista de funciones
for e in enteros:
    valores = list(map(lambda x : x(e), funciones)) # map(función, lista)
    print(valores) # [1, 1] [4, 8] [16, 64] [49, 343]


# FUNCIONES LISTAS

'''
# Funciones que reciben listas
def sumar_lista(lista): #pre: recibe una lista.
    suma = 0 # variable que almacenará la sumatoria
    cant = 0
    for elem in lista:
        suma += elem #acumulador de elementos
        cant += 1
    prom = suma/cant
    return suma, cant, prom #devuelve la sumatoria, la cantidad y el promedio de los elementos de la lista

#llamada a la función (programa principal)
numeros= [1,2,10,-5] #Le damos valores a la lista
suma, cantidad, promedio = sumar_lista(numeros)

print(f'Lista: {numeros}\nSuma: {suma}\nCantidad: {cantidad}\nPromedio: {promedio}')

'''


# ---------------------------------------------------------
# Ejemplo de carga de listas con valores positivos: validación y muestra

def ingresar_positivo():
    cant= int(input("Ingrese un número: "))
    while cant<=0:
        print("Dato no válido!")
        cant= int(input("Ingrese un número: "))
    return cant

def crear_lista(N):
    lista= []
    for i in range(N):
        valor= ingresar_positivo()
        lista.append(valor)
    return lista

def mostrar_lista(lista):
    for valor in lista:
        print(valor, end=" ")
    print()

# Prog Ppal
N=int(input("¿Cuántos valores tendrá la lista?: "))
numeros = crear_lista(N)
mostrar_lista(numeros)



# FUNCIONES CON PARÁMETROS
# Parámetros: Al definir la función
# Argumentos: Al llamarla

# Funciones con un parámetro
def imprimir_mensaje_N_veces(N): #Tiene 1 parámetro
    for i in range(N):
        print("Mensaje " + str(i))

# Programa principal
imprimir_mensaje_N_veces(3) #Ejemplo sin datos ingresados por el usuario

veces= int(input("Ingrese la cantidad de veces que desea imprimir: "))
imprimir_mensaje_N_veces(veces) #Ejemplo con datos ingresados por el usuario

# --------------------------------------------------------------------------------
# Funciones con dos parámetros
def mensaje_personalizado_N_veces(N, mje): #Tiene 2 parámetros
    for i in range(N):
        print(mje)

# Programa principal
mensaje_personalizado_N_veces(4, "Juan Pablo")


# Variante: función con 2 datos de entrada que recibe como parámetros proporcionados por el usuario. Usamos la misma función pero le pasamos valores nosotros.
cant = int(input("¿Cuántas veces se repetirá el valor?: "))
mensaje = input("¿Cuál es el mensaje?: ")
mensaje_personalizado_N_veces(cant, mensaje)

# Variante validando el código:
cant = int(input("¿Cuántas veces se repetirá el valor?: "))
while cant<=0: #Validamos que el número sea positivo
    print("Dato no válido!")
    cant = int(input("¿Cuántas veces se repetirá el valor?: "))
mensaje = input("¿Cuál es el mensaje?: ")
while len(mensaje)==0: #Validamos que se haya escrito un mensaje
    print("Debes escribir un mensaje!")
    mensaje = input("¿Cuál es el mensaje?: ")
mensaje_personalizado_N_veces(cant, mensaje)

# ---------------------------
# Ejemplo utilizando f-string
def multiplicar_por_5(numero):
    print(f'{numero}*5 = {numero * 5}')

# Programa principal
print("Comienzo del programa: ")
multiplicar_por_5(7)
print("Siguiente instrucción")
multiplicar_por_5(113)
print("Fin del programa")
# ------------------------------------------------------
# Parámetros opcionales
def sumar(a=2, b=0):
    return a + b

print(sumar(2,6))
print(sumar(5))
print(sumar())


def saludo(nombre, mensaje="encantado de saludarte"):
    print(f"Hola {nombre}, {mensaje}")

# Programa principal
saludo("Juan Pablo")
saludo("Juan Pablo", "¿cómo estás?")


# Parámetros opcionales (otro ejemplo)
def fn_raiz(num, raiz=2):#Si no recibe un segundo parámetro calcula la raiz cuadrada (2)
    return num**(1/raiz)

# Programa principal
print(fn_raiz(4))
print(fn_raiz(125,3)) #Acá tiene dos parámetros, el número y la raíz, que no necesariamente tiene que estar y si no está toma por defecto el 2.

# Parámetros posicionales y parámetros con nombre
def saludo(nombre, mensaje="encantado de saludarte"):
    print(f"Hola {nombre}, {mensaje}")

saludo(mensaje="¿Cómo estás?", nombre="Juan Pablo")
saludo(nombre="Ana Marìa", mensaje="Bienvenida!")
saludo("Juan Pablo", mensaje="¿Cómo estás?")




# FUNCIONES QUE DEVUELVEN VALORES (return)

def restar(num1,num2): # recibe 2 parámetros
    resta= num1-num2
    return resta # La fx retorna (devuelve) un valor

# Programa Principal
resultado = restar(10,3)
print("El resultado es:", resultado) #imprimo el valor de la variable (resultado)
print("El resultado es:", restar(4,9)) #imprimo lo que retorna la función restar(x,y)


# ---------------------------------------------------------------
# Ejemplo: return que no devuelve ningún valor
# Esta función buscar averiguar el cuadrado del número sólo si es par
def cuadrado_de_par(numero):
    if numero % 2 == 0:
        print(numero ** 2)
    else:
        return
cuadrado_de_par(8) #64
cuadrado_de_par(3) #nada, porque no es par


# ---------------------------------------------------------------
# Ejemplo: return que devuelve un valor u otro (con if)
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(2)) #True
print(es_par(5)) #False
for i in range(1,11): #Uso de la función dentro de un ciclo: obtenemos los pares en cierto rango
    if es_par(i) == True:
        print(i)

# ---------------------------------------------------------------
# Ejemplo: Devolver más de un valor con return
def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3

#Programa principal
cuad, cubo = cuadrado_y_cubo(8) #Desempaquetado
print(f'Cuadrado: {cuad}\nCubo: {cubo}')

def operaciones(a,b):
    if b != 0:
        return a+b, a-b, a*b, a/b
    else:
        return a+b, a-b, a*b, "Error, b es 0"

#Programa principal
suma, resta, multiplicacion, division = operaciones(10,5) #Desempaquetamos
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)


# Devolvemos los diferentes resultados/valores en una lista
def tabla_del(numero):
    resultados = [] #creamos la lista
    for i in range(11):
        resultados.append(numero * i)
    return resultados

#Programa principal
res = tabla_del(3)
print(res)



# EJEMPLO: FUNCIÓN QUE DEVUELVE UN VALOR
import math
'''
Ingresar la longitud del radio de una circunferencia.
Calcular y mostrar:
· La superficie del círculo (Sup = pi * r*r)
· El perímetro de la circunferencia (Per = pi * d)
· La superficie de la esfera (Sup = 4 * pi * r*r)
· El volumen de la esfera (Vol = 4/3 * pi * r*r*r)
'''
def calcularSupCirculo(radio):
    '''La superficie del circulo (Sup = pi * r*r)'''
    return math.pi * (radio ** 2)
def calcularPerCircunferencia(radio):
    '''El perímetro de la circunferencia (Per = pi * d)'''
    return math.pi * 2 * radio
def calcularSupEsfera(radio):
    ''' La superficie de la esfera (Sup = 4 * pi * r*r) '''
    return 4 * math.pi * (radio ** 2)
def calcularvolEsfera(radio):
    ''' La superficie de la esfera (Sup = 4 * pi * r*r) '''
    return 4/3 * math.pi * (radio ** 3)

# Programa principal
help(calcularSupCirculo)

radio = float(input('Radio: '))
print(f'Sup. del círculo: {calcularSupCirculo(radio):.2f}')
print(f'Perím. de la circunf.: {calcularPerCircunferencia(radio):.2f}')
print(f'Sup. de la esfera: {calcularSupEsfera(radio):.2f}')
print(f'Vol. de la esfera: {calcularvolEsfera(radio):.2f}')



# EJEMPLO: FUNCIÓN QUE DEVUELVE VARIOS VALORES
'''
Tarea: permite recibir un importe y obtiene la mínima cantidad de
billetes a recibir.
Los valores de los billetes pueden ser 500, 100, 50, 20, 10, 5, 1.
'''
def convertir(importe):
    b500 = importe // 500
    importe %= 500
    b100 = importe // 100
    importe %= 100
    b50 = importe // 50
    importe %= 50
    b20 = importe // 20
    importe %= 20
    b10 = importe // 10
    importe %= 10
    b5 = importe // 5
    importe %= 5
    b1 = importe
    return b500, b100, b50, b20, b10, b5, b1

# programa principal
imp = 1626
b500, b100, b50, b20, b10, b5, b1 = convertir(imp)
print(f'b500: {b500}, b100: {b100}, b50: {b50}, b20: {b20}, b10: {b10}, b5: {b5}, b2: {b1}')




# EJEMPLO: USO DE PARÁMETROS POR DEFECTO
'''Tarea: Por cada empleado de una empresa se leen tres datos: legajo, sueldo básico y
antigüedad en la empresa. Emitir un listado que informe:
    - Importe total de salarios pagados.
    - Porcentaje de empleados que ganan más del 20000.
    - Legajo del empleado que más gana.
    - Sueldo más bajo.
    Nota:
    - El salario de la siguiente manera, al sueldo básico se le debe sumar un 5%
    por año de antigüedad, agregando un 25% adicional si la misma supera los
    10 años.
    - El sueldo de los empledos no supera el millon de pesos.
    - El lote de datos finaliza cuando se ingresa el legajo 0 (cero)
    - Validar los datos de entrada
'''
def ingEntPos(mensaje):
    valor = float(input(mensaje))
    while valor != int(valor) or valor < 0:
        valor = float(input('Error. ' + mensaje))
    return int(valor)

def ingRealPos(mensaje):
    valor = float(input(mensaje))
    while valor < 0:
        valor = float(input('Error. ' + mensaje))
    return valor

def porcentaje(parcial, total):
    return parcial * 100 / total

def sueldoNeto(basico, antiguedad = 0):
    neto = basico + 0.05 * basico * antiguedad
    if antiguedad > 10:
        neto += 0.25 * basico
    return neto

# Programa principal
sueldoTotal, cantEmpl, cantEmplMas20Mil = 0, 0, 0
legMasGana, sueldoMasGana, sueldoMenosGana = 0, 0, 1000000
legajo = ingEntPos('Legajo: ')

while legajo != 0:
    ant = ingEntPos('Antiguedad: ')
    sBasico = ingRealPos('Sueldo: ')
    sueldo = sueldoNeto(sBasico) if ant == 0 else sueldoNeto(sBasico, ant)
    sueldoTotal += sueldo
    cantEmpl += 1
    if sueldoMasGana < sueldo:
        sueldoMasGana = sueldo
        legMasGana = legajo
    if sueldoMenosGana > sueldo:
        sueldoMenosGana = sueldo
    if sueldo > 20000:
        cantEmplMas20Mil += 1
    legajo = ingEntPos('Legajo: ')
print(f'Importe total a pagar: {sueldoTotal:10.2f}')
if cantEmpl != 0:
    print(f'Porcentaje de empleados que ganan más del 20000: {porcentaje(cantEmplMas20Mil, cantEmpl): 10.2f}')
    print(f'Empleado que más gana: {legMasGana}')
    print(f'Sueldo más bajo: {sueldoMenosGana}')




# VALOR REFERENCIA



#Pasaje por valor
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n) #10, no afecta a la variable, sigue valiendo lo mismo
def doblar_valor(numero):
    return numero * 2

n = 10
n = doblar_valor(n)
print(n) #20


#Pasaje por referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns)
print(ns) #[20, 100, 200]

ns = [10,50,100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
print(ns) #[10, 50, 100]



# VARIABLES



# Ámbito y ciclo de vida de las variables

def saludo(nombre):
    x = 10
    print(f'Hola {nombre}')
saludo('Luis')
print()
# print(x) # NameError: name 'x' is not defined

# -----------------------------------------
def muestra_x():
    x = 10
    print(f'x vale {x} dentro de la fx')

x = 20 #Es una variable de alcance global, diferente de la que está dentro de la función
muestra_x() # x vale 10
print(f'x vale {x} fuera de la fx') #20
print()

# -----------------------------------------
y = 20 #Global 

def muestra_xy():
    x = 10 #Local
    y = 15 #Global modificada
    print(f'"x" vale {x} "y" vale {y}')

muestra_xy() # "x" vale 10 "y" vale 15
print(f'Global: {y}') #20, global


