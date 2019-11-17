import os

# BOLETA DE VENTA
# declarar variables
cliente,kg,precio_camote="",0,0.0

# INPUT
cliente=os.sys.argv[1]
kg=int(os.sys.argv[2])
precio_camote=float(os.sys.argv[3])

# PROCESSING
total = (precio_camote * kg)

# VERIFICADOR
comprador=(total!=total)

# OUTPUT
print("#######################")
print("# CENTRO COMERCIAL DE TUBERCULOS")
print("#######################")
print("# Cliente:  ", cliente)
print("# Item   :  ",kg,"  kg camote")
print("# P.U.   :  S/.", precio_camote)
print("# Total  :  S/.", total)
print("#######################")
print("# comprador:", comprador)
print("#######################")

# CONDICIONAL SIMPLE
# si el total no supera lo S/. 23.00,entonces almorzaras
if( total<23):
    print("Ud almorzara")
# fin_if
