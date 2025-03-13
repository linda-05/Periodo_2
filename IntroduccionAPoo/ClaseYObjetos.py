class Persona :
    def __init__(self, nombre, edad) :
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear un objeto (instancia de la clase)
persona1 = Persona("Juan", 25)
print(persona1.saludar())  # Salida: Hola, mi nombre es Juan y tengo 25 años.

