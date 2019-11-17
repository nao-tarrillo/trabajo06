import os

# BOLETA DE VENTA
# declarar variables
cliente,RUC,lapiceros,lapices,borradores,precio_de_lapicero,precio_de_un_lapiz,precio_de_un_borrador="",0,0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
lapiceros=int(os.sys.argv[3])
lapices=int(os.sys.argv[4])
borradores=int(os.sys.argv[5])
precio_de_lapicero=float(os.sys.argv[6])
precio_de_un_lapiz=float(os.sys.argv[7])
precio_de_un_borrador=float(os.sys.argv[8])

#PROCESSING
total=((lapiceros*precio_de_lapicero)+(lapices*precio_de_un_lapiz)+(borradores*precio_de_un_borrador))

# VERIFICADOR
precio_de_compra=not(total!=65)

#OUTPUT
print("#########################")
print("# Libreria:     CAYETANO HEREDIA")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# lapiceros:", lapiceros,"                       precio:  S/.", precio_de_lapicero)
print("# lapices:", lapices,"                           precio:  S/.", precio_de_un_lapiz)
print("# borradores:", borradores,"                     precio:  S/.", precio_de_un_borrador)
print("# total:   S/.", total)
print("#########################")
print("# precio de compra:", precio_de_compra)
print("#########################")

# CONDICIONAL SIMPLE
# si el total supera los S/. 5.00, entonces solo comprara lapiceros
if( total>5):
    print("Ud solo comprara lapiceros")
# fin_if
