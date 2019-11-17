import os

#BOLETA DE VENTA
#declarar variables
cliente,RUC,pantalon,camisa,polo,precio_del_pantalon,precio_de_la_camisa,precio_del_polo="",0,"","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
pantalon=os.sys.argv[3]
camisa=os.sys.argv[4]
polo=os.sys.argv[5]
precio_del_pantalon=float(os.sys.argv[6])
precio_de_la_camisa=float(os.sys.argv[7])
precio_del_polo=float(os.sys.argv[8])

# PROCESSING
total=(precio_del_pantalon+precio_de_la_camisa+precio_del_polo)

# VERIFICADOR
ganancia_obtenida=(total<1)

#OUTPUT
print("#########################")
print("# Centro comercial:    EL ELEGANTE  ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# pantalon:", pantalon,"                           precio:   S/.", precio_del_pantalon)
print("# camisa:", camisa,"                               precio:   S/.", precio_de_la_camisa)
print("# polo:", polo,"                                   precio:   S/.", precio_del_polo)
print("# total:   S/.", total)
print("#########################")
print("# ganancia obtenida:", ganancia_obtenida)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera a S/. 630.00, ganaste la loteria
if( total>630):
    print("Ud ha ganado la loteria")
else:
    print("Ud no ha ganado la loteria")
# fin_if
