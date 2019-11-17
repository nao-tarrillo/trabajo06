import os

# BOLETA DE VENTA
# declarar variables
cliente,numero_de_DNI,numero_de_RUC,kg_de_pollo,kg_de_res,precio_de_kg_de_pollo,precio_de_kg_de_res="",0,0,0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
numero_de_DNI=int(os.sys.argv[2])
numero_de_RUC=int(os.sys.argv[3])
kg_de_pollo=int(os.sys.argv[4])
kg_de_res=int(os.sys.argv[5])
precio_de_kg_de_pollo=float(os.sys.argv[6])
precio_de_kg_de_res=float(os.sys.argv[7])

# PROCESSING
total=((kg_de_pollo*precio_de_kg_de_pollo)+(kg_de_res*precio_de_kg_de_res))

# VERIFICADOR
venta=(kg_de_res>kg_de_pollo)

#OUTPUT
print("#########################")
print("# CARNICERIA:   EL CHATO ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", numero_de_DNI)
print("# RUC:", numero_de_RUC)
print("# pollo:", kg_de_pollo,"kg                      precio:  S/.", precio_de_kg_de_pollo)
print("# res:", kg_de_res,"kg                          precio:  S/.", precio_de_kg_de_res)
print("# total: S/.",total)
print("#########################")
print("# venta:", venta)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 30.00, entonces solo comeras pollo
if( total>30):
    print("Ud solo comera pollo")
# fin_if

# si el total es igual a S/. 30.00, entonces solo comeras res
if( total==30):
    print("Ud solo comera res")
# fin_if

# si el total es menor que S/. 30.00, entonces comeras res y pollo
if( total<30):
    print("Ud comera res y pollo")
# fin_if
