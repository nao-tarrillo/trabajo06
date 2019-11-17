import os

# BOLETA DE VENTA
# declarar variables
cliente,RUC,pintura01,pintura02,pintura03,precio_pintura01,precio_pintura02,precio_pintura03="",0,"","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
pintura01=os.sys.argv[3]
pintura02=os.sys.argv[4]
pintura03=os.sys.argv[5]
precio_pintura01=float(os.sys.argv[6])
precio_pintura02=float(os.sys.argv[7])
precio_pintura03=float(os.sys.argv[8])

# PROCESSING
total=(precio_pintura01+precio_pintura02+precio_pintura03)

# VERIFICADOR
total_de_venta=(total!=555)

#OUTPUT
print("#########################")
print("# Ferreteria:     LA VIRGEN DEL CARMEN  ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# pintura:", pintura01,"                           precio:  S/.", precio_pintura01)
print("# pintura:", pintura02,"                           precio:  S/.", precio_pintura02)
print("# pintura:", pintura03,"                           precio:  S/.", precio_pintura03)
print("# total:    S/.", total)
print("#########################")
print("# total de venta:", total_de_venta)

# CONDICION MULTIPLE
# si el total supera los S/. 180.00, entonces no pintura el cuadro
if( total>180):
    print("Ud ha pintado el cuadro")
# fin_if

# si el total es igual a S/. 180.00, entonces pintaras el cuadro solo la mitad
if( total==180):
    print("Ud no pintado completo el cuadro")
# fin_if
# si el total es menor a S/. 180.00, entonces pintaras el cuadro completo
if( total<180):
    print("Ud ha pintado todo el cuadro")
# fin_if
