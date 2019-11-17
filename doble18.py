import os

# BOLETA DE VENTA
# declarar variables
cliente,tubos,fierros,clavos,precio_de_un_tubo,precio_de_un_fierro,precio_de_un_clavo="",0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
tubos=int(os.sys.argv[2])
fierros=int(os.sys.argv[3])
clavos=int(os.sys.argv[4])
precio_de_un_tubo=float(os.sys.argv[5])
precio_de_un_fierro=float(os.sys.argv[6])
precio_de_un_clavo=float(os.sys.argv[7])

# PROCESSING
total=((tubos*precio_de_un_tubo)+(fierros*precio_de_un_fierro)+(clavos*precio_de_un_clavo))

# VERIFICADOR
impuesto=(total<total)

#OUTPUT
print("#########################")
print("# Ferreteria:       EL LAMBAYECANO   ")
print("#########################")
print("# cliente:", cliente)
print("# tubos:", tubos,"                      precio:  S/.", precio_de_un_tubo)
print("# fierros:", fierros,"                  precio:   S/.", precio_de_un_fierro)
print("# clavos:", clavos,"                    precio:   S/.", precio_de_un_clavo)
print("# total:   S/.", total)
print("#########################")
print("# impuesto:", impuesto)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera a S/. 900.00, construiras tu casa
if( total>900):
    print("Ud construira su casa")
else:
    print("Ud no construira su casa")
# fin_if
