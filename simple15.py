import os

# BOLETA DE VENTA
# declarar variables
cliente,marca_de_celular01,marca_de_celular02,marca_de_celular03,precio_del_celular01,precio_del_celular02,precio_del_celular03="","","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
marca_de_celular01=os.sys.argv[2]
marca_de_celular02=os.sys.argv[3]
marca_de_celular03=os.sys.argv[4]
precio_del_celular01=float(os.sys.argv[5])
precio_del_celular02=float(os.sys.argv[6])
precio_del_celular03=float(os.sys.argv[7])

# PROCESSING
total=(precio_del_celular01+precio_del_celular02+precio_del_celular03)

# VERIFICADOR
ganancia=(total==total and total!=total)

#OUTPUT
print("#########################")
print("# Centro comercial:    LA NUEVA TECNOLOGIA ")
print("#########################")
print("# cliente:", cliente)
print("# celular:", marca_de_celular01,"               precio:  S/.", precio_del_celular01)
print("# celular:", marca_de_celular02,"               precio:  S/.", precio_del_celular02)
print("# celular:", marca_de_celular03,"               precio:  S/.", precio_del_celular03)
print("# total:  S/.", total)
print("#########################")
print("# ganancia:", ganancia)
print("#########################")

# CONDICIONAL DOBLE
# si el total no supera los S/. 200.00, habra comprado celulatres daniados
if( total<200):
    print("Ud a comprado celulares daniados")
# fin_if
