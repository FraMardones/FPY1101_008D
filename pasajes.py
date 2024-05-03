import os
import time
limpieza_pantalla = "cls"
os.system(limpieza_pantalla)
print("Bienvenido")
preciototal = 0
nropasaje = 1
cantidad = int(input("Ingresa la cantidad de pasajes para vender: "))
for i in range(cantidad):
    try:
        precio = int(input(f"Ingresa el precio del pasaje {nropasaje}: "))
        nropasaje += 1
    except ValueError:
        print("El valor ingresado no es valido.")
        break
    preciototal += precio

time.sleep(1)
print("---------------------------------------------")
print(f"El precio total por todo es de: ${preciototal} ")
print("---------------------------------------------")
