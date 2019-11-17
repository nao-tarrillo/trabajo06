import os

# BOLETA DE VENTA
# declarar variables
cliente,DNI,RUC,zapatillas,zapatos,chimpunes,precio_de_zapatillas,precio_de_zapatos,precio_de_chimpunes="",0,0,"","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
DNI=int(os.sys.argv[2])
RUC=int(os.sys.argv[3])
zapatillas=os.sys.argv[4]
zapatos=os.sys.argv[5]
chimpunes=os.sys.argv[6]
precio_de_zapatillas=float(os.sys.argv[7])
precio_de_zapatos=float(os.sys.argv[8])
precio_de_chimpunes=float(os.sys.argv[9])

# PROCESSING
total=(precio_de_zapatillas+precio_de_zapatos+precio_de_chimpunes)

# VERIFICADOR
perdida=(total!=65)

#OUTPUT
print("#########################")
print("# Centro de calzado:     EL AMANECER  ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# RUC:", RUC)
print("# zapatillas:", zapatillas,"                        precio:  S/.", precio_de_zapatillas)
print("# zapatos:", zapatos,"                              precio:  S/.", precio_de_zapatos)
print("# chimpunes:", chimpunes,"                          precio:  S/.", precio_de_chimpunes)
print("# total:    S/.", total)
print("#########################")
print("# perdida:", perdida)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera los S/. 750.00, ganaste la tarjeta dorada
if( total>750):
    print("Ud ha ganado la tarjeta dorada")
else:
    print("Ud ha ganado la tarjeta de plata")
# fin_if
