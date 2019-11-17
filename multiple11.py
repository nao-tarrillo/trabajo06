import os

# BOLETA DE VENTA
# declarar variables
cliente,RUC,carro01,carro02,carro03,precio_del_carro01,precio_del_carro02,precio_del_carro03="",0,"","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
carro01=os.sys.argv[3]
carro02=os.sys.argv[4]
carro03=os.sys.argv[5]
precio_del_carro01=float(os.sys.argv[6])
precio_del_carro02=float(os.sys.argv[7])
precio_del_carro03=float(os.sys.argv[8])

# PROCESSING
total=(precio_del_carro01+precio_del_carro02+precio_del_carro03)

# VERIFICADOR
ganancia_de_vendedor=(total==100000)

#OUTPUT
print("#########################")
print("# SAC. TOYOTA-PERU")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# carro:", carro01,"                                    precio:  S/.", precio_del_carro01)
print("# carro:", carro02,"                                    precio:  S/.", precio_del_carro02)
print("# carro:", carro03,"                                    precio:  S/.", precio_del_carro03)
print("total:    S/.", total)
print("#########################")
print("# ganancia del vendedor:", ganancia_de_vendedor)

# CONDICIONAL MULTIPLE
# si el total supera los S/. 1 000 000.00, ganaste un auto mas
if( total>1000000):
    print("Ud ha ganado un auto mas")
# fin_if

# si el total es igual a S/. 1 000 000.00, ganaste una moto
if( total==1000000):
    print("Ud ha ganado una moto")
# fin_if

# si el trabajo es menor a S/. 1 000 000.00, ganaste una bicicleta
if( total<1000000):
    print("Ud ha ganado una bicicleta")
# fin_if
