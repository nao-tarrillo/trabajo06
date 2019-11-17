import os
# BOLETA DE VENTA
# Declarar variables
cliente,cajero,nro_carteras,p.u= "","",0,0.0

# Input
cliente=input(os.sys.argv[1])
cajero=input(os.sys.argv[2])
nro_carteras=int(os.sys.argv[3])
p.u=float(os.sys.argv[4])

#Procesing
total= (p.u * nro_carteras)

#Verificador
comprador_compulsivo=(total>25000)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_carteras,"nro_carteras")
print("#p.u:      S/.", p.u)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es menor que 25000 obtiene una cartera de regalo
if (comrador_compulsivo ==True)
    print ("GANASTE UNA CARTERA POR TU PREFERENCIA")
else:
    print ("GANASTE UNA TARJETA PREMIUM")
#FIN_IF
