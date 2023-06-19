print("****** CADENAS DE CARACTERES ******")

#Escritura y concatenación


# Combinar comillas simples y dobles



#Concatenar números y cadenas

#Replicación de cadenas



#Cadenas multilínea




#Comparación de cadenas (ASCII y case sensitive)




#Largo de cadenas y subíndices



#Métodos upper / lower / capitalize / title



#Rebanadas (slicing)
# [:] Todos los elementos.


# [start:] Todos los elementos desde el índice establecido(start).


# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).


# [start:end] Todos los elementos de un rango de índices.


# [start:end:step] Todos los elementos de un rango de índices con saltos.


# [::step] Todos los elementos con saltos.


# [::step] Todos los elementos con saltos (negativo).



#Operadores de pertenencia: in / not in


#Iterando cadenas
#For


#While



#Uso de min y max



######################################################################

print("****** CADENAS: METODOS ******")

#Join 



#Split


#Replace


#Count e Index


#isalpha / isdigit / isalnum


#isupper / islower



#center / ljust / rjust / zfill


#lstrip / rstrip / strip
#lstrip quita elementos de la izquierda


#rstrip quita elementos de la derecha


#strip quita elementos de ambos lados


#find y rfind

######################################################################

#f-strings: ejemplo 1: cadenas


#f-strings: ejemplo 2: números


#f-strings: ejemplo 3


######################################################################

print("****** LISTAS ******")

#Creación e impresión de listas

#Acceso a elementos

# Iterar sobre una lista (for)

# Iterar sobre una lista (while)


#Desempaquetado de listas

#Desempaqueto la lista 2 en los 3 elementos



######################################################################

print("****** LISTAS: Métodos ******")

#Append agrega en la última posición


#Insert agrega en determinada posición


#Pop: no sólo elimina el elemento, sino que devuelve la posición


#Remove: elimino por su valor


#Index: devuelve la posición de determinado elemento



#Count: Cuenta cantidad de elementos


#Reverse: Da vuelta los valores de una lista


#Sort: Ordena una lista


#Clear: Vacía una lista


######################################################################

print("****** LISTAS: Operaciones ******")

#Concatenar



#Modificar valores por posición


#Intercambiar valores


#len (largo de la lista)



#Suma, máximo, mínimo y promedio



#list 



######################################################################

print("****** DICCIONARIOS ******")

#Creación de diccionarios
vacio = {} 			                # diccionario vacío
dicc_uno = {'Juan': 56}			    # diccionario de un elemento
dicc_dos = {'Juan': 56, 'Ana': 15}  # diccionario de dos elementos
print(vacio)
print(dicc_uno)
print(dicc_dos)
print()

#Acceder a elementos
print(dicc_dos.items()) #Mostramos los pares clave-valor
for clave, valor in dicc_dos.items(): #otra manera de mostrar los pares clave-valor
    print(f'{clave}: {valor}')

print(dicc_dos.keys()) #Mostramos las claves
for i in dicc_dos.keys(): #Mostramos los valores
    print(dicc_dos[i], end=' ')
print()

#Modificar elementos
print("Edad de Juan:",dicc_dos["Juan"]) #Valor que corresponde a la clave "Juan"
dicc_dos["Juan"] = 37
print("Nueva edad de Juan:",dicc_dos["Juan"]) 

#Agregar elementos
dicc_dos["Pablo"] = 12
dicc_dos["Julieta"] = 26
print(dicc_dos)
dicc_dos["Pablo"] = 47 #No agrega un nuevo "Pablo", sino que modifica el existente
print(dicc_dos)
print()

#Otra forma de acceder a elementos y mostrarlos: listas
lista_claves = list(dicc_dos.keys()) # Le pido al dicc sus claves y lo convierto a lista
lista_valores = list(dicc_dos.values())

for i in range(len(lista_claves)):
   print(lista_claves[i],"tiene",lista_valores[i],"años") #Imprimimos valores
'''
'''

######################################################################

print("****** TUPLAS ******")

#Creación de tuplas
vacia = () # tupla vacía
tupla_uno = 'Juan Pablo', # tupla con un valor
tupla_dos = ('Juan', 37, False) # mixtas
tupla_tres = 'Luciana', 56, (1998,5,26) # Tupla anidada
tupla_cuatro = ('Rivadavia', 3567, ['Calle 1', 'Calle2']) # Tupla con lista

print(vacia)
print(tupla_uno)
print(tupla_dos)
print(tupla_tres)
print(tupla_cuatro)
print()

#Acceso a elementos
print(tupla_dos[0]) 
print(tupla_tres[2]) 
print(tupla_cuatro[1]) 
#tupla_dos[0] = "Pablo" # Error
print()

#Otra forma de crear una tupla: empaquetar
nombre= 'Carlos'
apellido= 'Rodriguez'
datos= nombre,apellido,32
print(datos) 
print(type(datos))
print()

#También podemos desempaquetar una tupla para acceder a sus datos
fecha= (7, "noviembre", 2022)
print(fecha)
dd,mm,aa= fecha
print("Dia:",dd)
print("Mes:",mm)
print("Año:",aa)
print()

######################################################################

print("****** CONJUNTOS ******")

#Creación de conjuntos
conj_uno = set()
conj_dos = {'Juan','Juan'}
conj_tres = {'Pablo', 3456, True}
conj_cuatro = {'Rivadavia', 3567, ('Calle 1', 'Calle2')}

print("Conjunto vacío:",conj_uno)
print("Conjunto str:",conj_dos)
print("Conjunto combinado:",conj_tres)
print("Conjunto combinado:",conj_cuatro)
print("")

print("Iteración de elementos:")
#Acceso a elementos
conj_cinco = {1,2,5,6,9}
for i in conj_cinco:
    print(i, end=' ')
print()

############################################################################################################################################
######################################################################

######################################################################
######################################################################
######################################################################









