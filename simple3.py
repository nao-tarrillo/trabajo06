import os
# BOLETA DE VENTA
# Declarar variables
cliente,kg,P.u ="",0,0.0

# Input
cliente=os.sys.argv[1]
kg=int(os.sys.argv[2])
P.u=float(os.sys.argv[3])

#Verificador
comprador_compulsivo=(total>300)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("#")
print("# cliente:", cliente)
print("#item:    ",kg,"kg")
print("#P.U:      S/.", P.U)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor a 300 obtendran un bono especial
if (comrador_compulsivo ==True)
    print ("OBTUVISTE UN BONO ESPECIAL")
#FIN_IF
