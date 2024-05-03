nota1 = float(input("ingresa la primera nota: "))
nota2 = float(input("ingresa la segunda nota: "))
nota3 = float(input("ingresa la tercera nota: "))
promedio = float((nota1 + nota2 + nota3)/3)
print("su promedio es: ",promedio)
if promedio >= 4.0:
    print("felicidades, aprobaste")
else:
    print("reprobaste")