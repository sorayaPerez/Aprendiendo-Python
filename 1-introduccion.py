# print("Hola comision 23027")

# """
# Comentario en bloque
# sigue siendo un comentario
# """

# #Comentario en linea


#### Tipos de datos

# # String
# texto ="Estamos aprendiendo python"
# print(texto)
# print(type(texto))

# #Enteros
# valorEntero=4
# print(valorEntero)
# print(type(valorEntero))
# print(valorEntero+9)

# #Decimal
# decimal = 4.9
# print(decimal)
# print(type(decimal))
# print(decimal+1)

# #Booleano
# valor_logico = True
# print(valor_logico)
# print(type(valor_logico))


#### VARIABLES

# # Las variables se sobreescriben (tipado dinamico)
# # No podes sumar string con enteros

# variables
# cadena_string: Esta nomenclatura se utiliza para funciones
# cadenaString: La nomenclatura camelCase se usa para variables


# ####################### Operadores de asignacion

# a=2
# b=3
# suma = a+b
# print(suma)
# print("La suma es",suma)

# #Expresiones
# print(3+2)

# c =10
# print(c < 10)
# print(c is None)

# d = None
# print(d is None)

# e=20
# print(20*(3+1))

# #Despues estan en el resto (/ * -)


# ######################## Sentencias

# print("hola") # una sola linea

# f= 2+3+4+5+8+6 \     # sentencia dividida en lìneas
# + 7 + 6
# print(f)

# f2=[1 + 3+ 5+
#     7+8+9+10]  # continuación de línea implícita
# print(f2)

# ######################## Print

# print()
# print("hola")
# print("mundo")
# print()

# print("hola") # Incluye salto de línea
# print()
# print("mundo")
# print()

# print("Hola ", end="")  #end='' hace que sea continuo y no pegue el salto de línea
# print("en la comisión 12345") # Continúa en la línea anterior
# print("mundo")

# cadena= "Pepe Argento"
# print("Hola",cadena) #, agrega espacio intermedio
# print("Hola"+cadena) #+ no agrega espacio intermedio




# ####################### Separadores

# print(11,12,13, sep="/")
# print(11,12,13, sep="*") #es un asterisco la sepación
# print(11,12,13, sep="")
# print(11,12,13, sep="\t") #es una tabulacion
# print(11,12,13, sep="\n")  #es un salto de línea
# print(11,12,13, sep="\n \n") #es un doble salto de línea
# print(11,12,13, end="/") #termina con una línea en vez de con 1 salto
# print("otra linea")


##################### Input = te lo muestra en terminal

# Tenes que ir a la consola no al gatito (rpl).
#El gatito toma salidas no entradas

# variable = input("Ingrese su nombre: ")
# print("Hola",variable)

# mensaje = "Bienvenido/a al sistema. Ingrese su usuario"
# usuario = input(mensaje)
# print("Hola",usuario)


### Ejemplo 1 


# anio= input("Ingrese el año actual: ")
# print("El año proximo sera: ", anio +1) #tenes que parsear
# Estas concatenando (+) un string (anio) con un dato numerico (+1) 

# Tenes dos opciones o al input lo convertis en entero

# Opcion 1

# anio= int(input("Ingrese el año actual: "))
# print("El año proximo sera: ", anio +1)

# Opcion 2

# anio= input("Ingrese el año actual: ")
# print("El año proximo sera: ", int(anio) +1) #tenes que parsear



### Ejemplo 2

# lado = input("Ingresar el lado del cuadrado: ")
# superficie = lado*lado
# print(superficie)



# lado = int(input("Ingresar el lado del cuadrado: "))
# superficie = lado*lado
# print("La superficie es: "+ superficie) #Error
# print("La superficie es: "+ str(superficie))
# print("La superficie es:", superficie) #Otra forma para combinar string con int



# Cadenas

# dia = "Lunes"
# mes = "Mayo"


# print(dia +mes)
# print(dia ,mes)

# apellido = "Martinez"
# print(apellido[0]) # Te toma appelido como 
# #vector y agarra la primer letra
# print(len(apellido))
# print(apellido[-1]) #Ultimo caracter

#Programa para obtener el primercaracter, el ultimo y 
#el largo de la cadena

# palabra = input("Ingrese su palabra") 
#Toma la cadena como un vector
# primer = palabra[0]  #Devuelve el último valor, pero como nose cuantos datos se pueden ingresar, lo correcto es tomar el len y restarle 1
# ultimo = palabra[-1] #Es -1 porque arranca de 0.
# largo = len(palabra)

# print("La primer letra es",primer,",la ultima es", ultimo, " y el largo de la palabra",palabra,"es", largo)

# nombre_completo = "soraya Maite Perez"
# #Las cadenas son objetos, por lo tanto, tienen métodos
# nombre_completo="carlos Martínez estrada"
# print(nombre_completo.lower()) #minúsculas
# print(nombre_completo.upper()) #mayúsculas
# print(nombre_completo.capitalize()) #primer letra de la cadena
# print(nombre_completo.title()) #primer letra de cada palabra

