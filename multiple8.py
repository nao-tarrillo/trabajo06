import os
# BOLETA DE VENTA
# Declarar variables
cliente,gaseosas,precio_unitario= "",0,0.0

# Input
cliente=os.sys.argv[1]
gaseosas=int(os.sys.argv[2])
precio_unitario=float(os.sys.argv[3])

#Procesing
total= (precio_unitario * gaseosas)

#Verificador
comprador_compulsivo=( total > 578 )

#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",gaseosas,"gaseosas")
print("#precio unitario:       S/.", precio_unitario)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el monto en menor que 500 obtiene un pase al sorteo
if (comrador_compulsivo ==True)
    print ("GANSTE UN PASE AL SORTEO")
# Si el total es mayor que 578 gana un premio
if (comrador_compulsivo ==True)
    print ("GANASTE UN PREMIO")
# Si el total si no supera el minimo gana un paquete de gaseosas
if (comrador_compulsivo ==True)
    print ("GANASTE UN PAQUETE DE GASEOSAS")

#FIN_IF
