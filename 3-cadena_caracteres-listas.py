print("****** CADENAS DE CARACTERES ******")

##### Escritura y concatenación

# print()
# cadena1= "Aprendiendo cadena de caracteres "
# cadena2= "en VScode "

# print(cadena1)
# print(cadena2)
# print()

# print(cadena1+cadena2+"un domingo")  # Concatenando
# #Si pones , en vez de mas te pone los espacios solos



###### Combinar comillas simples y dobles

# print("Hoy quiero comer ¨poco¨ ")
# #Para usar comillas dentro de un print
# #tenes que usar comillas chiquitas 
# # shift y coma (al lado de enter)



##### Concatenar números y cadenas de caracteres

# # Te va a saltar error
# edad=25
# altura= 1.78
# datos = "La edad es " + edad
# print(datos)

# # Hay que parsear
# edad=25
# altura= 1.78
# datos = "La edad es " + str(edad)
# print(datos)




##### Replicación de cadenas

# risita = "ja"
# print(risita)
# carcajada= risita*5
# print(carcajada)

# print("-"*40)  # CLAVE



# ##### Cadenas multilínea

# cadena3= """
# Cadena
# en mas de 
# una linea
# """
# print(cadena3)

# # Es como esto 

# """" sadsadasdas asdsad
# asdasdsadsadsa
# asdasdasdsadasd
# asdasd """




##### Comparación de cadenas (ASCII y case sensitive)

# cadena4 = "@" #alt +64
# cadena5= "^"
# cadena6 ="@"

# print(cadena4 < cadena6)
# #Devuelve FALSE porque chequea que Nº simboliza en el codigo ACII

# print(cadena4 == cadena6)


# #Como pusiste la tilde hace diferencia
# # Es Case sensitive porque el codigo ASCII
# # Toma con un valor distinta la ó  la o

# ciudad= "Córdoba"

# if ciudad == "Cordoba":
#     print("El envio llega mañana")
# else:
#     print("El envio llega el Lunes")




##### Largo de cadenas y subíndices

# nombre= "Soraya Perez"
# print(len(nombre))

# print(nombre[0])
# print(nombre[-1]) # Version minimizada
# print(nombre[len(nombre)-1])



##### Métodos upper / lower / capitalize / title


# cadena7="Soraya Maite Perez uuuuuuuu"

# print(cadena7.upper())
# print(cadena7.lower())
# print(cadena7.capitalize())
# print(cadena7.title())




##### Rebanadas (slicing)
# [:] Todos los elementos de la cadena.

# cadena8= "Vamos por partes dijo Jack"
# print(cadena8[:])

# # [start:] Todos los elementos desde el índice establecido(start). 

# #Del 12 en adelante
# print(cadena8[12:])

# # [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
# print(cadena8[:3])

# # [start:end] Todos los elementos de un rango de índices.
# print(cadena8[12:20])

# # [start:end:step] Todos los elementos de un rango de índices con saltos.
# print(cadena8[6:20:2])

# # [::step] Todos los elementos con saltos.
# print(cadena8[::2])

# # [::step] Todos los elementos con saltos (negativo). Desde atras para adelante
# print(cadena8[::-1])


###### Operadores de pertenencia: in / not in

# cadena9="Python a la mesa"
# print("a" in cadena9) # true
# print("A" in cadena9) # false
# print("mesa" in cadena9) #true

# print("D" not in cadena9) #true
# print( "")



# ###### Iterando cadenas


# #For: recorres la cadena
# # Inicializa ya con la i = 0

# cadena10="Python"
# for i in cadena10:
#     print(i, end=" ")

# print()
# for i in cadena10:
#     print(i, end="") 


#While
# Tenes que definir i para poder usarla
# Tenes que sumarle posiciones 

# cadena10="Python"
# i=0
# while i < len(cadena10):
#     print(cadena10[i])
#     i += 1

# Mientras i sea menor a la cantidad de elementos que tenga la cadena metete dentro del while, imprimime la letra de esa posicion



#Uso de min y max

#Queres saber cual es el caracter mas grande
cadena10="Python"
print(max(cadena10))
print(min(cadena10))

#Comparacion codigo ASCII


######################################################################

# print("****** CADENAS: METODOS ******")

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

# print("****** LISTAS ******")

#Creación e impresión de listas

