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

#Condicion
#Cada vez que el cliente llegue a mas de 45 obtendra un vale por el 30% de descuento en productos
if (comrador_compulsivo == True)
    print ("OBTUVISTE EL 30% DE DESCUENTO EN PRODUCTOS")
else:
    print ("GANASTE UN VALE PARA TU PROXIMA COMPRA")

#FIN_IF
