import os
# BOLETA DE VENTA
# Declarar variables
cliente,nro_granadillas,p.u = "",0,0.0

# Input
cliente=os.sys.argv[1]
nro_granadillas=int(os.sys.argv[2])
p.u=float(os.sys.argv[3])

#Procesing
total= (p.u * nro_granadillas)

#Verificador
comprador_compulsivo=( total > 54 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_granadillas,"nro_granadillas")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor que 65 entonces gana una rifa
if (comrador_compulsivo ==True)
    print ("GANASTE UNA RIFA")
# Si el total es menor que 54 gana una docena de granadillas
if (comrador_compulsivo ==True)
    print ("GANASTE UNA DOCENA DE GRANADILAS")
# Si el total esta entre 54 y 65 gana un descuento en la sgnte compra
if (comrador_compulsivo ==True)
    print ("GANASTE UN DESCUENTO EN SU PROXIMA COMPRA")

#FIN_IF
