####Operadores asignacion
i=0
i= i+1
print(i)

# Operadores binarios
i+=1 #Incremento en 1 la variable i, equivamente a i= i+1. No tenemos el i++
print(i)
i-=1 #Decremento en 1 la variable i, equivalente a i= i-1. No tenemos el i++
i*=1
i/=1

# Sumatoria
suma= 0
num=  int(input())
suma+= num # Equivalente a suma= suma + num



# EJERCICIO: Ingresar un número entero e imprimir un mensaje indicando si es cero, par o impar.
c=int(input("Ingrese un número:"))
if c == 0:
    print("El número ingresado es cero.")
else:
    if c % 2 == 0:
        print("El número", c, "es par.")
    else:
        print("El número", c, "es impar.")


# EJERCICIO: Ingresar dos números enteros y decir si alguno es divisible por el otro.
num1=int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número:"))
if num1 % num2 == 0 or num2 % num1 == 0:
    print("Uno de los números es divisible por el otro")
else:
    print("Ninguno de los números es divisor del otro")

# -------------------------------------------------------------------------------------------------------
# Estructuras Iterativas/Repetitivas
# Ciclos Exactos: yo sé la cantidad exacta de repeticiones (while/for).
# Ciclos Condicionales: no sé la cantidad de repeticiones (while).
# -------------------------------------------------------------------------------------------------------


'''
Realizar un programa que imprima en pantalla los números del 1 al 100.
'''

i= 1            # Inicialización del contador
while i<=10:    # Cuando llegue a 10 quiero que finalice, es una condición (que en algún momento tiene que finalizar)
    print(i)    # Imprimo el contador, con print(i, end='-') se imprimen uno al lado del otro
    i= i+1      # Le sumo 1
print("Fin del programa")

i= 1 #Debemos darle un valor inicial
N= int(input("Ingrese valor máximo del contador: ")) # Sigue siendo exacto porque al momento de ejecutar el While ya conozco el dato
while i<=N:     # Puede pasar que no entre en la condición porque sea falsa de entrada
    print(i)    # El orden es importante (si lo cambiamos tendremos un comportamiento diferente)                 
    i= i+1      # Importante: no debemos olvidar la instrucción que cambia la condición
print("Fin del programa")


    # For
    #Range va a generar una serie de valores entre un valor inicial, un valor final y el incremento entre valor y valor
    #Esta es una sintaxis para Python, que dista bastante de JS o JAVA
    #Tenemos un valor inicial, un fin y un salto/incremento
    #El valor final en el range no es inclusivo, si queremos hacer desde el 1 al 10 debemos colocar 11 como fin (10+1)

for cont in range(1,10,1): #inicio, fin, salto/inc
    print(cont) #cont es de ámbito local, existe dentro del for

#Otro ejemplo con valores ingresados por el usuario
N= int(input("Ingrese valor máximo del contador: "))

for cont in range(1,N+1,1): #inicio, fin, salto/inc
    print(cont) 

#Otra variante del For: sin incremento, que por defecto es 1
for cont in range(1,N+1): #inicio, fin
    print(cont) 


# Ciclos Condicionales
'''
Realizar un programa que calcule la sumatoria de números enteros ingresados
por teclado. Finaliza el programa ingresando 0.
'''

suma= 0 # Inicializo mi acumulador (sumatoria)
num= int(input("Ingrese un número: "))
while num!=0:   #Cortamos la condiciòn cuando el nùmero sea distinto de 0
                #Si es 0 no entra en el buble o deja de repetirse
    suma+= num # suma= suma+num
    num= int(input("Ingrese un número: "))  #Volvemos a pedir el número para evitar caer en un ciclo infinito
                                            #No debemos olvidar la instrucción que cambia la condición
print("La sumatoria de los números ingresados es:", suma) #Mostramos el resultado


'''
Realizar un programa que solicite ingresar dos números distintos y muestre
por pantalla el mayor de ellos. Si NO son distintos mostra un mensaje de error.
'''
num1=int(input("Ingrese el primer valor:"))
num2=int(input("Ingrese el segundo valor:"))
if num1!=num2: 
    if num1>num2: 
        # Bloque de verdad
        print("num1 es mayor")
        # print("El valor mayor es", num1)
    else:
        # Bloque de falsedad
        print("num2 es mayor")
        # print("El valor mayor es", num2)
else:
    print("Error! los números son iguales.")
print("Fin del programa")






#Repetitivas 

#While 
#EJERCICIO: Leer números y mostrarlos hasta que se ingrese un número negativo (ciclo condicional).
num1 = int(input("Ingrese un número: "))
while num1 > 0:
    print(num1)
    num1 = int(input("Ingrese un número: "))
print("Fin del ejercicio")

#EJERCICIO: Desarrollar un programa que cuente hasta 4, utilizando una sola variable para contar (ciclo exacto).
cont= 1 #Inicializamos la variable
while cont <= 4:
    print(cont)
    cont = cont + 1     # Incrementamos la variable en 1
                        # Siempre debemos modificar la variable
                        # que determinará nuestra Condición
                        # Sino, se genera un CICLO INFINITO!
print("Fin del ejercicio")

#EJERCICIO: Ingresar números enteros y sumar solamente los números positivos, el programa finalizará ingresando 0 (cero) (ciclo condicional).
suma= 0
nro= int(input("Ingrese un número (cero para finalizar): "))
while nro != 0:
    if nro > 0:
        suma += nro
    nro= int(input("Ingrese otro número (cero para finalizar): "))
print("FIN! Ingresó cero. La suma de los valores ingresados es:", suma)

#EJERCICIO: Ingresar 5 valores por teclado, obtener su suma y su promedio.
cont= 1
suma= 0
while cont <= 5:
    num= int(input("Ingrese un número: "))
    suma = suma + num   # Acumulamos, es equivalente suma += num 
    cont = cont + 1     # Incrementamos, es equivalente cont += 1

print("La suma es:", suma)
print("El promedio es:", suma/cont)

#For
# EJERCICIO: Mostrar los números del 1 al 10.
for i in range(1,11,1): #No incluye al 10 (se puede poner 10+1)
    print(i)

# EJERCICIO: Mostrar los múltiplos de 5 comprendidos entre 12 y 80.
for i in range(12,81,5):
    print(i)

# EJERCICIO: Imprimir los números del 9 al 1.
for i in range(9,0,-1): #En este caso, como el valor inicial es mayor al valor final, el paso debe ser necesariamente un número negativo.
    print(i)

# EJERCICIO: Mostrar los números del 10 al 20
for i in range(10,21):
    print(i)

# EJERCICIO: Ingresar cinco números y mostrar su suma
suma= 0
for i in range(5):
    a = int(input("Ingrese un número: "))
    suma += a
print("La suma es:", suma)




