# print("****** CADENAS DE CARACTERES ******")

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
# cadena10="Python"
# print(max(cadena10))
# print(min(cadena10))

#Comparacion codigo ASCII


######################################################################

# print("****** CADENAS: METODOS ******")

# #Join 
# cade= "Soraya"
# print(cade)
# na= "..".join(cade)
# print(na)



# #Split
# cadena11 = "Cadena de caracteres"
# cadenaLista= cadena11.split(" ")
# print(cadenaLista) #Separa cada palabra en elementos. Se armo un vector identificando los espacios
# print(cadenaLista[2]) #ya lo toma como vector



#Replace
# cadena12= "Ya no se que poner. Mucho texto no es"
# print(cadena12)
# print(cadena12.replace("no","si")) #Me reemplaza los dos no
# print(cadena12.replace("no","si",1)) 



#Count e Index

# cadena13= "Ya no se que poner. Mucho texto no es"
# print("Cantidad de no:",cadena13.count("no"))
# print("Priner no:",cadena13.index("no")) #Te dice donde esta



# #isalpha / isdigit / isalnum

# cadena14 = "Python"
# cadena15 = "Pthon2"

# print(cadena14.isalpha()) # True:son todas letras
# print(cadena15.isalpha()) # False son letras y numeros

# cad1= "1234325"
# cad2="121312412dsgsdgsdg"
# cad3=""
# # print(cad1.isdigit()) # true
# # print(cad2.isdigit()) # false 
# # print(cad3.isdigit())

# print(cad1.isalnum()) # true
# print(cad2.isalnum()) # true
# print(cad3.isalnum()) # false




#isupper / islower

# cad4= "Python"
# cad5="pthon"

# print(cad4.isupper()) #False
# print(cad4.islower()) #False
# print(cad5.isupper()) #False
# print(cad5.islower()) # True



#center / ljust / rjust / zfill

# cad4= "Python"
# cad5 = cad4.center(16,"/")
# print(cad5)

# cad5 = cad4.ljust(16,"-")
# print(cad5)

# cad5 = cad4.rjust(16,"-")
# print(cad5)




#lstrip / rstrip / strip

#lstrip quita elementos de la izquierda
# cad= "--Hola Python- izquierda---"
# print(cad.lstrip("-"))

# #rstrip quita elementos de la derecha
# print(cad.rstrip("-"))

# #strip quita elementos de ambos lados
# print(cad.strip("-"))




#find y rfind

# Si no lo encuentra devuelve -1.
# cad="soraa perezosa"
# print(cad.find("perezosa")) #atras pa delante
# print(cad.rfind("soraa")) #primer posocion


############################  f-strings ##########################################


# curso= "Full Stack Pthon"
# alumna= "Soraya Perez"
# print("Esta estudiando",curso,"la alumna",alumna)
# print(f"Esta estudiando {curso} la alumna {alumna}")


# #f-strings: ejemplo 2: números
# base = 4
# altura = 5
# area = (4*5)/2
# print(f'Base: {base}\nAltura: {altura}\nÁrea del triángulo: {area}')
# print()

# #f-strings: ejemplo 3
# legajo = 12345
# nombre = "Pablo"
# apellido = "Picasso"
# notas = [8, 7, 3]
# promedio =sum(notas)/len(notas)

# print(f"Legajo: {legajo}\nNombre completo: {apellido}, {nombre}\nNotas: {notas[0]}, {notas[1]}, {notas[2]}\nPromedio: {promedio}")




######################################################################

# print("****** LISTAS ******")

#Creación e impresión de listas

# numeros = [1,2,3,4,5] #Lista de números
# dias = ["Lunes", "Martes", "Miércoles"] #Lista de strings
# elementos = [] #Lista vacía
# sublistas = [ [1,2,3] , [4,5,6] ] # lista de listas


#Acceso a elementos

