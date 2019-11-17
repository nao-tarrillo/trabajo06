import os

# BOLETA DE VENTA
# declarar variables
cliente,cuaderno,libro,agenda,precio_de_cuaderno,precio_de_libro,precio_de_agenda="","","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
cuaderno=os.sys.argv[2]
libro=os.sys.argv[3]
agenda=os.sys.argv[4]
precio_de_cuaderno=float(os.sys.argv[5])
precio_de_libro=float(os.sys.argv[6])
precio_de_agenda=float(os.sys.argv[7])

#PROCESSING
total_a_pagar=(precio_de_cuaderno+precio_de_libro+precio_de_agenda)

#vVERIFICADOR
total_a_gastar=(not(total_a_pagar<655))

#OUTPUT
print("###########################")
print("#  Librería:     ILUSIONES DEL SABER")
print("###########################")
print("# cliente:", cliente)
print("# cuaderno01:", cuaderno,"            # precio:  S/.", precio_de_cuaderno)
print("# cuaderno02:", libro,"            # precio:  S/.", precio_de_libro)
print("# cuaderno03:", agenda,"            #  precio:  S/.", precio_de_agenda)
print("# total:  S/.", total_a_pagar)
print("###########################")
print("# total a gastar:", total_a_gastar)
print("###########################")

# CONDICIONAL SIMPLE
# si el total a pagar supera los S/. 215.00, no podras ir a clases
if( total_a_pagar>215):
    print("Ud no podra asistir a clases")
# fin_if
