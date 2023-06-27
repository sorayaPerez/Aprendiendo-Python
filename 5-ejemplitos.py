"""Introduccion """


#Clases y Objetos
#Definiendo nuestra primera clase
class Persona:
    nombre = "" #Atributo de clase
    edad = 0 #Atributo de clase

    # Para poder inicializar el objeto voy a necesitar al objeto mismo (self) y dos datos más
    # que va a ser el nombre y la edad. self es un atributo que permite definir al objeto a sí mismo.
    def inicializar(self, nom, e): # Le damos un estado inicial (es una función dentro de la clase)
        self.nombre= nom #Cuando inicialice quiero que cambie su nombre (self) por el nombre que le pasamos
        self.edad= e

    def imprimir(self):
        print(f'Nombre: {self.nombre}') #Mostramos la información del propio objeto: nombre

    def mayor_edad(self):
        if self.edad>=18:
            print(f'{self.nombre} es mayor de edad, tiene {self.edad}')
        else:
            print(f'{self.nombre} es menor de edad, tiene {self.edad}')
 
# Programa principal 
# Instanciar (crear) el objeto de tipo Persona
persona1= Persona() # Llamamos a la clase y creamos el objeto
persona1.imprimir() # El Nombre está vacío
persona1.inicializar("Juan Pablo", 25) # No es necesario pasar el self 
persona1.imprimir() # No tengo que pasarle un parámetro porque Python entiende que debo usar los propios datos del objeto

persona2= Persona() # Es otra persona creada a partir de la misma clase, otra instancia, otro objeto
persona2.inicializar("Carla", 33) # El cambio de estado está asociado a este objeto
persona2.imprimir() 

persona3= Persona()
persona3.inicializar("Pedro", 15)
persona3.imprimir()
persona1.mayor_edad()
persona2.mayor_edad()
persona3.mayor_edad() 




'''
Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)
'''

class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f'Coordenada del punto: ({self.x}:{self.y})'

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0: 
            print("Primer cuadrante")
        elif self.x<0 and self.y>0: 
            print("Segundo cuadrante")
        elif self.x<0 and self.y<0: 
            print("Tercer cuadrante")
        else: 
            print("Cuarto cuadrante")

# Bloque principal
punto1=Punto(10,5)
punto2=Punto(-5,30)
punto3=Punto(-10,-30)
punto4=Punto(10,-15)

print(punto1)
punto1.imprimir_cuadrante()

print(punto2)
punto2.imprimir_cuadrante()

print(punto3)
punto3.imprimir_cuadrante()

print(punto4)
punto4.imprimir_cuadrante()


#(Adicional 2)

class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion: "))
            if opcion==1: 
                self.cargar()
            elif opcion==2: 
                self.listar()
            elif opcion==3: 
                self.notas_altas()
            elif opcion==4: 
                self.finalizar()
            else: 
                print("Opción no válida!")

    def cargar(self):
        for x in range(5):
            nombre=input("Ingrese nombre del alumno: ")
            self.nombres.append(nombre)
            nota=int(input("Nota del alumno: "))
            self.notas.append(nota)

    def listar(self):
        print("Listado completo de alumnos")
        print(f'Alumno\tNota')
        for x in range(5):
            print(f'{self.nombres[x]}\t{self.notas[x]}')
        print()

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        print(f'Alumno\tNota')
        for x in range(5):
            if self.notas[x]>=7:
                print(f'{self.nombres[x]}\t{self.notas[x]}')
        print()    

    def finalizar(self):
        print("Adiós!")
        print()

# Bloque principal
alumnos=Alumnos()
alumnos.menu()


#(POO 1)


class Persona: # Creamos la clase (sustantivo 1° letra mayúscula)

    piernas = 2 # Atributo de clase

    def inicializar(self, nombre): # Método constructor
        self.nombre = nombre # Atributo de instancia

    def imprimir(self): # Método para mostrar datos
        print(f'Nombre: {self.nombre}')

# Programa principal
persona1 = Persona() # Creamos un objeto basadoe en la clase Persona
persona1.inicializar("Juan Pablo") # Llamamos al constructor con un nombre
persona1.imprimir() # Mostramos los datos

persona2 = Persona()
persona2.inicializar("Julieta")
persona2.imprimir()

print(persona1.nombre,"tiene",persona1.piernas,"piernas")
print(persona2.nombre,"tiene",persona2.piernas,"piernas")


#(POO 2)


class Alumno:
    
    def inicializar(self, nombre, nota): # Constructor
        self.nombre = nombre # Atributo de instancia
        self.nota = nota # Atributo de instancia
    
    def imprimir(self): # Método para mostrar datos
        print(f'{self.nombre} se sacó un {self.nota}')
    
    def mostrar_estado(self): # Método para ver el estado del alumno
        if self.nota >= 7:
            print(f'{self.nombre} promocionó')
        elif self.nota >= 4:
            print(f'{self.nombre} rinde final')
        else:
            print(f'{self.nombre} desaprobó')
        print()

#Programa principal
alumno1 = Alumno() # Creamos el objeto
alumno1.inicializar("Juan", 8)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2 = Alumno() # Creamos el objeto
alumno2.inicializar("Luisa", 4)
alumno2.imprimir()
alumno2.mostrar_estado()

alumno3 = Alumno() # Creamos el objeto
alumno3.inicializar("Diego", 2)
alumno3.imprimir()
alumno3.mostrar_estado()



#(POO 3)


class Animal:

    def __init__(self, nombre, tipo, edad): # Permite instanciar y agregar valores a los atributos
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
    
    def imprimir(self):
        print(f'Tipo: {self.tipo}\nNombre: {self.nombre}\nEdad: {self.edad} años.')

    def __str__(self): # Reemplaza al método imprimir
        return f'Tipo: {self.tipo}\nNombre: {self.nombre}\nEdad: {self.edad} años.'

    def __del__(self): # Elimina el objeto
        print(f'{self.nombre} ha sido eliminado')

# Programa principal
mi_animal1 = Animal("Lassie", "Perro", 11)
# mi_animal1.imprimir()
print(mi_animal1)

print()
mi_animal2 = Animal("Dumbo", "Elefante", 35)
print(mi_animal2)
# del mi_animal2




#(POO 4)

class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor: "))
        self.valor2=int(input("Ingrese segundo valor: "))
        # self.chequear_division()
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma=self.valor1+self.valor2
        print(f'La suma es: {suma}')

    def restar(self):
        resta=self.valor1-self.valor2
        print(f'La resta es: {resta}')

    def multiplicar(self):
        producto=self.valor1*self.valor2
        print(f'El producto es: {producto}')

    def dividir(self):
        self.chequear_division()
        division=self.valor1/self.valor2
        print(f'La division es: {division}')

    def chequear_division(self):
        while self.valor2 == 0:
            self.valor2=int(input("El segundo valor no puede ser cero. Ingrese segundo valor: "))

# Bloque principal
operacion1 = Operacion()







