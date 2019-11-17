import os
# BOLETA DE VENTA
# Declarar variables
cliente,bolsas_caramelo,precio_bolsa= "",0,0.0

# Input
cliente =input(os.sys.argv[1])
bolsas_caramelo=int(os.sys.argv[2])
precio_bolsa=float(os.sys.argv[3])

#Procesing
total= (precio_bolsa * bolsas_caramelo)

#Verificador
comprador_compulsivo =( total > 200 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",bolsas_caramelo,"bolsas_caramelo")
print("#precio_bolsa:       S/.", precio_bolsa)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es menor a 200 gana un descuento en su proxima compra
if (comrador_compulsivo == True)
    print ("GANASTE UN DESCUENTO EN TU PROXIMA COMPRA")
# Si el total es mayor que 200 gana una tarjeta de compra
if (comrador_compulsivo ==True)
    print ("GANASTE UNA TARJETA DE COMPRA")
# Si el total no llega al monto gana una bolsa gratis
if (comrador_compulsivo ==True)
    print ("GANASTE UNA BOLSA GRATIS")

#FIN_IF
