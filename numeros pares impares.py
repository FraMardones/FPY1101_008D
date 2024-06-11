numeros = (input("Ingrese una lista de numeros separadas por espacios: "))


def validar_datos():
    while True:
        try:
            pass
        except:
            if (numeros.split()) != int:
                print("valor invalido, ingrelos de nuevo")
            break

par = []
impar = []
for numeros in range(int(numeros)):
    if int(numeros) % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)

print(par)
print(impar)