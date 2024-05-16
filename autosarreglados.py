print("Bienvenido a Transporte LU")
otroviaje = True
import os
import time
limpieza_pantalla = "cls"
os.system(limpieza_pantalla)
while otroviaje != 2:
    print("Cada automovil tiene capacidad de 4 personas \n4 personas = $150000 \nSi son menos, cada persona paga $35000 y una multa de $50000 ")
    print("¿Cuantas personas van a ir?")
    while True:
        try:
            cant_pers = int(input("ingrese la cantidad: ")) 
            if cant_pers == 0:
                raise ValueError("valor invalido, ingrese otro")
            break
        except ValueError as e:
            print(e)
    
    time.sleep(1)
    os.system(limpieza_pantalla)
    vehiculos=cant_pers / 4
    
    if vehiculos <=1 and cant_pers == 4:
        vehiculos=1
        print(f"Empresas LU \nCantidad de vehiculos a usar: {vehiculos} \nCantidad de personas: {cant_pers} \nValor a pagar: $150000")
    elif vehiculos <= 1 and cant_pers <4:
        vehiculos=1
        print(f"Empresas LU \nCantidad de vehiculos a usar: {vehiculos} \nCantidad de personas: {cant_pers} \nValor a pagar: ${(35000 * cant_pers)+50000}")
    elif cant_pers >1.1 and (cant_pers % 2 == 0):
        vehiculos= int(vehiculos)
        print(f"Empresas LU \nCantidad de vehiculos a usar: {vehiculos}   \nCantidad de personas: {cant_pers} \nValor a pagar: ${150000 * vehiculos}")
    elif cant_pers >1.1:
        vehiculos= int(vehiculos)+1
        print(f"Empresas LU \nCantidad de vehiculos a usar: {vehiculos}   \nCantidad de personas: {cant_pers} \nValor a pagar: ${(35000 * cant_pers)+50000}")
    otroviaje = int(input("¿Desea otro viaje? si(1)/no(2): "))
print("Hasta luego")