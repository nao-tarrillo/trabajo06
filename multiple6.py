import os
# BOLETA DE VENTA
# Declarar variables
cliente,nro_juguetes,p.u= "",0,0.0

# Input
cliente=os.sys.argv[1]
nro_juguetes=int(os.sys.argv[2])
p.u=float(os.sys.argv[3])

#Procesing
total= (p.u * nro_juguetes)

#Verificador
comprador_compulsivo=( total > 80 )

#Output
print("#######################")
print("####Boleta de venta####")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_juguetes,"nro_juguetes")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera 80 gana un pase para el cine
if (comrador_compulsivo == True)
    print ("GANASTE UN PASE AL CINE")
# Si el total es menor que 80 gana un premio sorpresa
if (comrador_compulsivo == True)
    print ("GANASTE UN PREMIO SORPRESA")
# Si el total no llega a ser mayor que 85 tiene un vale de descuento
if (comrador_compulsivo == True)
    print ("VALE DE DESCUENTO")

#FIN_IF
