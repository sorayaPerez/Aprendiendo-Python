'''
Ejercicio 1: Crear un programa que permita registrar las inscripciones de los alumnos de una universidad privada. Debe incluir un título principal, pedir los datos personales (nombre, edad, fecha de nacimiento). Crear una variable que muestre True o False si posee título secundario (ese dato no se pide al usuario, se escribe en el programa).
Además se deberá ingresar el monto de matrícula y calcular la cuota (valor de la matrícula + $ 2000 de cuota).
Finalmente se deberán imprimir todos los datos pedidos.
'''

# print()
# print("==========================================================")
# print("==================== Inscripcion de alumnos =================")
# print("==========================================================")

# nombre_completo= input("Ingrese nombre del alumno:")
# edad= int(input("Ingrese edad del alumno : "))  #Aca pasa a ser un string,lo cabias a entero
# fechaDeNacimiento= input("Ingrese fecha de nacimiento del alumno: ")
# titulo = True #se escribe en el programa

# montoMatricula= (input("El monton de la matricula es: ")) 
# montoMatricula=float(montoMatricula)  #Nº con coma
# print(type(montoMatricula)) 

# #Mostras datos

# print()
# print("==========================================================")
# print("====================== Bienvenido ====================")
# print("==========================================================")

# print()
# print("DATOS DE INGRESO:")
# print("Nombre completo:", nombre_completo)
# print("Fecha de nacimiento:", fechaDeNacimiento)
# print("Edad:"+ str(edad))
# print("Posee título?:", titulo)

# print("El monto de la matricula es: $",montoMatricula, "la cuota sale $ 2000 por lo que el monto total es",montoMatricula+2000 )



'''
Ejercicio 2: La universidad ahora pide un programa que permita cargar las notas de dos exámenes y obtener el promedio. Además deberá determinar si el alumno aprobó el último examen (nota mayor o igual a 7), en caso contrario informar que desaprobó.
Además se desea saber si el alumno mejoró, empeoró o mantuvo su desempeño entre ambos parciales. Para ello se deberá informar "Mejoró su desempeño" si la nota del segundo parcial es mayor que la del primero, "Mantuvo la nota" si ambas notas son iguales o "Empeoró su desempeño" si la nota del primer parcial es mayor que la del segundo.
Finalmente, la universidad desea saber si el alumno promocionó la materia (promedio mayor o igual a 7), debe rendir final (promedio mayor o igual a 4) o debe recursar.

'''

# print()
# print("==========================================================")
# print("====================== Bienvenido ====================")
# print("==========================================================")

# primerParcial= float(input("Ingrese nota del primer parcial:"))
# segundoParcial= float(input("Ingrese nota del segundo parcial:"))
# promedio= (primerParcial+segundoParcial)/2
# print()
# print("El promedio de las notas es:", promedio)


# if (segundoParcial >= 7):
#     print("El alumno aprobó el segundo parcial con una nota igual o mayor a siete")
# else: print("El alumno desaprobó el segundo parcial con una nota menor a siete")

# if(segundoParcial>primerParcial):
#     print("Al mismo tiempo el alumno mejoro su rendimiento")
# elif(segundoParcial == primerParcial):
#     print("Al mismo tiempo el alumno mantuvo su rendimiento")
# else:
#     print("Al mismo tiempo el alumno redujo su rendimiento")


# if(promedio >= 7):
#     print("Por lo que el alumno promociono")
# elif(promedio >=4):
#     print("Por lo que el alumno debe rendir final")
# else:
#     print("El alumno debe recursar")


# print(f'Progreso del 1er al 2do parcial: {estado}')


# print()
# print("==========================================================")
# print("====================== Notas ====================")
# print("==========================================================")



'''
Ejercicio 3: La universidad requiere un programa para organizar las aulas para los alumnos de primer año, de acuerdo al número de día, sabiendo que 1 es lunes y 6 es sábado.
Desarrollar un programa que permita ingresar el número de día entre 1 y 6. Los días cuyo número de orden son pares los alumnos cursan en el aula A-300, mientras que aquellos días impares cursan en el aula A-315.
Además se requiere un programa que otorgue un descuento especial del 25% en el valor de la cuota a aquellos alumnos que deseen cursar en el turno Tarde y se inscriban a más de 3 materias, para el resto de los casos el descuento será de un 5%. El programa debe imprimir el valor de la cuota con descuento de acuerdo al caso.
También se requiere que el programa asigne un costo diario de estacionamiento de $ 300 a aquellos alumnos que vengan en auto o en moto y de $ 50 si vienen en bicicleta.
'''
# lunes = 1
# martes =2
# miercoles =3
# jueves = 4
# viernes = 5
# sabado = 6