#Acceso a elementos

# Iterar sobre una lista (for)

# Iterar sobre una lista (while)


#Desempaquetado de listas

#Desempaqueto la lista 2 en los 3 elementos



######################################################################

# print("****** LISTAS: Métodos ******")

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

# print("****** LISTAS: Operaciones ******")

#Concatenar



#Modificar valores por posición


#Intercambiar valores


#len (largo de la lista)



#Suma, máximo, mínimo y promedio



#list 



######################################################################

# print("****** DICCIONARIOS ******")

# #Creación de diccionarios
# vacio = {} 			                # diccionario vacío
# dicc_uno = {'Juan': 56}			    # diccionario de un elemento
# dicc_dos = {'Juan': 56, 'Ana': 15}  # diccionario de dos elementos
# print(vacio)
# print(dicc_uno)
# print(dicc_dos)
# print()

# #Acceder a elementos
# print(dicc_dos.items()) #Mostramos los pares clave-valor
# for clave, valor in dicc_dos.items(): #otra manera de mostrar los pares clave-valor
#     print(f'{clave}: {valor}')

# print(dicc_dos.keys()) #Mostramos las claves
# for i in dicc_dos.keys(): #Mostramos los valores
#     print(dicc_dos[i], end=' ')
# print()

# #Modificar elementos
# print("Edad de Juan:",dicc_dos["Juan"]) #Valor que corresponde a la clave "Juan"
# dicc_dos["Juan"] = 37
# print("Nueva edad de Juan:",dicc_dos["Juan"]) 

# #Agregar elementos
# dicc_dos["Pablo"] = 12
# dicc_dos["Julieta"] = 26
# print(dicc_dos)
# dicc_dos["Pablo"] = 47 #No agrega un nuevo "Pablo", sino que modifica el existente
# print(dicc_dos)
# print()

# #Otra forma de acceder a elementos y mostrarlos: listas
# lista_claves = list(dicc_dos.keys()) # Le pido al dicc sus claves y lo convierto a lista
# lista_valores = list(dicc_dos.values())

# for i in range(len(lista_claves)):
#    print(lista_claves[i],"tiene",lista_valores[i],"años") #Imprimimos valores
# '''
# '''

# ######################################################################

# print("****** TUPLAS ******")

# #Creación de tuplas
# vacia = () # tupla vacía
# tupla_uno = 'Juan Pablo', # tupla con un valor
# tupla_dos = ('Juan', 37, False) # mixtas
# tupla_tres = 'Luciana', 56, (1998,5,26) # Tupla anidada
# tupla_cuatro = ('Rivadavia', 3567, ['Calle 1', 'Calle2']) # Tupla con lista

# print(vacia)
# print(tupla_uno)
# print(tupla_dos)
# print(tupla_tres)
# print(tupla_cuatro)
# print()

# #Acceso a elementos
# print(tupla_dos[0]) 
# print(tupla_tres[2]) 
# print(tupla_cuatro[1]) 
# #tupla_dos[0] = "Pablo" # Error
# print()

# #Otra forma de crear una tupla: empaquetar
# nombre= 'Carlos'
# apellido= 'Rodriguez'
# datos= nombre,apellido,32
# print(datos) 
# print(type(datos))
# print()

# #También podemos desempaquetar una tupla para acceder a sus datos
# fecha= (7, "noviembre", 2022)
# print(fecha)
# dd,mm,aa= fecha
# print("Dia:",dd)
# print("Mes:",mm)
# print("Año:",aa)
# print()

# ######################################################################

# print("****** CONJUNTOS ******")

# #Creación de conjuntos
# conj_uno = set()
# conj_dos = {'Juan','Juan'}
# conj_tres = {'Pablo', 3456, True}
# conj_cuatro = {'Rivadavia', 3567, ('Calle 1', 'Calle2')}

# print("Conjunto vacío:",conj_uno)
# print("Conjunto str:",conj_dos)
# print("Conjunto combinado:",conj_tres)
# print("Conjunto combinado:",conj_cuatro)
# print("")

# print("Iteración de elementos:")
# #Acceso a elementos
# conj_cinco = {1,2,5,6,9}
# for i in conj_cinco:
#     print(i, end=' ')
# print()

############################################################################################################################################
######################################################################

######################################################################
######################################################################
######################################################################









