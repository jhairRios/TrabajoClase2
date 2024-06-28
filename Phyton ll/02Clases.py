import os
os.system('cls' if os.name == 'nt' else 'clear')
#clases y objetos
class Persona:
    especie ="humano"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}')
    def cumplir_anios(self, estado_humor):
        print(f'tengo {self.edad + 1} años me pone {estado_humor}')
        
juan = Persona("Juan", 37)
juan.saludar()
juan.cumplir_anios("feliz")

#imprimiir solo el nombre
print(juan.nombre)
#imprimiir solo la edad
print(juan.edad)