# diaCursado=input("¿Que dia cursas?")

# if diaCursado == lunes or miercoles or viernes:
#     print("Cursas en el aula A-320")
# elif diaCursado == martes or jueves or sabado: #pares
#     print("Cursas en el aula A-300")

# turnoCursado=input("¿Cursas en el turno mañana, tarde o noche?")
# cantidadMaterias = input("¿Cuantas materias cursas?")
# valorCuota=6000

# if turnoCursado == "tarde" and cantidadMaterias >=3: 
#     print("Tenes un descuento del 25porciento al pagar la cuota, quedando un valor de:",str(valorCuota-(valorCuota*0.25)))
# else: print("Tenes un descuento del 5 porciento al pagar la cuota, quedando un valor de:",str(valorCuota-(valorCuota*0.05))) 

# medioTransporte=input("Venis en bicicleta, moto o auto?")

# if medioTransporte == "moto" or "auto":
#     print("Deberas abonar 300 pesos por estacionamiento")
# elif medioTransporte == "bicicleta":
#     print("Deberas abonar 50 pesos por estacionamiento")
# else: print("No deberas abonar nada por estacionamiento")



# Forma mas facil

# print("============== Aulas =============")

# dia = int(input("Ingrese el número del día: 1 (lunes) a 6 (sábado): "))
# if dia % 2 == 0:    # el resto al dividir por 2
#     aula = "A-300"
# else:
#     aula = "A-315"

# print("Aula:", aula)

# print("Aula:", aula)

# print()
# print("============== Descuentos y estacionamiento =============")
# cuota = 10000
# turno = input("Ingrese el turno: Mañana, Tarde o Noche: ")
# materias = int(input("Ingrese la cantidad de materias: "))
# if turno == "Tarde" and materias > 3:
#     cuota = cuota - (cuota * 0.25)
# else:
#     cuota = cuota - (cuota * 0.05)
# print(f'El valor de la cuota es: {cuota}')

# vehiculo = input("Ingrese el vehículo en el que ingresa: Auto, Moto o Bicicleta: ")
# costo_estacionamiento = 0
# if vehiculo == "Auto" or vehiculo == "Moto":
#     costo_estacionamiento = 300
# else:
#     costo_estacionamiento = 50
# print(f'El costo de estacionamiento para {vehiculo} es: ${costo_estacionamiento}')





'''
Ejercicio 4: La universidad ha decidido desarrollar un programa que muestre en dos columnas el número de día y el aula, de acuerdo al número de día par o impar desarrollado en el ejercicio anterior. Imprimir el listado como el siguiente:
Día Aula
1   A-315
2   A-300
...
5   A-315
6   A-300
Además se desea mejorar el sistema de carga de edades, validando que correspondan a mayores de edad. Desarrollar un programa que solicite edades válidas e imprima la edad ingresada y cuántas cargas erróneas se realizaron.
También se requiere cargar las notas de 5 alumnos y obtener el promedio (for). Nota: Al usar for probar cómo se podría plantear el ejercicio usando 1, 2 o 3 parámetros.
Finalmente se desea imprimir el costo del comedor. La cuota vale $ 1250 por día y se desea imprimir un informe que muestre la cantidad de días (de 1 a 6) y el costo total (for). Por ejemplo: 1 día cuesta $ 1250, 2 días cuestan $ 2500...

'''


print("============== Listado de aulas =============")
print("Día\tAula")
cont = 1
while cont <= 6:
    print(cont, end='')
    if cont % 2 == 0:
        print("\tA-300")
    else:
        print("\tA-315")
    cont = cont + 1

print()
print("========== Carga de edades ==========")
carga_erronea = 0
edad = int(input("Ingrese una edad mayor o igual a 18: "))
while edad < 18:
    carga_erronea += 1 #Contador
    edad = int(input("Error! Ingrese una edad mayor o igual a 18: "))
print("La edad ingresada es:", edad)
print("Se ha ingresado la edad erróneamente", carga_erronea,"veces")

print()
print("========== Promedio de notas ==========")
suma = 0
# Alternativa 1 - for i in range(fin):
for i in range(5):
    nota = int(input("Ingrese la nota: "))
    suma = suma + nota #Acumulador, alternativa: suma += nota
promedio = suma/(i+1)
print("El promedio de notas es:", promedio)
# Alternativa 2 - for i in range(inicio, fin):
# for i in range(0,5):

# Alternativa 3 - for i in range(inicio, fin, paso):
# for i in range(0,5,1):

print()
print("========== Costo del comedor ==========")

costo_diario = 1250
print("Dia\tCosto")
for i in range(6):
    print(i+1,"\t$",(i+1)*costo_diario)