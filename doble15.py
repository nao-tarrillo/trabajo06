import os
# BOLETA DE VENTA
# declarar variables
cliente,avion01,avion02,avion03,precio_de_avion01,precio_de_avion02,precio_de_avion03="","","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
avion01=os.sys.argv[2]
avion02=os.sys.argv[3]
avion03=os.sys.argv[4]
precio_de_avion01=float(os.sys.argv[5])
precio_de_avion02=float(os.sys.argv[6])
precio_de_avion03=float(os.sys.argv[7])

# PROCESSING
total=(precio_de_avion01+precio_de_avion02+precio_de_avion03)

# VERIFICADOR
IGV=(total>=21 or 21>=total)

#OUTPUT
print("#########################")
print("# SAC.    AEROLINEA-SIDER-EE.UU")
print("#########################")
print("# cliente:", cliente)
print("# avion01:", avion01,"                      precio:  S/.", precio_de_avion01)
print("# avion02:", avion02,"                      precio:  S/.", precio_de_avion02)
print("# avion03:", avion03,"                      precio:  S/.", precio_de_avion03)
print("# total:   S/.", total)
print("#########################")
print("# IGV:", IGV)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera a S/. 5 000 000 000.00, ganaste en la venta
if( total>5000000000):
    print("Ud ha ganado en la venta")
else:
    print("Ud ha perdido en la venta")
# fin_if
