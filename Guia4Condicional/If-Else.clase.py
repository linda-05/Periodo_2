# if una opcion
# condicion true false

# numero es par, impar, negativo o positivos 

respuesta  = int(input("Ingrese el numero"))

if respuesta % 2 == 0 : 
    print ("Es par")
else:
    print("Es impar")

if respuesta < 0 :
    print ("Negativo")
else:
    print("Es positivo")

if respuesta == 0: print("El numero ingresado es 0")

print ("______________________________________")
respuesta1 = "Es par" if respuesta % 2 == 0 else "Es impar"
respuesta2 = "Negativo" if respuesta < 0 else "positivo"
print (f"{respuesta1} , {respuesta2}")

# definir el numero par
# def nombre():                        indica que estamos en presencia de una una funcion
def Modulo(valor):
    valor = True if  respuesta % 2 == 0 else False
    print (valor)
    return valor

# las funciones son estructuras de codigo que se ejecutan mediante su llamado nombre()
# Fncion es positivo

def signo(valor):
    valor = False if  respuesta < 0 else True
    print (valor)
    return(valor)

def detectarLetras(valor):
    if any (c.isalpha() for c in str (valor)):
        print(True)
        return True
    else:
        print(False)
        return False
#any() es funcion que ya trae python
#si hay un elemento que es true la funcion nos devolvera
#true de lo contrario false
#for c es una variable temporal
#for data las vueltas necesarias para terminar el numero
#segun sus caracteres
#isalfhan nos indica si todos los caractes son letra so numeros

valor = 4
Modulo(valor)
signo(valor)
detectarLetras(43)

def ejecutar():
    pedirValor = int(input("Ingrese el numero"))
    if pedirValor == True:
        ejecutar()
    else : 
        # valor = True if  respuesta < 0 else True
        Mrespuesta = Modulo(pedirValor)
        #Valor = true respuesta % 2 == 0 else false
        Srespuesta = signo(pedirValor)
        #positivo y par
    if Mrespuesta and Srespuesta == True:
        print("Positivo y par")
    if Mrespuesta or Srespuesta == False:
        print("Negativo y impar")
    
    ejecutar()

# and multiplica 1 x 1 = 1 true
#                1 x 0 = 0 false