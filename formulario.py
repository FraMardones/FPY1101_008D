print("¿Cuál de los siguientes animales vive en el agua?")
print("1.Perro")
print("2.Cocodrilo")
print("3.Conejo")
print("4.Tiburón")
respuesta1 = input("Ingrese su respuesta (1-4): ")
if respuesta1 == "4":
    print("Correcto, ganaste 1 punto")
    respuesta1 = 1
elif respuesta1 == "2":
    print("Correcto, ganaste 0.5 puntos")
    respuesta1 = 0.5
else:
    print("Incorrecto")
    respuesta1 = 0
print("¿Cual es el pez protagonista de Buscando a nemo?")
print("1.Pez cirujano azul")
print("2.Pez mariposa")
print("3.Pez payaso")
print("4.Caballito de mar") 
respuesta2 = input("ingrese su respuesta (1-4): ")
if respuesta2 == "3":
    print("Correcto, ganaste 1 punto")
    respuesta2 = 1
elif respuesta2 == "1":
    print("Correcto, ganaste 0.5 puntos")
    respuesta2 = 0.5
else:
    print("Incorrecto")
    respuesta2 = 0
print("¿Cuales son los protagonistas de Dragon Ball?")
print("1.Freezer")
print("2.Goku")
print("3.Krilin")
print("4.Vegeta")
respuesta3 = input("Ingrese su respuesta (1-4): ")
if respuesta3 == "2":
    print("Correcto, ganaste 1 punto")
    respuesta3 = 1
elif respuesta3 == "4":
    print("Correcto, ganaste 0.5 puntos")
    respuesta3 = 0.5
else:
    print("Incorrecto")
    respuesta3 = 0
print("¿Cuales son los cantantes que ganaron la gaviota de platino en el festival de viña del mar? ")
print("1.Juan Gabriel")
print("2.Los Jaivas")
print("3.Luis Miguel")
print("4.Illapu")
respuesta4 = input("Ingrese su respuesta (1-4): ")
if respuesta4 == "3":
    print("Correcto, ganaste 1 punto")
    respuesta4 = 1
elif respuesta4 == "2":
    print("Correcto, ganaste 0.5 puntos")
    respuesta4 = 0.5
else:
    print("Incorrecto")
    respuesta4 = 0
resultado =float(respuesta1 + respuesta2 + respuesta3 + respuesta4)
if resultado == 0.0:
    print("Su nota es un 1.0")
elif resultado == 0.5:
    print("Su nota es un 1.6")
elif resultado == 1.0:
    print("Su nota es un 2.3")
elif resultado == 1.5:
    print("Su nota es un 2.9")   
elif resultado == 2.0:
    print("Su nota es un 3.5")
elif resultado == 2.5:
    print("Su nota es un 4.2")    
elif resultado == 3.0:
    print("Su nota es un 5.1")
elif resultado == 3.5:
    print("Su nota es un 6.1")
elif resultado == 4.0:
    print("Su nota es un 7.0")
