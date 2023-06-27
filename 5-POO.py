'''
1. Implementar una clase llamada Estudiante que tendrá como atributos (variables)
su nombre, su apellido, dni y dos métodos (funciones), uno de dichos métodos
inicializará los atributos y el siguiente método los mostrará en pantalla.
Definir dos objetos de la clase Estudiante e incorporar una variable de clase (hijos).

'''
# Clase (molde de galletas): La clase define de forma genérica cómo son las personas, con sus atributos y métodos
class Estudiante: # Creamos la clase (sustantivo 1° letra mayúscula)

    hijos = 2 # Atributo / variable de clase la dif con los de abajo es que vale 
    # PARA TODOS LOS OBJETOS LO MISMO
    # Es el "por defecto"

    #Metodos: acciones que el objeto puede hacer 
    def inicializar(self, nombre, apellido, dni): # Método constructor
        self.nombre = nombre #  SELF Atributo de instancia (Momento en cual se crea la clase, referencia al objeto que vas a crear que luego llama al metodo). Vas inicializando los demas atributos (appelido,nombre,dni)
        self.apellido = apellido # Atributo de instancia
        self.dni = dni # Atributo de instancia
    #Metodo
    def imprimir(self): # Método para mostrar datos, por eso no recibe ningun parametro
        print(f'Apellido y nombre: {self.apellido.upper()}, {self.nombre}\nDNI: {self.dni}')

# Programa principal
estud1 = Estudiante() # Creamos un objeto basado en la clase Estudiante (Toma el metodo de ini y imprimir)
#estyd1. Aca ya podes ingresas a los metodos y atributos
estud1.inicializar("Pepe", "Argento", 12345678) # Llamamos al constructor con un nombre
estud1.imprimir() # Mostramos los datos

estud2 = Estudiante() 
estud2.inicializar("Luciana", "Pérez", 31234567)
estud2.imprimir() 

print(f'Los estudiantes tienen {Estudiante.hijos} hijos.')
print(f'{estud1.nombre} tiene {estud1.hijos} hijos.')
print(f'{estud2.nombre} tiene {estud2.hijos} hijos.')

print()
#Pisas el valor
estud1.hijos = 4 #Modifico el atributo hijos solo para estud1
print(f'{estud1.nombre} tiene {estud1.hijos} hijos.') # 4 hijos
estud2.nombre = "Fernanda" #Modifico el atributo nombre solo para estud2
print(f'{estud2.nombre} tiene {estud2.hijos} hijos.') # 2 hijos

estud1.edad = 37 # Atributo de instancia
print(estud1.edad)
print(estud2.edad) # Error, no tiene ese atributo

# Si modificas un atributo a la clase, pasa a modificar a todos.





'''
2. Implementar una nueva clase llamada Estudiante. Esta clase tendrá como atributos 
su nombre y su nota. Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje que indique: “Promocionó” (nota >= 7),
“Rinde final” (nota >= 4) o “Desaprobó”.
Definir tres objetos de la clase Alumno, cada uno con una condición
de aprobación distinta.

'''

class Estudiante: 

    def inicializar(self, nombreCompleto, nota): # Método constructor
        self.nombreCompleto = nombreCompleto # Atributo de instancia
        self.nota = nota # Atributo de instancia
    
    def imprimir(self): # Método para mostrar datos
        print(f'Nombre completo: {self.nombreCompleto.title()} - Nota: {self.nota}')
        if self.nota >= 7:
            print("Promocionó")
        elif self.nota >= 4:
            print("Rinde final")
        else:
            print("Desaprobó")
        print()


# Programa principal

estud1 = Estudiante() # Creamos el objeto 1 
estud1.inicializar("Juan Serrano", 8)
estud1.imprimir()

alumno2 = Estudiante() # Creamos el objeto 2 
alumno2.inicializar("Luisa López", 4)
alumno2.imprimir()

alumno3 = Estudiante() # Creamos el objeto  3
alumno3.inicializar("Diego Fernández", 2)
alumno3.imprimir()





'''
3. Crear una clase que represente una Materia de la universidad. Definir como atributos su nombre, carrera, duración en meses y un atributo de clase booleano para definir que todas las materias no son promocionables. Desarrollar un método __init__ para incializarlos. Crear un método para imprimir los datos del objeto, luego sustituirlo por el método __str__(). Crear dos objetos. Eliminar uno de ellos a través del método __del__().

'''

