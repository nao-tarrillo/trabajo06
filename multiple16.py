import os

# BOLETA DE VENTA
# declarar variables
cliente,RUC,baldes,tinas,cilindros,precio_de_un_balde,precio_de_una_tina,precio_de_un_cilindro="",0,0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
baldes=int(os.sys.argv[3])
tinas=int(os.sys.argv[4])
cilindros=int(os.sys.argv[5])
precio_de_un_balde=float(os.sys.argv[6])
precio_de_una_tina=float(os.sys.argv[7])
precio_de_un_cilindro=float(os.sys.argv[8])

# PROCESSING
total=((baldes*precio_de_un_balde)+(tinas*precio_de_una_tina)+(cilindros*precio_de_un_cilindro))

# VERIFICADOR
ganancia=(total==total)

#OUTPUT
print("#########################")
print("# Plastiqueria:      RAMOS  ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# baldes:", baldes,"                                       precio:   S/.", precio_de_un_balde)
print("# tinas:", tinas,"                                         precio:   S/.", precio_de_una_tina)
print("# cilindros:", cilindros,"                                 precio:   S/.", precio_de_un_cilindro)
print("total:     S/.", total)
print("#########################")
print("# ganancia:", ganancia)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 25.00, entonces pondras tienda de plasticos
if( total>25):
    print("Ud ha puesto una tienda de plasticos")
# fin_if

# si el total es igual a S/ 25.00, entonces invertiras en otra venta
if( total==25):
    print("Ud ha invertido en otra venta")
# fin_if

# si el total es menor a S/. 25.00, entonces no pondras tienda de plasticos
if(total<25):
    print("Ud no ha puesto ninguna tienda de plasticos")
# fin_if
