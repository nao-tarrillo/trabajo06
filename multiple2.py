import os
# BOLETA DE VENTA
# Declarar variables
cliente, producto, p.u= "","",0.0

# Input
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
p.u=float(os.sys.argv[3])

#Procesing
total= (p.u * producto)

#Verificador
comprador_compulsivo=( total > 45 )

#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",producto,"producto")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

#Cada vez que el cliente llegue a mas de 100 obtendra un vale por el 60% de descuento en productos
if (comrador_compulsivo == True)
    print ("OBTUVISTE EL 60% DE DESCUENTO EN PRODUCTOS")
# Si el total es menor de 45 se gana un vale de compra
if (comrador_compulsivo ==True)
    print ("GANASTE UN VALE PARA TU PROXIMA COMPRA")
# Si el total esta entre 45 y 100 obtiene el 25% de descuento en cualquier producto
if (comrador_compulsivo ==True)
    print ("GANASTE UN 25% DE DESCUENTO")

#FIN_IF