class Materia: 
    promo = False #Atributo de clase
    
    # Nuevo método constructor
    def __init__(self, nombre, carrera, duracion): # Permite instanciar y agregar valores a los atributos
        self.nombre = nombre
        self.carrera = carrera
        self.duracion = duracion
        
    def imprimir(self):
        print(f'Materia: {self.nombre.title()}\nCarrera: {self.carrera.upper()}\nDuración: {self.duracion} meses\nPromocionable: {self.promo}')

    def __str__(self): # Reemplaza al método imprimir
        return f'Materia: {self.nombre.title()}\nCarrera: {self.carrera.upper()}\nDuración: {self.duracion} meses\nPromocionable: {self.promo}'

    def __del__(self): # Elimina el objeto
        print(f'{self.nombre} ha sido eliminada')

# Programa principal
materia1 = Materia("introd. a python", "ing. en informática", 4) #Creas el obj al determinale la clase
#y ya le estas pasando valores
materia1.imprimir()
#print(materia1) ##te muestra la direccion de memoria sonde tene guardado el objt, no te imprime lo que queres y no usas esto alumno2.imprimir()
print()
materia2 = Materia("inteligencia artificial", "ing. en informática", 8)


print(materia2)
print()


del materia2   #Queres eliminar materia2 
print(materia2) #para ver que lo eliminaste




'''
Integrador- Implementar una clase llamada Empleado, que posee un atributo de clase (nro_empleados) que lleva la cuenta de los objetos instanciados.
Cada objeto de la clase Empleado posee un legajo, nombre completo y un sueldo.
Definir métodos para inicializar sus atributos, definir su categoría (variable de clase), procesar su eliminación de la memoria y para mostrar un texto con la categoría asignada.
La categoría es "Full Time" para los legajos comenzados en "F", "Part time" para los legajos comenzados en "P" y "Contratado" para los comenzados en "C", para el resto la categoría es vacía.
En el programa principal instanciar distintos objetos de la clase Empleado y mostrar sus características encolumnadas. Al salir del programa eliminarlos de la memoria.

'''

class Empleado:  # Creamos la clase
    nro_empleados = 0  # Cantidad de empleados (atributo de clase)
    categoria = ""

    # Constructor
    def __init__(self, legajo, nombreCompleto, sueldo):
        self.legajo = legajo
        self.nombreCompleto = nombreCompleto
        self.sueldo = sueldo
        Empleado.nro_empleados += 1  # Agregamos un empleado

    # Mostrar datos del objeto
    def __str__(self):
        inicial_legajo = self.legajo[0] #Primera inicial del legajo
        #Los strings se tratan como vectores. Accede a la primer letra de la palabra

        if inicial_legajo == "F":
            self.categoria = "Full Time"
        elif inicial_legajo == "P":
            self.categoria = "Part time"
        elif inicial_legajo == "C":
            self.categoria = "Contratado"

        cadena = f'{self.legajo}\t{self.nombreCompleto}\t{self.sueldo}\t{self.categoria}'
        
        return cadena

    def titulos():
        print(f'Legajo\tNombre Completo\tSueldo\tCategoria')

    # Damos de baja al empleado (A TODOS)
    def __del__(self):
        Empleado.nro_empleados -= 1  # Restamos un empleado
        print(f'{self.nombreCompleto} ha sido dado de baja - Restan: {Empleado.nro_empleados}')
        del self

# Programa principal
emp1 = Empleado("F1000", "Juan Pérez", 150000)
emp2 = Empleado("P1001", "Ana Gómez", 240000) #dos empleados
emp3 = Empleado("C1002", "Luciano García", 130000) #tres
emp4 = Empleado("H1003", "Marcela Priore", 220000) #cuatro

Empleado.titulos()
print(emp1)
print(emp2)
print(emp3)
print(emp4)
print()
input("Pulse Enter para salir: ")
print()
del emp1
print(emp1)



#(Ejercicio integrador2 POO)


class Producto:  # Creamos la clase
    nro_productos = 0  # Cantidad de productos
    categoria = ""

    # Constructor
    def __init__(self, descripcion, precio):
        self.descripcion = descripcion
        self.precio = precio
        Producto.nro_productos += 1  # Agregamos un producto

    # Mostrar datos del objeto
    def __str__(self):
        return f'Descripción: {self.descripcion} - Precio $ {self.precio}'

    # Damos de baja al producto
    def __del__(self):
        Producto.nro_productos -= 1  # Restamos un producto
        print(f'Producto {self.descripcion} dado de baja - Restan: {Producto.nro_productos}')
    
    def mostrar_categoria(self):  # Categoría del producto según precio
        print(f'La categoría del producto {self.descripcion} es:', end=' ')
        if self.precio >= 100:
            print("A")
        elif self.precio >= 50:
            print("B")
        else:
            print("C")

# Programa principal
producto1 = Producto("Azúcar", 120)
producto2 = Producto("Mayonesa", 80)
producto3 = Producto("Caramelos", 30)

print(producto1)
print(producto2)
print(producto3)

producto1.mostrar_categoria()
producto2.mostrar_categoria()
producto3.mostrar_categoria()

input("Pulse enter para salir")


