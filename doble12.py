import os

# BOLETA DE VENTA
# declarar variables
cliente,carro01,carro02,carro03,precio_del_carro01,precio_del_carro02,precio_del_carro03="","","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
carro01=os.sys.argv[2]
carro02=os.sys.argv[3]
carro03=os.sys.argv[4]
precio_del_carro01=float(os.sys.argv[5])
precio_del_carro02=float(os.sys.argv[6])
precio_del_carro03=float(os.sys.argv[7])

# PROCESSING
total=(precio_del_carro01+precio_del_carro02+precio_del_carro03)

# VERIFICADOR
ganancia_de_vendedor=(total==100000)

#OUTPUT
print("#########################")
print("# SAC. TOYOTA-PERU")
print("#########################")
print("# cliente:", cliente)
print("# carro:", carro01,"                                    precio:  S/.", precio_del_carro01)
print("# carro:", carro02,"                                    precio:  S/.", precio_del_carro02)
print("# carro:", carro03,"                                    precio:  S/.", precio_del_carro03)
print("total:    S/.", total)
print("#########################")
print("# ganancia del vendedor:", ganancia_de_vendedor)
print("#########################")

# CONDICIONAL DOBLE
# si el total es mayor a S/. 800 000.00, ganaste el auto mas veloz
if( total>800000):
    print("Ud ha ganado el auto mas veloz")
else:
    print("Ud ha ganado el auto mas lento")
# fin_if
