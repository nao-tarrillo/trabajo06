import os
# BOLETA DE VENTA
# Declarar variables
cliente,nro_granadillas,p.u = "",0,0.0

# Input
cliente=os.sys.argv[1]
nro_granadillas=int(os.sys.argv[2]
p.u=float(os.sys.argv[3])

#Procesing
total= (p.u * nro_granadillas)

#Verificador
comprador_compulsivo=( total > 34 )

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

# Si el total es mayor que 34 entonces gana una rifa
if (comrador_compulsivo ==True)
    print ("GANASTE UNA RIFA")
else:
    print ("GANASTE UN PREMIO")
#FIN_IF
