import os # La librería el módulo “os” hace posible el manejo de funciones dependientes del Sistema Operativo. 
          # Básicamente lo que hace es buscar un módulo interno en función al SO del ordenador y luego exporta 
          # la misma funcionalidad para así ejecutar las acciones necesarias dentro del programa.
import time # Este módulo proporciona varias funciones relacionadas con el tiempo. 


limpieza_pantalla = "cls"
# Saldo inicial en cuenta
saldo = 1000 
contador = 1
respuesta = 0
os.system(limpieza_pantalla) # llamado a la función de limpiar pantalla de la libreria OS con una variable llamada -> limpieza_pantalla
while contador <= 3:
    clave = input("Escribe la contraseña, solo 3 intentos : ")
    if clave == "abc":
	    contador = 4
    else:
        contador += 1
        if contador == 4:
            print("Has fallado los 3 intentos")
            respuesta = 4
        else:		
	        print("La contraseña es incorrecta")

while respuesta != 4:
        # Mostrar menú
            time.sleep(2) # Genera una pausa durante un tiempo (sleep = dormir) 
            os.system(limpieza_pantalla) # llamado a la función de limpiar pantalla de la libreria OS con una variable llamada -> limpieza_pantalla
        
            print("Bienvenido al Banco del País, seleccione una opción")
            print("1. Consultar Saldo")
            print("2. Depositar Dinero")
            print("3. Girar Dinero")
            print("4. Salir")
            # Opciones de manejo de error
            try:
                respuesta = int(input("Selecciona una opción (1-4):"))
            except ValueError:
                print("Selecciona una opción (1-4), ya que la elegida es incorrecta")
                continue

            # Realizar acciones según la opción seleccionada
            if respuesta == 1:
                print(f"Tu saldo actual es: ${saldo}")
            elif respuesta == 2:
                cantidad_deposito = float(input("Ingrese la cantidad a depositar: $"))
                saldo = saldo + cantidad_deposito
                print(f"Has retirado ${cantidad_deposito}. Nuevo saldo: ${saldo}")
            elif respuesta == 3:
                cantidad_retiro = float(input("Ingrese la cantidad a retirar: $"))
                if cantidad_retiro <= saldo:
                    saldo -= cantidad_retiro
                    print(f"Has retirado ${cantidad_retiro}. Nuevo saldo: ${saldo}")
                else:
                    print("Saldo insuficiente. No es posible realizar el retiro.")
            elif respuesta == 4:
                print("Gracias por utilizar el Cajero.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

				
		
