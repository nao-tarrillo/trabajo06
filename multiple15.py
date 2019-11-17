import os

# BOLETA DE VENTA
# declarar variables
cliente,RUC,tubos,fierros,clavos,precio_de_un_tubo,precio_de_un_fierro,precio_de_un_clavo="",0,0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
tubos=int(os.sys.argv[3])
fierros=int(os.sys.argv[4])
clavos=int(os.sys.argv[5])
precio_de_un_tubo=float(os.sys.argv[6])
precio_de_un_fierro=float(os.sys.argv[7])
precio_de_un_clavo=float(os.sys.argv[8])

# PROCESSING
total=((tubos*precio_de_un_tubo)+(fierros*precio_de_un_fierro)+(clavos*precio_de_un_clavo))

# VERIFICADOR
impuesto=(total<total)

#OUTPUT
print("#########################")
print("# Ferreteria:       EL LAMBAYECANO   ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# tubos:", tubos,"                      precio:  S/.", precio_de_un_tubo)
print("# fierros:", fierros,"                  precio:   S/.", precio_de_un_fierro)
print("# clavos:", clavos,"                    precio:   S/.", precio_de_un_clavo)
print("# total:   S/.", total)
print("#########################")
print("# impuesto:", impuesto)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 1000.00, ganaste la tarjeta dorada
if( total>1000):
    print("Ud ha ganado la tarjeta dorada")
# fin_if

# si el total es igual S/. 1000.00, ganaste la tarjeta de plata
if( total==1000):
    print("Ud ha ganado la tarjeta de plata")
# fin_if

# si el total es menor a S/. 1000.00, ganaste la tarjeta de cobre
if( total<1000):
    print("Ud ha ganado la tarjeta de cobre")
# fin_if
