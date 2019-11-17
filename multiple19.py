import os

# BOLETA DE VENTA
# declarar variables
cliente,numero_de_DNI,numero_de_RUC,marca_de_cuaderno01,marca_de_cuaderno02,marca_de_cuaderno03,precio_de_cuaderno01,precio_de_cuaderno02,precio_de_cuaderno03="",0,0,"","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
numero_de_DNI=int(os.sys.argv[2])
numero_de_RUC=int(os.sys.argv[3])
marca_de_cuaderno01=os.sys.argv[4]
marca_de_cuaderno02=os.sys.argv[5]
marca_de_cuaderno03=os.sys.argv[6]
precio_de_cuaderno01=float(os.sys.argv[7])
precio_de_cuaderno02=float(os.sys.argv[8])
precio_de_cuaderno03=float(os.sys.argv[9])

#PROCESSING
total_a_pagar=(precio_de_cuaderno01+precio_de_cuaderno02+precio_de_cuaderno03)

#vVERIFICADOR
total_a_gastar=(not(total_a_pagar<655))

#OUTPUT
print("###########################")
print("#  Librería:     ILUSIONES DEL SABER")
print("###########################")
print("# cliente:", cliente)
print("# DNI:", numero_de_DNI)
print("# RUC:", numero_de_RUC)
print("# cuaderno01:", marca_de_cuaderno01,"            # precio:  S/.", precio_de_cuaderno01)
print("# cuaderno02:", marca_de_cuaderno02,"            # precio:  S/.", precio_de_cuaderno02)
print("# cuaderno03:", marca_de_cuaderno03,"            #  precio:  S/.", precio_de_cuaderno03)
print("# total:  S/.", total_a_pagar)
print("###########################")
print("# total a gastar:", total_a_gastar)
print("###########################")

# CONDICION MULTIPLE
# si el total supera los S/. 10.00, entonces compraras el cuaderno mas barato
if( total_a_pagar>10):
    print("Ud ha comprado el cuaderno mas barato")
# fin_if

# si el total es igual a S/. 10.00, entonces compraras 1 solo cuaderno
if( total_a_pagar==10):
    print("Ud ha comprado un solo cuaderno ")
# fin_if

# si el total es menor a S/.10.00, entonces compraras todos los cuadernos
if( total_a_pagar<10):
    print("Ud ha comprado todos los cuadernos")
# fin_if
