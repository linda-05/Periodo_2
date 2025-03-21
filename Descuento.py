
# 50 5
#100 10
#200 12
#100 20

compra = float(input("Ingrese el monto de la compra:"))
unidades = int(input("Ingrese la cantidad de unidades:"))
descuento = 0
impuesto = 0
if compra < 0:
    print("El monto de la compra no puede ser negativo")

if unidades <12: descuento = 0
if unidades >= 12 : descuento = 0.20

if compra >= 10 and compra < 50: impuesto = 0.05
if compra > 50 and compra < 100: impuesto = 0.10
if compra > 100 and compra <200: impuesto = 0.20
if compra > 200: impuesto =0.20

resultado = compra * impuesto
montototal = compra + resultado - descuento * compra
print( descuento * compra)
print("El impuesto a pagar es:", montototal)

#pedir desde consola un monto de compra 12 unidades va ser el descuento del 10% de descuento
# si compra 20 unidades 10% de descuento 



