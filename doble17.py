import os

# BOLETA DE VENTA
# declarar variables
cliente,RUC,colonia,desodorante,talco,precio_de_la_colonia,precio_del_desodorante,precio_del_talco="",0,"","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
colonia=os.sys.argv[3]
desodorante=os.sys.argv[4]
talco=os.sys.argv[5]
precio_de_la_colonia=float(os.sys.argv[6])
precio_del_desodorante=float(os.sys.argv[7])
precio_del_talco=float(os.sys.argv[8])

# PROCESSING
total=(precio_de_la_colonia+precio_del_desodorante+precio_del_talco)

# VERIFICADOR
numero_de_venta=(total!=23 or 23==total)

#OUTPUT
print("#########################")
print("# Perfumeria:       FLORES    ")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# colonia:", colonia,"                                     precio:   S/.", precio_de_la_colonia)
print("# desodorante:", desodorante,"                             precio:    S/.", precio_del_desodorante)
print("# talco:", talco,"                                         precio:    S/.", precio_del_talco)
print("# total:    S/.", total)
print("#########################")
print("# numero de venta:", numero_de_venta)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera los S/. 5000.00, no pondras tu negocio
if( total>5000):
    print("Ud no pondra su negocio")
else:
    print("Ud pondra su negocio")
# fin_if
