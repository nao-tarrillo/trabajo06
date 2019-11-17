import os

# BOLETA DE VENTA
# declarar variables
cliente,kg_de_pollo,kg_de_res,precio_de_kg_de_pollo,precio_de_kg_de_res="",0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
kg_de_pollo=int(os.sys.argv[2])
kg_de_res=int(os.sys.argv[3])
precio_de_kg_de_pollo=float(os.sys.argv[4])
precio_de_kg_de_res=float(os.sys.argv[5])

# PROCESSING
total=((kg_de_pollo*precio_de_kg_de_pollo)+(kg_de_res*precio_de_kg_de_res))

# VERIFICADOR
venta=(kg_de_res>kg_de_pollo)

#OUTPUT
print("#########################")
print("# CARNICERIA:   EL CHATO ")
print("#########################")
print("# cliente:", cliente)
print("# pollo:", kg_de_pollo,"kg                      precio:  S/.", precio_de_kg_de_pollo)
print("# res:", kg_de_res,"kg                          precio:  S/.", precio_de_kg_de_res)
print("# total: S/.",total)
print("#########################")
print("# venta:", venta)
print("#########################")

# CONDICIONAL SIMPLE
# si el total supera los S/. 55.00, entonces no iras de paseo
if( total>55):
     print("Ud no ira de paseo")
# fin_if
