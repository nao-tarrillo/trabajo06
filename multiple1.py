import os
# BOLETA DE VENTA
# Declarar variables
cliente, nro_cervezas, p.u= "", 0, 0.0

# Input
cliente = os.sys.argv[1]
nro_cervezas = s.sys.argv[2]
p.u= float(os.sys.argv[3])

#Procesing
total= (p.u * nro_cervezas)

#Verificador
comrador_compulsivo=(total > 80)

#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_cervezas,"nro cervesas")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

#si el total es menor que 80 entonces tiene un bono en su proxima visita.
if (comrador_compulsivo == True)
    print ("GANASTE UN BONO EN TU PROXIMA VISITA")
# Si el total es mayor que 150 entonces obtiene una visita por la fabrica
if (comrador_compulsivo ==True)
    print ("GANASTE UNA VISITA A LA FABRICA ")
# Si el total esta entre 80 y 100 entonces obtiene 5 cervezas mas
if (comrador_compulsivo ==True)
    print ("GANASTE 5 CERVEZAS")

#FIN_IF
