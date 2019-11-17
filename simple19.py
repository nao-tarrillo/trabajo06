import os

# BOLETA DE VENTA
# declarar variables
cliente,DNI,arroz,fideo,azucar,precio_de_kg_arroz,precio_de_kg_fideo,precio_de_kg_azucar="",0,0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
DNI=int(os.sys.argv[2])
arroz=int(os.sys.argv[3])
fideo=int(os.sys.argv[4])
azucar=int(os.sys.argv[5])
precio_de_kg_arroz=float(os.sys.argv[6])
precio_de_kg_fideo=float(os.sys.argv[7])
precio_de_kg_azucar=float(os.sys.argv[8])

# PROCESSING
total=((arroz*precio_de_kg_arroz)+(fideo*precio_de_kg_fideo)+(azucar*precio_de_kg_azucar))

# VERIFICADOR
IGV=(total>=fideo and 52!=total)

#OUTPUT
print("#########################")
print("# Centro comercial:    LA AYACUCHANA")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# arroz:", arroz,"kg                               precio:   S/.", precio_de_kg_arroz)
print("# fideo:", fideo,"kg                               precio:   S/.", precio_de_kg_fideo)
print("# azucar:", azucar,"kg                             precio:   S/.", precio_de_kg_azucar)
print("# total:    S/.", total)
print("#########################")
print("# IGV:", IGV)
print("#########################")

# CONDICIONAL SIMPLE
# si el total no supera los S/. 95.00, entonces comprare mas viveres
if( total<95):
    print("Ud comprara mas viveres")
# fin_if
