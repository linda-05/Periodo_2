class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "Hace un sonido"

# Clase Perro hereda de Animal
class Perro(Animal):
    def sonido(self):
        return "Ladra"

# Uso
perro = Perro("Bobby")
print(perro.nombre)       # Salida: Bobby
print(perro.sonido())     # Salida: Ladra
