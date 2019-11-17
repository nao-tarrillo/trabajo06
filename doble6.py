import os
# BOLETA DE VENTA
# Declarar variables
empresa,nro_computadoras,p.u= "",0,0.0

# Input
empresa=os.sys.argv[1]
nro_computadoras=os.sys.argv[2]
p.u=float(os.sys.argv[3])

#Procesing
total= (p.u * nro_computadoras)

#Verificador
comprador_compulsivo=(total>38)
#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_computadoras,"nro_computadoras")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera a 38 obtiene una tarjeta black
if (comrador_compulsivo == True)
    print ("GANASTE LA TARJETA BLACK")

# Si el total es menor que 38 se le da una tarjeta golden
else:
    print ("GANASTE UNA TARJETA GOLDEN")

#FIN_IF
