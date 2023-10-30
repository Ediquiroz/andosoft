# class Estudiantes:
#     def __init__(self, id, nomb, tipo_sangre):
#         self.identificacion=id
#         self.nombre=nomb
#         self.__tipo_sangre=tipo_sangre
#         self._tipo_sangre=tipo_sangre
        
#     def obtener_tipo_sangre(self):
#         return self.__tipo_sangre
    
#     def modificar_tipo_sangre(self, tipo_sangre):
#         if tipo_sangre=="a+":
#             self.__tipo_sangre=tipo_sangre

# est1=Estudiantes(1,"Sofonias","0+")

# print("ID: ", est1.identificacion, "Nombre: ", est1.nombre, "Tipo sangre: ", 
#       est1.obtener_tipo_sangre())
# est1.modificar_tipo_sangre("a+")
# print("ID: ", est1.identificacion, "Nombre: ", est1.nombre, "Tipo sangre: ", 
#       est1.obtener_tipo_sangre())

# class Persona:
#     def saludar(self, nombre):
#         print("Hola", nombre)
#         print(self)

# p=Persona()
# p.saludar("Aqui Toy")

# p1=Persona()
# p1.saludar("Pablo Pinto")

# class Persona:
#     def __init__(self, ced, nom, ed):
#         print("Quien quiere salir a descanso", self)
#         self.cedula=ced
#         self.nombre=nom
#         self.edad=ed
        
# obj1=Persona(123, "juanito", 19)
# obj2=Persona(345,"pedrito", 22)

# print(obj1.cedula, obj1.nombre, obj1.edad)
# print(obj1)
# print(obj2.cedula, obj2.nombre, obj2.edad)
# print(obj2)

# class Persona:
#     def __init__(self, nombre, edad, ciudad):
#         self.nombre=nombre
#         self.edad=edad
#         self.ciudad=ciudad
        
#     def mostrar_informacion(self):#Mediante el self el método reconoce
#         #al objeto que esta invocando el método
#         print("El nombre es ", self.nombre, self.edad, self.ciudad)
        
# pepita=Persona("Pepita Mirasoles", 23, "Manizales")
# pepito=Persona("Pepito Gonzales", 20, "Medellin")

# pepita.mostrar_informacion()
# pepito.mostrar_informacion()

class Persona:
    def __init__(self, n, e, c):
        self.nombre=n
        self.edad=e
        self.ciudad=c
        
    def cumplir_anos(self):
        self.edad+=1
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, x):
        self.edad=x
    
    def puede_votar(self):
        if self.edad>=18:
            return True
        else:
            return False
    
    def cambiar_ciudad(self, nueva_ciudad):
        self.ciudad=nueva_ciudad
    
    def mostrar_info(self):
        print(f"{self.nombre} tiene {self.edad} y vive en {self.ciudad} y puede votar???{self.puede_votar()}")
    
   
pepita=Persona("Pepita Mirasoles", 23, "Manizales")
pepito=Persona("Pepito Gonzales", 20, "Medellin")

pepita.mostrar_info()
pepita.cumplir_anos()
pepita.cambiar_ciudad("Medellin")
pepita.mostrar_info()









    