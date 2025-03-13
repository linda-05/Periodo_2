class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado (dos guiones bajos)
    
    def depositar(self, cantidad):
        self.__saldo += cantidad
    
    def obtener_saldo(self):
        return self.__saldo  # Metodo para acceder el atributo privado

# Uso
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo())  # Salida: 1500