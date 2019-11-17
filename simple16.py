import os

# BOLETA DE VENTA
# declarar variables
cliente,numero_de_RUC,televisor,licuadora,refrigeradora,precio_del_televisor,precio_de_la_licuadora,precio_de_la_refrigeradora="",0,"","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
numero_de_RUC=int(os.sys.argv[2])
televisor=os.sys.argv[3]
licuadora=os.sys.argv[4]
refrigeradora=os.sys.argv[5]
precio_del_televisor=float(os.sys.argv[6])
precio_de_la_licuadora=float(os.sys.argv[7])
precio_de_la_refrigeradora=float(os.sys.argv[8])

# PROCESSING
total=(precio_del_televisor+precio_de_la_licuadora+precio_de_la_refrigeradora)

# VERIFICADOR
precio_de_venta=(total==total)

#OUTPUT
print("#########################")
print("# Centro comercial:    LA CHICLAYANITA")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", numero_de_RUC)
print("# televisor:", televisor,"                       precio:  S/.", precio_del_televisor)
print("# licuadora:", licuadora,"                       precio:  S/.", precio_de_la_licuadora)
print("# refrigeradora:", refrigeradora,"               precio:  S/.", precio_de_la_refrigeradora)
print("# total:   S/.", total)
print("#########################")
print("# precio de venta:", precio_de_venta)
print("#########################")

# CONDICIONAL SIMPLE
# si el total es menor a S/. 2000.00, entonces no compraras todos los artefactos domesticos
if( total<2000):
    print("Ud no comprara todos los artefactos domesticos")
# fin_if
