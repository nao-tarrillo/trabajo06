import os

# BOLETA DE VENTA
# declarar variables
cliente,gaseosas,cervezas,cifruts,precio_de_una_gaseosa,precio_de_una_cerveza,precio_de_un_cifrut="",0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
gaseosas=int(os.sys.argv[2])
cervezas=int(os.sys.argv[3])
cifruts=int(os.sys.argv[4])
precio_de_una_gaseosa=float(os.sys.argv[5])
precio_de_una_cerveza=float(os.sys.argv[6])
precio_de_un_cifrut=float(os.sys.argv[7])

# PROCESSING
total=((gaseosas*precio_de_una_gaseosa)+(cervezas*precio_de_una_cerveza)+(cifruts*precio_de_un_cifrut))

# VERIFICADOR
cantidad_de_bebida=not(total!=gaseosas or total==total)

#OUTPUT
print("#########################")
print("# Centro comercial:     MI JUANITA  ")
print("#########################")
print("# cliente:", cliente)
print("# gaseosas:", gaseosas,"                        precio:   S/.", precio_de_una_gaseosa)
print("# cervezas:", cervezas,"                        precio:   S/.", precio_de_una_cerveza)
print("# cifruts:", cifruts,"                          precio:   S/.", precio_de_un_cifrut)
print("# total:   S/.", total)
print("#########################")
print("# cantidad de bebida:", cantidad_de_bebida)
print("#########################")

# CONDICIONAL DOBLE
# si el total es mayor a S/. 430.00, entonces iras a la fiesta
if( total>430):
    print("Ud ira a la fiesta")
else:
    print("Ud no ira a la fiesta")
# fin_if
