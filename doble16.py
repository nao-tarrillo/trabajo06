import os

# BOLETA DE VENTA
# declarar variables
cliente,pintura01,pintura02,pintura03,precio_pintura01,precio_pintura02,precio_pintura03="","","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
pintura01=os.sys.argv[2]
pintura02=os.sys.argv[3]
pintura03=os.sys.argv[4]
precio_pintura01=float(os.sys.argv[5])
precio_pintura02=float(os.sys.argv[6])
precio_pintura03=float(os.sys.argv[7])

# PROCESSING
total=(precio_pintura01+precio_pintura02+precio_pintura03)

# VERIFICADOR
total_de_venta=(total!=555)

#OUTPUT
print("#########################")
print("# Ferreteria:     LA VIRGEN DEL CARMEN  ")
print("#########################")
print("# cliente:", cliente)
print("# pintura:", pintura01,"                           precio:  S/.", precio_pintura01)
print("# pintura:", pintura02,"                           precio:  S/.", precio_pintura02)
print("# pintura:", pintura03,"                           precio:  S/.", precio_pintura03)
print("# total:    S/.", total)
print("#########################")
print("# total de venta:", total_de_venta)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera a S/. 230.00, pintas tu casa
if( total>230):
    print("Ud si pinta su casa")
else:
    print("Ud no pinta su casa")
# fin_if
