import os

# BOLETA DE VENTA
# declarar variables
cliente,RUC,relojes,pulseras,cadenas,precio_de_un_reloj,precio_de_una_pulsera,precio_de_una_cadena="",0,0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
relojes=int(os.sys.argv[3])
pulseras=int(os.sys.argv[4])
cadenas=int(os.sys.argv[5])
precio_de_un_reloj=float(os.sys.argv[6])
precio_de_una_pulsera=float(os.sys.argv[7])
precio_de_una_cadena=float(os.sys.argv[8])

# PROCESSING
total=((relojes*precio_de_un_reloj)+(pulseras*precio_de_una_pulsera)+(cadenas*precio_de_una_cadena))

# VERIFICADOR
precio_de_venta=not(total<=pulseras and relojes!=cadenas)

#OUTPUT
print("#########################")
print("# Joyeria:       EL MILLONARIO   ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# relojes:", relojes,"                                   precio:  S/.", precio_de_un_reloj)
print("# pulseras:", pulseras,"                                 precio:  S/.", precio_de_una_pulsera)
print("# cadenas:", cadenas,"                                   precio:  S/.", precio_de_una_cadena)
print("# total:   S/.", total)
print("#########################")
print("# precio de venta:", precio_de_venta)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 150.00, ganaste la tarjeta dorada
if( total>150):
    print("Ud ha ganado la tarjeta dorada")
# fin_if

# si el total es igual a S/. 150.00, ganaste la tarjeta de plata
if( total==150):
    print("Ud ha ganado la tarjeta de plata")
#fin_if

# si el total es menor que S/. 150.00, ganaste la tarjeta de cobre
if( total<150):
    print("Ud ha ganado la tarjeta de cobre")
# fin_if
