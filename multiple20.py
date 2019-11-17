import os

# BOLETA DE VENTA
# declarar variables
cliente,DNI,platos,cucharas,ollas,precio_de_un_plato,precio_de_una_cuchara,precio_de_una_olla="",0,0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
DNI=int(os.sys.argv[2])
platos=int(os.sys.argv[3])
cucharas=int(os.sys.argv[4])
ollas=int(os.sys.argv[5])
precio_de_un_plato=float(os.sys.argv[6])
precio_de_una_cuchara=float(os.sys.argv[7])
precio_de_una_olla=float(os.sys.argv[8])

# PROCESSING
total=((platos*precio_de_un_plato)+(cucharas*precio_de_una_cuchara)+(ollas*precio_de_una_olla))

# VERIFICADOR
impuesto=not(total>=precio_de_una_olla and total!=total)

#OUTPUT
print("#########################")
print("# Centro comercial:      EL PIURANITO ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# platos:", platos,"                    precio:  S/.", precio_de_un_plato)
print("# cucharas:", cucharas,"                precio:  S/.", precio_de_una_cuchara)
print("# ollas:", ollas,"                      precio:  S/.", precio_de_una_olla)
print("# total:    S/.", total)
print("#########################")
print("# impuesto:", impuesto)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 500.00, entonces compraras dos docenas de platos
if( total>500):
    print("Ud ha comprado dos docenas de platos")
# fin_if

# si el total es igual a los S/. 500.00, entonces compraras cinco centenas de cucharas
if( total==500):
    print("Ud ha comprado cinco centenas de cucharas")
# fin_if

# si el total es menor que los S/. 500.oo, entonces compraras  dos docenas de ollas
if( total<500):
    print("Ud ha comprado dos docenas de ollas")
# fin_if
