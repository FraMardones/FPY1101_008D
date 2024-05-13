import os
import time
Pikachuroll = 4500
Otakuroll = 5000
PulpoVenenosoRoll = 5200
AngilaElectricaRoll = 4800
cantidad1 = 0
cantidad2 = 0
cantidad3 = 0
cantidad4 = 0
algoMas = True
codigo = True
nombrecodigo = True
otropedido = True
intentarDeNuevo = True
os.system("cls")

print("Bienvendo a nuestra tienda de sushi")
print("Nuestro menu es: \n1.Pikachu roll = $4500 \n2.Otaku roll = 5000 \n3.Pulpo Venenoso Roll = 5200 \n4.Angila Electrica Roll = 4800")
while otropedido != 2: 
    algoMas = True
    while algoMas != 2:    
            eleccion = int(input("Elija su comida (1-4): "))
            if eleccion == 1:
                cantidad = int(input("¿Cuantos quiere? "))
                cantidad1 += cantidad
            elif eleccion == 2:
                cantidad = int(input("¿Cuantos quiere? "))
                cantidad2 += cantidad
            elif eleccion == 3:
                cantidad = int(input("¿Cuantos quiere? "))
                cantidad3 += cantidad
            elif eleccion == 4:
                cantidad = int(input("¿Cuantos quiere? "))
                cantidad4 += cantidad
            else:
                print("numero invalido")
            algoMas = int(input("Desea algo mas? si(1)/no(2) "))
    codigo = int(input("Tiene codigo de descuento? si(1)/no(2) "))
    
    os.system("cls")
    time.sleep(1)
    total = (f"{(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4)}")
    if codigo == 1:
        nombrecodigo = input("Ingrese el codigo: ")
        if nombrecodigo == "soyotaku":
            os.system("cls")
            time.sleep(1)
            print(f"************************ \nTOTAL PRODUCTOS: {cantidad1 + cantidad2 + cantidad3 + cantidad4} \n************************")
            print(f"Pikachu Roll : {cantidad1} \nOtaku Roll : {cantidad2} \nPulpo Venenoso Roll : {cantidad3} \nAngila Electrica Roll : {cantidad4}")
            print(F"************************ \nSubtotal por pagar: {total} \nDescuento: {float(total)*0.10} ")
            print(f"TOTAL: ",float(total) - ((float(total) * 0.10)))
            break
        elif nombrecodigo != "soyotaku":
            while intentarDeNuevo != "X":
                intentarDeNuevo = input("Codigo invalido, ingrese de nuevo el codigo o pulse X para no utilizar un codigo: ")
                if intentarDeNuevo == "soyotaku":
                    os.system("cls")
                    time.sleep(1)
                    print(f"************************ \nTOTAL PRODUCTOS: {cantidad1 + cantidad2 + cantidad3 + cantidad4} \n************************")
                    print(f"Pikachu Roll : {cantidad1} \nOtaku Roll : {cantidad2} \nPulpo Venenoso Roll : {cantidad3} \nAngila Electrica Roll : {cantidad4}")
                    print(F"************************ \nSubtotal por pagar: {total} \nDescuento: {float(total)*0.10} ")
                    print(f"TOTAL: ",float(total) - ((float(total) * 0.10)))
                    break
                elif intentarDeNuevo == "x" or intentarDeNuevo =="X":
                    os.system("cls")
                    time.sleep(1)
                    print(f"************************ \nTOTAL PRODUCTOS: {cantidad1 + cantidad2 + cantidad3 + cantidad4} \n************************")
                    print(f"Pikachu Roll : {cantidad1} \nOtaku Roll : {cantidad2} \nPulpo Venenoso Roll : {cantidad3} \nAngila Electrica Roll : {cantidad4}")
                    print(F"************************ ")
                    print(f"TOTAL: {total}")
                    break
    elif codigo == 2:
        os.system("cls")
        time.sleep(1)
        print(f"************************ \nTOTAL PRODUCTOS: {cantidad1 + cantidad2 + cantidad3 + cantidad4} \n************************")
        print(f"Pikachu Roll : {cantidad1} \nOtaku Roll : {cantidad2} \nPulpo Venenoso Roll : {cantidad3} \nAngila Electrica Roll : {cantidad4}")
        print(F"************************ ")
        print(f"TOTAL: {total}")
    
    otropedido = int(input("¿Desea hacer otro pedido? si(1)/no(2)"))
    os.system("cls")
    time.sleep(1)
    if otropedido == 2:
        print("Gracias por su compra!!")
        break