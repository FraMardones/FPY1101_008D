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
AlgoMas = True
codigo = True
nombrecodigo = True
otropedido = True
intentarDeNuevo = True
os.system("cls")

print("Bienvendo a nuestra tienda de sushi")
print("Nuestro menu es: \n1.Pikachu roll = $4500 \n2.Otaku roll = 5000 \n3.Pulpo Venenoso Roll = 5200 \n4.Angila Electrica Roll = 4800")
while otropedido != 2: 
        while AlgoMas != 2:    
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
                        AlgoMas = int(input("Desea algo mas? si(1)/no(2) "))
                break


        codigo = int(input("Tiene codigo de descuento? si(1)/no(2) "))
        os.system("cls")
        time.sleep(1)

        if codigo == 1:
                nombrecodigo = input("Ingrese el codigo: ")
                if nombrecodigo == "soyotaku":
                        os.system("cls")
                        time.sleep(1)
                        print(f"************************ \nTOTAL PRODUCTOS: {cantidad1 + cantidad2 + cantidad3 + cantidad4} \n************************")
                        print(f"Pikachu Roll : {cantidad1} \n Otaku Roll : {cantidad2} \n Pulpo Venenoso Roll : {cantidad3} \n Angila Electrica Roll : {cantidad4}")
                        print(F"************************ \n Subtotal por pagar: {(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4)} \n Descuento: {((Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4))*0.10} ")
                        print(f"TOTAL: {(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4) - ((Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4))*0.10} ")
                        
                elif nombrecodigo != "soyotaku":
                        while intentarDeNuevo != "X":
                                intentarDeNuevo = input("Codigo invalido, ingrese de nuevo el codigo o pulse X para no utilizar un codigo: ")
                                if intentarDeNuevo == "soyotaku":
                                        os.system("cls")
                                        time.sleep(1)
                                        print(f"************************ \nTOTAL PRODUCTOS: {cantidad1 + cantidad2 + cantidad3 + cantidad4} \n************************")
                                        print(f"Pikachu Roll : {cantidad1} \n Otaku Roll : {cantidad2} \n Pulpo Venenoso Roll : {cantidad3} \n Angila Electrica Roll : {cantidad4}")
                                        print(F"************************ \n Subtotal por pagar: {(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4)} \n Descuento: {((Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4))*0.10} ")
                                        print(f"TOTAL: {(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4) - ((Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4))*0.10} ")
                                elif intentarDeNuevo == "X":
                                        os.system("cls")
                                        time.sleep(1)
                                        print(f"************************ \nTOTAL PRODUCTOS: {cantidad1 + cantidad2 + cantidad3 + cantidad4} \n************************")
                                        print(f"Pikachu Roll : {cantidad1} \n Otaku Roll : {cantidad2} \n Pulpo Venenoso Roll : {cantidad3} \n Angila Electrica Roll : {cantidad4}")
                                        print(F"************************ \n Subtotal por pagar: {(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4)} \n Descuento: {((Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4))*0} ")
                                        print(f"TOTAL: {(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4) - ((Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4))*0} ")                       
        elif codigo == 2:
                os.system("cls")
                time.sleep(1)
                print(f"************************ \nTOTAL PRODUCTOS: {cantidad1 + cantidad2 + cantidad3 + cantidad4} \n************************")
                print(f"Pikachu Roll : {cantidad1} \n Otaku Roll : {cantidad2} \n Pulpo Venenoso Roll : {cantidad3} \n Angila Electrica Roll : {cantidad4}")
                print(F"************************ \n Subtotal por pagar: {(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4)} \n Descuento: {((Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4))*0} ")
                print(f"TOTAL: {(Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4) - ((Pikachuroll * cantidad1) + (Otakuroll * cantidad2) + (PulpoVenenosoRoll * cantidad3) + (AngilaElectricaRoll * cantidad4))*0} ")                       

otropedido = int(input("¿Desea hacer otro pedido?"))                        


        

        