# dias = ["Lunes", "Martes", "Miércoles"]
# print(dias)
# print(dias[0])
# print(dias[1])
# print(dias[-1])
# print(dias[3])


# Iterar sobre una lista (for)

# lista = ["Shrek 1", "Shrek 2","Shrek 3","Shrek 4"]
# suma = 0
# print(len(lista))

# for peliculas in lista:
#     print(peliculas)


# lista = [2,3,4,5,6]
# suma = 0
# for i in range(len(lista)):
#     suma = suma + lista[i]
# print(suma)



# Iterar sobre una lista (while)

# lista = [2,3,4,5,6]
# suma = 0
# i = 0
# while i < len(lista):
#     suma = suma + lista[i]
#     i = i + 1
# print(suma) # 20




#Desempaquetado de listas

# dias = ["Lunes", "Martes", "Miércoles"]
# d1, d2, d3 = dias
# print(d1)
# print(d2)
# print(d3)



######################################################################

# print("****** LISTAS: Métodos ******")

#Append agrega en la última posición

# lista = [3,4,5]
# lista.append(6)
# print(lista)



#Insert agrega en determinada posición

# # insert(<pos>, <elemento>)
# lista=[3,4,5]
# lista.insert(0,2)
# print(lista)
# lista.insert(3,25)
# print(lista)



#Pop: elimina el ultimo elemento, al no asignar posicion

# lista = [6,9,8]
# lista.pop()
# print(lista)

# lista = [3,4,5]
# lista.pop(1)
# print(lista) #Elimino el 4




#Remove: elimino por su valor

# lista = [3,4,5]
# lista.remove(3)
#Resultado: [4,5]



#Index: devuelve la posición de determinado elemento
# lista = [3,4,5]
# print(lista.index(5))
# print(lista.index(5,1)) #Empieza a buscar desde [1]



#Count: Cuenta las veces que aparece un elemento
# lista = [3,4,5,3,5,8,5]
# print(lista.count(5))
# # Resultado: 3
# print(lista.count(2))
# # Resultado: 0


#Reverse: Da vuelta los valores de una lista
# lista = [3,4,5]
# lista.reverse()
# print(lista)
# # Resulado: [5,4,3]


#Sort: Ordena una lista de menor a mayor
# lista = [5, 1, 7, 2]
# lista.sort()
# print(lista)
# #Resultado: [1,2,5,7]

# mayor a menor
# lista = [5, 1, 7, 2]
# lista.sort(reverse=True)
# print(lista)
# #Resultado: [7,5,2,1]



#Clear: Vacía una lista
# lista = [3,4,5]
# lista.clear()
# print(lista)
# #Resultado: []


######################################################################

# print("****** LISTAS: Operaciones ******")

#Concatenar

# lista1 = [1,2,3]
# lista2 = [4,5,6]
# lista3 = lista1 + lista2
# print(lista3)



#Intercambiar valores




# Len, Suma, máximo, mínimo y promedio

# lista = [3,4,5,6]
# print(len(lista))
# print(max(lista))
# print(min(lista))
# print(sum(lista))
# print((sum(lista)/len(lista)))



#Operadores de pertenencia 

# lista = list(range(6))
# print(lista)
# cadena = "Hola"
# print(list(cadena))
# lista2 = [3,4,5,6]
# print(4 in lista2) #true
# print(8 in lista2) # falsde
# print("A" not in lista2) #t



######################################################################

# print("****** DICCIONARIOS ******")

# #Creación de diccionarios (por extension)
# vacio = {} 			                # diccionario vacío
# dicc_uno = {'Juan': 56}			    # diccionario de un elemento
# dicc_dos = {'Juan': 56, 'Ana': 15}  # diccionario de dos elementos
# print(vacio)
# print(dicc_uno)
# print(dicc_dos)
# print()

# #Creación de diccionarios (por compresion)
# diccionario = {x: x ** 2 for x in (2, 4, 6)}



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
# print(tupla_dos[::]) # Acceso mediante rebanadas

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









