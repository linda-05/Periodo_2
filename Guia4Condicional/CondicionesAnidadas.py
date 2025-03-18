valor = int(input("Ingrese un valor:"))
valor2 = int(input("Ingrese un valor:"))

if valor> valor2:
    print("Es mayor")
else:
    print("No es mayor que")

def par (valor):
    resultado = "Es par" if valor % 2 == 0 else "Es impar"
    return resultado

def positivoONegativo (valor):
    resultado = "Negativo" if valor<0 else "Positivo"
    return  resultado

def detectarLetras(valor):
    if any(c.isalpha() for c in str (valor)):
        return True
    else:
        return False
    
def parYSigno (func1, func2):
    if func1(valor) == "Negativo" and func2(valor) == "Es impar":
        return "negativo, impar"
    if func1(valor) == "Positivo" and func2(valor) == "Es impar":
        return "Positivo, impar"
    if func1(valor) == "Positivo" and func2(valor) == "Es par":
        return "Positivo, par"
    if func1(valor) == "Positivo" and func2(valor) == "Es impar":
        return "Positivo, impar"

45
if not detectarLetras(valor):
    resultado = parYSigno (positivoONegativo, par)
    print (f"El numero {valor} es {resultado}")
else: print("Solo numeros")