import os

# BOLETA DE VENTA
# declarar variables
cliente,numero_de_venta,libro01,libro02,libro03,precio_del_libro01,precio_del_libro02,precio_del_libro_03="",0,"","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
numero_de_venta=int(os.sys.argv[2])
libro01=os.sys.argv[3]
libro02=os.sys.argv[4]
libro03=os.sys.argv[5]
precio_del_libro01=float(os.sys.argv[6])
precio_del_libro02=float(os.sys.argv[7])
precio_del_libro_03=float(os.sys.argv[8])

# PROCESSING
total=(precio_del_libro01+precio_del_libro02+precio_del_libro_03)

# VERIFICADOR
total_comprado=not(total<3 or precio_del_libro_03>=3)

#OUTPUT
print("#########################")
print("# Libreria:   EL PERUANITO ")
print("#########################")
print("# cliente:", cliente)
print("# numero de venta:", numero_de_venta)
print("# libro:", libro01,"               precio: S/.", precio_del_libro01)
print("# libro:", libro02,"               precio: S/.", precio_del_libro02)
print("# libro:", libro03,"               precio: S/.", precio_del_libro_03)
print("# total: S/.", total)
print("#########################")
print("# total comprado:", total_comprado)
print("#########################")

# CONDICIONAL SIMPLE
# si el total supera los S/. 67.00, entonces no resolveras los ejercicios
if( total>67):
    print("Ud no resolvera los ejercicios")
# fin_if
