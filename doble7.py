import os
# BOLETA DE VENTA
# Declarar variables
comprador,nro_cajas,precio_caja= "",0,0.0

# Input
comprador=os.sys.argv[1])
nro_cajas=os.sys.argv[2]
precio_caja=float(os.sys.argv[3])

#Procesing
total= (precio_caja * nro_cajas)

#Verificador
comprador_compulsivo=( total > 32 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# comprador:", comprador)
print("#item:    ",nro_cajas,"nro_cajas")
print("#precio_caja:       S/.", precio_caja)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor a 32 accede a un sorteo
if (comrador_compulsivo ==True)
    print ("INGRESASTE AL SORTEO")
else:
    print ("GANASTE UNA SORPRESA")

#FIN_IF
