import os
import time
#Lista de los productos
productos={
    "Pan": 1000,
    "Queso" : 2500,
    "Salame" : 3000,
    "Huevos" : 2000
}
#Carro para almacenar
carro=[]

#Menu de opciones
while True:
    print("\nMenú:")
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")
    print("\n")
    opc=input("Ingrese la opcion : ")
    
    os.system("cls")
    time.sleep(1)
    
    if opc =="1":
        print("\nProductos disponibles: ")
        for i,producto in enumerate(productos, start=1):
            print(f"{i}. {producto} : ${productos[producto]:.2f}")
        seleccion = input("Seleccione un producto (1-5): ")
        
        os.system("cls")
        time.sleep(1)
        
        if seleccion in ['1', '2', '3', '4', '5']:
            producto_seleccionado = list(productos.keys())[int(seleccion) - 1]
            carro.append(producto_seleccionado)
            print(f"{producto_seleccionado} agregado al carro de compras.")
        else:
            print("Selección no válida, por favor intente de nuevo.")
            
            
            
    elif opc == "2":
        if carro:
            print("\nProductos en la canasta:")
            for producto in carro:
                print(f"- {producto}")
                
        else:
            print("La canasta está vacía.")
            
    elif opc == '3':
        total = 0
        for producto in carro:
            total += productos[producto]
        print(f"\nEl total a pagar es: ${total}")
        
    elif opc == '4':
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida, por favor intente de nuevo.")    