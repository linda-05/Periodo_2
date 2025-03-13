class Gato:
    def sonido (self):
        return "Maulla"
    
class Perro:
    def sonido (self):
        return "Ladra"

#Uso de polimorfismo
def hacer_sonido (animal):
    print (animal.sonido())

gato = Gato ()
perro = Perro ()

hacer_sonido(gato)
hacer_sonido(perro)